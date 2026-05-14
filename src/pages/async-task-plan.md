---
title: AsyncTask — Plan
date: 2026-05-14
status: draft, pending review with Diego
---

# AsyncTask — sub-agents que NO bloquean el chat

## Problema

Hoy `Task` (Cluster 3, 14 mayo) corre sub-agentes con context window propio, pero es **síncrono**: mi turn principal se queda bloqueado esperando a que el sub-agent termine. En la prueba real del 14/05 a las 12:10, una investigación del watchdog tardó **104 segundos**, durante los cuales el DM con Diego estuvo congelado.

Eso rompe el modelo mental que esperaba Diego: "si delego a un sub-agent, vuelvo a estar disponible".

## Objetivo

Que invocar `Task` sea fire-and-forget desde el punto de vista del turn principal:

1. Yo decido lanzar un sub-agent.
2. Recibo un `task_id` y un ack inmediato.
3. Respondo a Diego con "lanzado, te aviso cuando termine".
4. Mi turn principal termina y el dispatcher queda libre.
5. El sub-agent corre en un proceso separado.
6. Cuando termina, el resultado entra al dispatcher como si fuera un mensaje más, y rutea al chat correcto.

## Diseño propuesto

### Componentes

**1. `async_task_runner.py`** — script standalone que corre un sub-agent.
- Recibe por CLI: `task_id`, `prompt`, `chat_id`, `topic_id`, `parent_message_id` (para reply), `system_prompt_kind`, `tool_set`.
- Carga credenciales, ejecuta `_run_tool_loop` con los args dados.
- Al terminar: escribe resultado a `/tmp/async_tasks/$task_id.json` con `{status, result, error, started_at, ended_at, tokens, iters}`.
- Manda mensaje a Telegram con el resultado, en el chat/topic original.

**2. Modificación de `task_tool.py`** — la tool ya no corre el sub-agent inline.
- En vez de llamar `run_loop` síncronamente, genera un `task_id`, spawneа `async_task_runner.py` con `subprocess.Popen(..., start_new_session=True)` (proceso huérfano, sobrevive a que mi turn termine), y devuelve inmediatamente:
  ```
  Sub-agent launched. task_id=abc123. ETA based on prompt complexity: 1-3 min.
  You'll be notified when it completes.
  ```

**3. Watcher en el dispatcher** — opcional, sólo si queremos UI rica.
- Lee `/tmp/async_tasks/*.json` cada N segundos.
- Cuando ve `status: complete`, formatea + manda mensaje, mueve fichero a `archive/`.
- Alternativa: el propio `async_task_runner.py` manda el mensaje al terminar, sin watcher. **Simpler. Esta es mi preferencia.**

### Lifecycle de un task

```
[T0]   Diego pide algo.
[T0+1] Mi turn invoca Task, recibe task_id=abc123.
[T0+2] Yo respondo a Diego: "lanzado, te aviso, ETA ~2min".
[T0+3] Mi turn termina. Dispatcher libre.
[T1]   En paralelo, async_task_runner.py ejecuta sub-agent.
[T1+N] Termina. Manda mensaje al chat/topic con el resultado.
[T1+N] Diego ve el resultado, puede responder, ciclo normal.
```

### Decisiones de diseño

| Pregunta | Propuesta | Razón |
|---|---|---|
| ¿Dónde viven los tasks en curso? | `/tmp/async_tasks/$task_id.json` | Efímero, OS limpia en reboot |
| ¿Cómo se llama el sub-agent? | `nohup python3 async_task_runner.py ... &` con `start_new_session=True` | Sobrevive a SIGHUP del parent |
| ¿Y si el dispatcher se reinicia? | Tasks siguen corriendo (proceso huérfano). Cuando terminan, mandan mensaje Telegram directo (no via dispatcher). Funciona. | Robusto a restarts |
| ¿Y si el chat ya no existe? | El send falla, el resultado queda en el JSON, no se pierde nada. | Tolerante |
| ¿Cuántos sub-agents en paralelo? | Cap inicial: 3. Si Diego dispara un 4º, devolver error "demasiados tasks en curso". | Cost control |
| ¿Cómo se cancela un task? | Comando `/cancel_task abc123` en el DM, kill PID guardado en el JSON. | Esencial |
| ¿Visibilidad del progreso? | El sub-agent puede editar un "progress message" en Telegram via su propia Bash tool. | Reutiliza patrón existente |
| ¿Coste runaway? | `MAX_TOOL_ITERATIONS=32` para sub-agents (la mitad del parent). `MAX_TOKENS=8000`. | Sub-agents son baratos por diseño |

### Plan de implementación

Estimación: ~1.5h-Rook si no hay sorpresas.

1. **`async_task_runner.py`** (~45 min). Standalone, args CLI, ejecuta el loop, manda Telegram, escribe JSON.
2. **Modificar `task_tool.py`** (~15 min). Spawn en vez de inline.
3. **`/cancel_task` handler en dispatcher** (~15 min).
4. **Smoke test end-to-end** (~15 min): lanzar un task, verificar que vuelvo a estar disponible inmediatamente, verificar que el resultado llega.

### Decisiones abiertas (para discutir con Diego)

1. **¿Mensaje del sub-agent va al chat donde se lanzó, o siempre al DM de Diego?** Mi voto: al chat donde se lanzó. Si Diego dispara un Task en Workshop, la respuesta debe llegar a Workshop, no contaminar el DM.

2. **¿El sub-agent puede invocar Task recursivamente?** Mi voto: NO. Un sub-agent no spawnea más sub-agents. Evita bombas exponenciales.

3. **¿Auto-resumen del resultado si es muy largo?** Por ejemplo si el sub-agent devuelve 8KB de texto. Mi voto: no, Telegram parte mensajes largos automáticamente.

4. **¿Persistencia de tasks históricos?** Hoy estoy proponiendo `/tmp` (efímero). ¿Quiere Diego logs persistentes en `~/.openclaw/async_tasks_log/`?

5. **¿Notificación de progreso intermedia?** Si un task tarda > 2 min, ¿mando un mensaje cada N iteraciones del sub-agent? Mi voto: NO por defecto, sólo si el prompt lo pide explícitamente.

## No incluido en este plan

- **Sub-agents persistentes/conversacionales** (hacer una conversación de varios turnos con un sub-agent). Eso es otra cosa. Hoy Task es one-shot.
- **Cola priorizada de tasks.** Si llegan 10 a la vez, el cap de 3 los rechaza. No hay queue.
- **Streaming del progreso del sub-agent al chat token-a-token.** Eso es `sendMessageDraft` que aplazamos a la próxima semana también.
