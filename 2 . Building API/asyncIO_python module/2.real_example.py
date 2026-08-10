import asyncio
import time


## see next example 
# start  = time.time()

# async def get_moive_tickits():
#     await asyncio.sleep(3)
#     print("got tickits")


# async def like_ig_posts():
#     await asyncio.sleep(1)
#     print("Liked all")

# async def main():

#     await get_moive_tickits()
#     await like_ig_posts()

# asyncio.run(main())

# end  = time.time()

# print(f"all task done in {end - start}sec")   ## its still like the async only 





start  = time.time()

async def get_moive_tickits():
    await asyncio.sleep(3)
    print("got tickits")


async def like_ig_posts():
    await asyncio.sleep(1)
    print("Liked all")

async def main():

    # await coro()   Execution : Pauses the code until the job finishes. 
    #                Concurrency : Runs one thing at a time (sequential).

    ## starts a coroutine in the background. It wraps your async function in a Task object and schedules 
    # it right away on the event loop. This lets your program run multiple jobs
    #  at the same time instead of waiting for one to finish before starting the next


    #asyncio.create_task(coro()) Execution : Starts the job and moves to the next line right away.  
    #                            Concurrency : Runs multiple things at the same time (concurrent).

    task1  = asyncio.create_task( get_moive_tickits())     ## return a Task Object
    await like_ig_posts()
    await task1

    ## # await task1 <-- if REMOVED :: Because like_ig_posts() only takes 1 second, the main() function will finish
    #  and the program will print the total time after just 1 second.
    #  The background task will get cut off and destroyed before it ever finishes printing "got tickets".




    ## Coroutine Object: This is a passive object. It is just a wrapper around your function's code and state.
    #                    It does absolutely nothing on its own. If you don't explicitly run it, it sits idle

    # ┌────────────────────────────────────────────────────────┐
    # │               COROUTINE OBJECT (coro)                  │
    # ├───────────────────┬────────────────────────────────────┤
    # │ cr_code           │ Points to the actual Python byte-  │
    # │                   │ code of your async def function.   │
    # ├───────────────────┼────────────────────────────────────┤
    # │ cr_frame          │ Holds local variables and the      │
    # │                   │ current line execution pointer.    │
    # ├───────────────────┼────────────────────────────────────┤
    # │ cr_running        │ Boolean flag (True or False).      │
    # ├───────────────────┼────────────────────────────────────┤
    # │ cr_await          │ Points to what this coroutine is   │
    # │                   │ currently awaiting (e.g., sleep).  │
    # └───────────────────┴────────────────────────────────────┘

    #Task Object: This is an active, scheduled job. When you wrap a coroutine in a Task (via asyncio.create_task()),
    #             you hand it over to Python's event loop. Python immediately manages its execution in the background.

    # ┌────────────────────────────────────────────────────────┐
    # │                  TASK OBJECT (task1)                   │
    # ├───────────────────┬────────────────────────────────────┤
    # │ _coro             │ ──► [ Points to Coroutine Object ] │
    # ├───────────────────┼────────────────────────────────────┤
    # │ _state            │ 'PENDING', 'FINISHED', or 'CANCELLED'│
    # ├───────────────────┼────────────────────────────────────┤
    # │ _result           │ Holds returned value when done.    │
    # ├───────────────────┼────────────────────────────────────┤
    # │ _exception        │ Holds any error if the task fails. │
    # ├───────────────────┼────────────────────────────────────┤
    # │ _callbacks        │ List of functions to run when done.│
    # └───────────────────┴────────────────────────────────────┘


    ####### Visual Analogy ###########
    # [ Coroutine Function ] (async def get_movie_tickets)
    #    │
    #    ▼ (Call it)
    # [ Coroutine Object ] ───► A static plan of work (Does nothing yet)
    #    │
    #    ▼ (Pass to asyncio.create_task)
    # [   Task Object    ] ───► An active process managed by the Event Loop

asyncio.run(main())

end  = time.time()

print(f"all task done in {end - start}sec")  



# why we need use sayncio.sleep with async corotuine funtions  : 
# Because asyncio.sleep() is a non-blocking way to simulate or perform waiting inside an async program
##The key is not really the sleep itself. The important part is what happens to the event loop while we are waiting.

## 1. Normal time.sleep()


# import time

# def task_a():
#     print("A started")
#     time.sleep(5)
#     print("A finished")

## time.sleep(5) blocks the entire current thread:

# Event Loop Thread
# │
# ├── Task A
# │    │
# │    └── time.sleep(5)
# │           ↓
# │        BLOCKED
# │
# └── Task B
#      ↓
#    cannot run


# So if you do this inside an async function:

# async def task_a():
#     time.sleep(5)


## you are basically telling the event-loop thread:  "Stop everything for 5 seconds."




## 2. asyncio.sleep()

# import asyncio

# async def task_a():
#     print("A started")
#     await asyncio.sleep(5)
#     print("A finished")
 
# here  await asyncio.sleep(5) means: "I don't need the CPU for the next 5 seconds.
#                                        Pause this coroutine and let the event loop do other work."



# Event Loop
# │
# ├── Task A
# │    │
# │    └── await asyncio.sleep(5)
# │             │
# │             └── SUSPEND A
# │
# ├── Task B  ← runs
# │
# ├── Task C  ← runs
# │
# └── Task D  ← runs


# After 5 seconds:

# Task A
#    │
#    └── resumes
#         │
#         └── print("A finished")