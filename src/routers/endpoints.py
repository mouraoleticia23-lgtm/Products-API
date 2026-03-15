# Este arquivo define os endpoints para gerenciamento de produtos usando FastAPI.
# Importa o modelo de produto, manipula os dados e define os endpoints para criar, ler, atualizar e deletar produtos.


# Importa a biblioteca FastAPI para criar endpoints e HTTPException para retornar erros HTTP
from fastapi import APIRouter, HTTPException
# Importa a biblioteca json
import json
# Importa o modelo de produto definido em models/product.py
from src.models.product import Product


# Cria um roteador para os endpoints de produtos
router = APIRouter()

# Carrega dados iniciais (para demo; em produção, use um banco de dados)
try:
    with open("data/data.json") as f:
        products = json.load(f)
except FileNotFoundError:
    products = []

# Para eficiência, converte para dict com ID como chave (O(1) para buscas)
products_dict = {p["id"]: p for p in products}

def save_products():
    # Converte preços para int antes de salvar (consistência)
    products_list = list(products_dict.values())
    for p in products_list:
        p['price'] = int(p['price'])
    # Salva de volta no formato lista para manter compatibilidade com JSON
    with open("data/data.json", "w") as f:
        json.dump(products_list, f, indent=4)

# Endpoint para obter a lista de produtos, com opção de filtrar por categoria
@router.get("/products")
def get_products(category: str = None):
    all_products = list(products_dict.values())
    if category:
        filtered = [p for p in all_products if p["category"] == category]
        return filtered
    return all_products

# Endpoint para obter um produto específico pelo seu ID
@router.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id not in products_dict:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_dict[product_id]

# Endpoint para criar um novo produto
@router.post("/products")
def add_product(product: Product):
    new_product = product.model_dump()
    if new_product["id"] in products_dict:
        raise HTTPException(status_code=400, detail="Product ID already exists")
    products_dict[new_product["id"]] = new_product
    save_products()
    return {
        "message": "Product added",
        "product": new_product
    }

# Endpoint para atualizar um produto existente pelo seu ID
@router.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    if product_id not in products_dict:
        raise HTTPException(status_code=404, detail="Product not found")
    updated_data = updated_product.model_dump()
    # Garante que o ID não mude (imutável)
    updated_data["id"] = product_id
    products_dict[product_id] = updated_data
    save_products()
    return {"message": "Product updated"}

# Endpoint para deletar um produto pelo seu ID
@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id not in products_dict:
        raise HTTPException(status_code=404, detail="Product not found")
    del products_dict[product_id]
    save_products()
    return {"message": "Product deleted"}