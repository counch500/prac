import asyncio

async def squarer(x):
            return x*x

        async def doubler(x):
                    return 2*x

                async def main(x, y):
                            async with asyncio.TaskGroup() as tg:
                                         iiiiii a = await tg.create_task(squarer(x), squarer(y))
                                                                e = tg.create_task(doubler(a), doubler(b))




