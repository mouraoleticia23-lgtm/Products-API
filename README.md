# Products API

API REST simples desenvolvida em Python utilizando FastAPI para gerenciamento de produtos.

O projeto implementa um CRUD com persistência de dados em JSON e documentação automática via Swagger.

---

# Funcionalidades

* Listar produtos
* Buscar produto por ID
* Filtrar produtos por categoria
* Criar novos produtos
* Atualizar produtos existentes
* Deletar produtos
* Validação automática de dados
* Documentação automática da API

---

# Tecnologias utilizadas

* Python
* FastAPI
* Pydantic
* Uvicorn
* JSON

---

# Estrutura do projeto

```
simple-data-api
│
├── main.py
├── requirements.txt
│
├── models
│   └── product.py
│
├── routers
│   └── products.py
│
└── data
    └── data.json
```

**Descrição das pastas**

* **models** → definição dos modelos de dados
* **routers** → definição dos endpoints da API
* **data** → armazenamento dos dados em JSON

---

# Endpoints da API

| Método | Endpoint       | Descrição                |
| ------ | -------------- | ------------------------ |
| GET    | /              | Verificar status da API  |
| GET    | /products      | Listar todos os produtos |
| GET    | /products/{id} | Buscar produto por ID    |
| POST   | /products      | Criar novo produto       |
| PUT    | /products/{id} | Atualizar produto        |
| DELETE | /products/{id} | Remover produto          |

---

# Como executar o projeto

Clone o repositório:

```
git clone https://github.com/seu-usuario/simple-data-api.git
```

Entre na pasta do projeto:

```
cd simple-data-api
```

Instale as dependências:

```
pip install -r requirements.txt
```

Execute a aplicação:

```
uvicorn main:app --reload
```

A API estará disponível em:

```
http://127.0.0.1:8000
```

---

# Documentação interativa

Acesse:

```
http://127.0.0.1:8000/docs
```

---
