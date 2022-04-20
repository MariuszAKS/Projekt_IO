from imitacja_ladowania import zwroc_rodzaj
import asyncio


async def odczytaj(sciezki: list) -> list:
    rodzaje = [None] * len(sciezki)
    # for i, sciezka in asyncio.as_completed(sciezki):
    #     rodzaje[i] = zwroc_rodzaj(sciezka)