import asyncio
async def task(name):
    print("Starting",name)
    await asyncio.sleep(2)
    print("Finished",name)
    
async def main():
    await asyncio.gather(task("Task A"),task("Task B"),task("Task C"))

asyncio.run(main())