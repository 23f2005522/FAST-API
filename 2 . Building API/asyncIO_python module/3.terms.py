# https://www.youtube.com/watch?v=QlkXji08lno
## There a 3 main approaches to concurrency in python threading ,  multi processing  , asyncio

## threading : is prefenct for i/o bound task like network request , file optn , or waiting for external resources
## Python Global Interpreter Lock (GIL) :  restricts the execution of Python bytecode to a single thread at a time,
# even on a multi-core processor , multiple Python threads cannot run compute-heavy tasks truly in parallel within a single process
# but if one thread is waiting for someting it doest say other in that time cant wrok hence achiveing concurrency


## Multi processing : unlike threading here seperate python process is created with own sepearte memory space and python interpreter
# that means they can truely run in parallel even for cpu bound tasks because each process has its own GIL (data processing ,
# heavy calc)

##  when canfused btw therading or multiprocessing think of your task waits most of the time or need cpu for excutuion
# most of the time


## Asyncio :  pythons modern apporach to async programming just like threading  does not use the threading module for its core loop.
# Instead, asyncio uses a single-threaded event loop to switch between tasks , co-rotuines cooperatively using async and await
#  key adv : more effiect than threading module in I/O tasks (highly concurrent I/O-bound tasks)


# asyncio is single threaded and runs on a single process it uses Co-operative multi tasking where task volumtarily
# giveus up control Consequently,


# import asyncio


# async def main():
#     loop = asyncio.get_running_loop()
#     future = loop.create_future()  # a promise like obj
#     print(f"Pending Future : {future}")

#     future.set_result("ReultXYZ") ## set_exception() -- > for error
#     future_result = await future ## there are 3 types of await able corouties , Tasks (wrapper around Coroutines) , Futures (like js promise)
#     print(future_result)

# # but we dont direclty use Futures as asyncio uses it underthe hood as an abstruction and traks the results of Tasks

# if __name__ == "__main__":
#     asyncio.run(main())

# FLOW

# Python starts
#    |
#    v
# __name__ == "__main__"
#    |
#    v
# asyncio.run(main())
#    |
#    v
# Create event loop
#    |
#    v
# Start loop
#    |
#    v
# Run main()
#    |
#    +--> get_running_loop()
#    |
#    +--> create Future
#    |
#    +--> set_result()
#    |
#    +--> await Future
#    |
#    +--> print("ResultXYZ")
#    |
#    v
# main() finishes
#    |
#    v
# Event loop cleaned up
#    |
#    v
# asyncio.run() returns


# 1. Modern/simple way: asyncio.run()

# import asyncio

# async def main():
#     loop = asyncio.get_running_loop()
#     print(loop)

# asyncio.run(main())

# Here asyncio.run(main()) creates and manages the event loop for you.

# Inside main() ,  loop = asyncio.get_running_loop() does not create a new loop.
# It means Give me the event loop that is currently running this coroutine.

# asyncio.run(main())
#        |
#        | creates
#        v
#    Event Loop
#        |
#        | runs
#        v
#      main()
#        |
#        | get_running_loop()
#        v
#    SAME Event Loop


# 2. Manual/low-level way

# import asyncio

# async def main():
#     print("Hello")


# loop = asyncio.new_event_loop()

# loop.run_until_complete(main())

# loop.close()


# new_event_loop()
#        |
#        v
# Create loop
#        |
#        v
# run_until_complete(main())
#        |
#        v
# Run coroutine
#        |
#        v
# main finishes
#        |
#        v
# loop.close()


# import asyncio

# ## A coroutine function is a special type of function that can pause its work,
# # save its state, and resume later from where it stopped

# async def async_func(task_id):  #thos is how  a corutine func is made with async def keyword
#     print("This is a async coturine function")
#     await asyncio.sleep(0.5)
#     return f"Asyc Task {task_id} Done -- Result"


# async def main():

#     coro_obj  = async_func("1")
#     print(coro_obj)  ## <coroutine object async_func at 0x000002461C0B1600>  and await able object

#     coro_obj_res = await coro_obj
#     print(coro_obj_res)


# if __name__ == "__main__":
#     asyncio.run(main())


## Tasks  : are the wrapped corutintes that  can be executed independently , tasks are how we run the courutines concurrently
import asyncio


async def async_func(
    task_id, sec
):  # thos is how  a corutine func is made with async def keyword
    print("This is a async coturine function")
    await asyncio.sleep(sec)
    return f"Asyc Task {task_id} Done -- Result"


async def main():

    # Pass coroutines directly into gather() to run them concurrently
    results = await asyncio.gather(
        async_func("1", 4), async_func("2", 5), async_func("3", 2)
    )

    # Results are returned as a list matching the submission order
    print(f"All done! Results: {results}")


if __name__ == "__main__":
    asyncio.run(main())
 