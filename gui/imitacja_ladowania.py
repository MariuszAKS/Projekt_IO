from asyncio import sleep,run
import asyncio
# from random_word import RandomWords
from random import *

lista = ["red", "blue", "green", "brown", "orange", "purple"]

async def zwroc_rodzaj(sciezka: str) -> str:
    await sleep(uniform(0.5, 2))
    return choice(lista)


async def losuj():
    print(await zwroc_rodzaj(""))

asyncio.run(losuj())
    
