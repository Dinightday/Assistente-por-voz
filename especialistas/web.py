from config import Baseconfig
from langchain_community.document_loaders import WebBaseLoader

class Pesquisar(Baseconfig):
    def __init__(self):
        super().__init__(modelo="gpt-4o-mini")
    
    def pesquisa(self, url):
        documentoweb = WebBaseLoader(url)
        loader_web = documentoweb.load()
        return loader_web