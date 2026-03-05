# Este arquivo define as rotas para gerenciamento de produtos usando FastAPI.
# Importa o modelo de produto, manipula os dados e define os endpoints para criar, ler, atualizar e deletar produtos.


# Importa a biblioteca FastAPI para criar rotas e HTTPException para lidar com erros HTTP
from fastapi import APIRouter, HTTPException
# Importa a biblioteca json para ler e escrever no arquivo de dados
import json
# Importa o modelo de produto definido em models/product.py
from models.product import Product


# Cria um roteador para as rotas de produtos
router = APIRouter()

# Lê o arquivo data.json e armazena os dados em "products"
with open("data/data.json") as f:
    products = json.load(f)

# Função para salvar os produtos no arquivo JSON
def save_products():
    with open("data/data.json", "w") as f:
        json.dump(products, f, indent=4)

# Endpoint para obter a lista de produtos, com opção de filtrar por categoria
@router.get("/products")
def get_products(category: str = None):
    if category:
        filtered = [p for p in products if p["category"] == category]
        return filtered
    return products

# Endpoint para obter um produto específico pelo seu ID
@router.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    # Retorna erro HTTP 404 se não encontrar
    raise HTTPException(status_code=404, detail="Product not found")

# Endpoint para criar um novo produto
@router.post("/products")
def add_product(product: Product):
    new_product = product.dict()
    products.append(new_product)
    save_products()
    return {
        "message": "Product added",
        "product": new_product
    }

# Endpoint para atualizar um produto existente pelo seu ID
@router.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            products[index] = updated_product.dict()
            save_products()
            return {"message": "Product updated"}
    # Retorna erro HTTP 404 se não encontrar
    raise HTTPException(status_code=404, detail="Product not found")

# Endpoint para deletar um produto pelo seu ID
@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            save_products()
            return {"message": "Product deleted"}
    # Retorna erro HTTP 404 se não encontrar
    raise HTTPException(status_code=404, detail="Product not found")