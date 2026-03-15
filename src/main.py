# main.py - ponto de entrada da aplicação FastAPI

# Importa a biblioteca FastAPI para criar a aplicação e incluir rotas
from fastapi import FastAPI
from src.routers.endpoints import router as products_router


# Cria a aplicação FastAPI com informações de título, descrição e versão
app = FastAPI(
    title="Products API",
    description="API REST para gerenciamento de produtos",
    version="1.0.0"
)

# Inclui as rotas definidas em routers/products.py
app.include_router(products_router)

# Rota raiz para verificar se a API está rodando
@app.get("/")
def home():
    return {"message": "Products API running"}
