# Decisão por LangGraph
from langgraph.graph import StateGraph, START, END
from config import Baseconfig
from langchain_ollama import ChatOllama
from typing import TypedDict, Literal
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from especialistas.web import Pesquisar

class Estado(TypedDict):
    query: str
    resposta_decisao: Literal["web_search", "nada"]
    responta_final: str

class Decisao(Baseconfig):
    def __init__(self):
        self.llm = ChatOllama(model="gemma3:4b")

    async def decisao(self, estado: Estado):
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", """Transforme o comentário do usuário em um rótulo técnico.
            REGRAS OBRIGATÓRIAS:
            1. Se o usuário quiser pesquisar, buscar, usar a web ou internet, responda apenas: web_search
            2. Caso contrário, responda apenas: nada
            3. Proibido usar pontos, letras maiúsculas, espaços ou justificativas.
            4. Responda apenas a palavra-chave seca."""),
                ("human", "{query}")
            ]
        )
        
        chain = ({"query": RunnablePassthrough()} 
                 | prompt 
                 | self.llm 
                 | StrOutputParser())

        response = await chain.ainvoke(estado["query"])

        return {"resposta_decisao": response}
    
    async def pesquisar_web(self, estado: Estado):
        buscar = Pesquisar()

        url = input("Link: ")

        pesquisa = buscar.pesquisa(url)
        return {"responta_final": pesquisa}

    async def nada(self, estado: Estado):
        return {"responta_final": "nada"}
    
    async def roteador(self, estado: Estado) -> Literal["web_search", "nada"]:
        if estado["resposta_decisao"] == "web_search":
            return "web_search"
        else:
            return "nada"
        
    def grafo(self):
        workflow = StateGraph(Estado)

        workflow.add_node("decidir", self.decisao)
        workflow.add_node("web", self.pesquisar_web)
        workflow.add_node("nothing", self.nada)
        workflow.add_edge(START, "decidir")
        workflow.add_conditional_edges(
            "decidir",
            self.roteador,
            {
                "web_search": "web",
                "nada": "nothing"
            }
        )

        workflow.add_edge("web", END)
        workflow.add_edge("nothing", END)
        return workflow.compile()