from fastapi import FastAPI
from fastapi.responses import JSONResponse
import asyncio


app = FastAPI()


@app.get("/wait")
async def wait():
    await asyncio.sleep(10)
    return JSONResponse(status_code=200, content={"message": "heavy tasks done"})


@app.get("/light")
async def light():
    return JSONResponse(status_code=200, content={"message": "light tasks done"})


# =============================================================================
# HOW THIS RUNS ON FASTAPI'S EVENT LOOP (what you see in Swagger/docs)
# =============================================================================
#
# 1) Uvicorn starts ONE event loop (single thread) for your app.
#    FastAPI route handlers marked `async def` become coroutines on that loop.
#
# 2) You click GET /wait once:
#    - `wait()` starts → hits `await asyncio.sleep(10)`
#    - sleep does NOT block the whole server for 10 seconds
#    - it tells the event loop: "wake me after 10s, run other work meanwhile"
#    - control returns to the event loop immediately
#
# 3) While /wait is "sleeping", you click GET /light 3–4 times:
#    - each /light request is picked up by the SAME event loop
#    - /light has no await/sleep → runs instantly → JSON response right away
#    - that's why /light works even though /wait is still waiting
#
# 4) After ~10 seconds:
#    - the event loop resumes the /wait coroutine(s)
#    - they finish and return {"message": "heavy tasks done"}
#
# 5) If you click /wait 3–4 times quickly:
#    - all those requests start their 10s sleep concurrently (interleaved on one loop)
#    - they don't queue behind each other like blocking `time.sleep(10)` would
#    - roughly all finish around the same time (~10s), not 10+10+10+10
#
# KEY IDEA:
#   `await asyncio.sleep(10)`  → cooperative, non-blocking (good for async APIs)
#   `time.sleep(10)` in async   → blocks the event loop (bad — /light would also hang)
#
# FLOW (simplified):
#
#   Time 0s:  click /wait  → coroutine sleeps (yields to loop)
#   Time 1s:  click /light → instant response
#   Time 2s:  click /light → instant response
#   Time 3s:  click /light → instant response
#   Time 10s: /wait wakes up → returns response
#
# FastAPI + Starlette + uvicorn manage this loop for you automatically.
# You only need `async def` + `await` on I/O-bound work (sleep, DB, HTTP calls, etc.).


# FastAPI async routes run on the main thread’s event loop, not on separate threads per request.
#  Concurrency comes from switching between waiting tasks, not from parallel threads 
# — unless FastAPI/uvicorn explicitly uses a thread pool for sync code.

## Main thread = the one Python process starts with (often the only thread in a simple uvicorn app).

## Event loop = a scheduler inside that thread. It picks which coroutine runs next.

## await asyncio.sleep(10) = “pause this request, let the loop run other coroutines.” It does not spawn a new thread.