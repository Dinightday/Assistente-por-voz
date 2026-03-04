from decisao import Decisao
from escuta import escuta
import asyncio
from decisao import Estado
import os

async def ir():
    os.system('cls')
    state = Estado()
    work = Decisao()
    grafo = work.grafo()
    while True:

        pergunta = await asyncio.to_thread(escuta)

        inputs = {
            "query": pergunta
        }

        resposta = await grafo.ainvoke(inputs)
        response_final = resposta.get("resposta_final")
        print(response_final)

if __name__ == "__main__":
    asyncio.run(ir())