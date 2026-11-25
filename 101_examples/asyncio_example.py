import asyncio


async def worker(done): # async allows the function to pause
    await asyncio.sleep(2) # sleep is just a function to wait 2s 
    print("2. work finished") 
    done.set() # a flag that return: the job has been done


async def main():
    done = asyncio.Event() # open the job

    # define the task, on this example the work must have the job done
    task = asyncio.create_task(worker(done)) 


    print("1. waiting...")
    # return if the task was done
    await done.wait()


    print("3. continue")


asyncio.run(main()) # allows the code wait
