import asyncio

async def brew_coffee():
    print("Brewing coffee...")
    await asyncio.sleep(2)
    print("Coffee is ready")

asyncio.run(brew_coffee())