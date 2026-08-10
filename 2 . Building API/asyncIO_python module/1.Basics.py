import asyncio
from doctest import debug
import time

## https://www.youtube.com/watch?v=3E-Ym2mbSCc
## https://www.youtube.com/playlist?list=PLhTjy8cBISEpfMihZ8E5yynf5sqPCcBXD

## a process is a program under execution or instance of a program or code+runtime activities
## process as a data structure in operating system [stack , heap  ,  datasection , codesection ]
## process is a collection of code, data and resources 

## when we need to create multiple instances of a prgrammm (same process) but very lil varitaion in data or logic
## then we dont try to create multiple same processess as it will be costly(need more sapce in main memory) and not efficient
## we just lightweight-copy the process in such a way - we will keep shareable thing common 
# and seperable things different for that process

## shared among thread  -  codesection , data section  , OS Resources . openFiles and signals
## uniques for each thread - Thread ID , RegisterSet , stack , program counter




## Multi-threading programming :  it is about workers {naturo clones doing diff things simultaniously}    threds
## async programming : is about the tasks  {you alone simultaneouly doing diff things}  
## multi processing / prallel programming: multiple cores inside the cpu can actually exceute the tasks in parallel 
# import  multiprocessing
# print(f"Number of CPUs : {multiprocessing.cpu_count()}")

##### aync programming ### 
### coroutines : a program component that can pause its work and resume later without blocking system threads

## normal way
# def a():
#     value = b()
#     print(value)


# def b():
#     time.sleep(5)
#     return 5


# a()
## async program

# import asyncio

# async def a(sec:int = 1): #  --> retuerns a corutin object 
#     time.sleep(sec)
#     print(f"Result form a : after {sec}s")

# a()  ## RuntimeWarning: coroutine 'a' was never awaited

##### Async Envent - Loop ####


## to execute a co-routine you need an event-loop , Asyncio.run autonatically creates this asyc event loop

# asyncio.run(a(2))


## now the old and hard manual way : 
# 1 . create event loop
# 2. create co-routine 
# 3. execute that co-routine using our own event-loop 

# #create event loop
# loop = asyncio.new_event_loop()
# print(loop)

# #create co-routine 
# task1 = asyncio.sleep(2) ## behind the seen creats co routine

# ## execute a task
# loop.run_until_complete(task1)

# # report message
# print("Done")



# ### async keyworod is to create a coroutine
# ### await keyword is to pause a coroutine 

# async def square(num):
#     result =  num*num
#     return result

# async def main():

#     x = await square(5)
#     print(x)

#     y =  await square(10)
#     print(y)


#     z = x+y
#     print(z)


# asyncio.run(main())
## this looking like a sync code why even  async await  in real_example.py








# def sync_func(test_param: str) -> str:
#     print("This is sync funtion")
#     time.sleep(1)
#     return f"sync Result : {test_param}"


# async def async_func(test_param: str) -> str:
#     print("This is async funtion")
#     await asyncio.sleep(1)
#     return f"async Result : {test_param}"


# async def main():
#     # result = sync_func("Anish")
#     # print(result)

#     # awaitables -> objects that has __await__ method

#     loop = asyncio.get_event_loop()
#     future = (
#         loop.create_future()
#     )  # a promise -like object that represents a future result of an asynchronous operation

#     print(f"future object [empty] : {future}")


#     future.set_result("Anish")
#     future_result = await future
#     print(f"future object [filled] : {future_result}")

# if __name__ == "__main__":
#     asyncio.run(main())
