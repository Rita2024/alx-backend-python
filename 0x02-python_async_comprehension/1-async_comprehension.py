from async_generator import async_generator, yield_

async def async_comprehension():
    async with async_generator() as agen:
        # Use async comprehensions to collect 10 random numbers
        result = [number async for number in agen][:10]
    
    return result

