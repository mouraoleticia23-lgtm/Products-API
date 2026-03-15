# Products API

API REST simples desenvolvida em Python utilizando FastAPI para gerenciamento de produtos.

O projeto implementa um CRUD completo com persistência de dados em JSON, validação automática e documentação interativa via Swagger.

---

## Estrutura do Projeto

```
Process-API/
├── src/
│   ├── main.py          # Ponto de entrada da aplicação FastAPI
│   ├── models/
│   │   └── product.py   # Modelo Pydantic para Produto
│   └── routers/
│       └── endpoints.py  # Endpoints para gerenciamento de produtos
├── data/
│   └── data.json        # Dados persistidos em JSON
├── tests/
│   └── test_products.py # Testes unitários para os endpoints
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo
```

---

## Funcionalidades

* Listar todos os produtos
* Buscar produto por ID
* Filtrar produtos por categoria
* Criar novos produtos (com validação de ID único)
* Atualizar produtos existentes (ID imutável)
* Deletar produtos
* Validação automática de dados com Pydantic
* Documentação automática da API via Swagger
* Testes automatizados

---

## Endpoints da API

| Método | Endpoint              | Descrição                          |
|--------|-----------------------|------------------------------------|
| GET    | `/products`          | Lista todos os produtos           |
| GET    | `/products?category=X` | Filtra por categoria             |
| GET    | `/products/{id}`     | Busca produto por ID              |
| POST   | `/products`          | Cria novo produto                 |
| PUT    | `/products/{id}`     | Atualiza produto existente        |
| DELETE | `/products/{id}`     | Deleta produto                    |
| GET    | `/`                  | Página inicial                    |

---

## Tecnologias Utilizadas

* **Python 3.14** - Linguagem principal
* **FastAPI** - Framework web para APIs
* **Pydantic** - Validação de dados
* **Uvicorn** - Servidor ASGI
* **JSON** - Persistência de dados
* **Pytest** - Testes automatizados
* **HTTPX** - Cliente HTTP para testes

---

## Melhorias Implementadas

- **Estrutura modular**: Código organizado em `src/`, separando lógica de dados/testes
- **Performance**: Uso de dicionário para buscas O(1)
- **Validações robustas**: IDs únicos, imutabilidade de IDs, tratamento de erros
- **Testabilidade**: Testes unitários cobrindo todos os endpoints
- **Documentação**: README detalhado e docs automáticas
- **Compatibilidade**: Código atualizado para Pydantic V2

---

## Melhorias Futuras

Aqui estão algumas ideias para evoluir o projeto:

- **Banco de Dados**: Migrar de JSON para SQLite/PostgreSQL para melhor performance
- **Autenticação**: Implementar JWT/OAuth2 para proteger endpoints
- **Logs**: Sistema de logging estruturado para monitoramento
- **Containerização**: Dockerfile e docker-compose para facilitar deploy
- **CI/CD**: Pipeline de integração contínua com GitHub Actions
- **Testes de Integração**: Testes end-to-end com banco real
- **Webhooks**: Notificações para eventos (produto criado/atualizado)
- **Upload de Imagens**: Suporte a imagens de produtos
- **Internacionalização**: Suporte a múltiplos idiomas

---

## Como Executar

### Passos

1. **Clone o projeto** e navegue até a pasta:
   ```bash
   cd Process-API
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação**:
   ```bash
   uvicorn src.main:app --reload
   ```

4. **Acesse a aplicação**:
   - API: http://127.0.0.1:8000
   - Documentação Swagger: http://127.0.0.1:8000/docs

---

## Como Testar

Execute os testes automatizados com:
```bash
pytest tests/
```

Ou para modo verboso:
```bash
pytest tests/ -v
```

---

## Exemplos de Uso

### Criar um produto
```bash
POST /products
{
  "id": 5,
  "name": "Mouse Gamer",
  "category": "electronics",
  "price": 150.0,
  "stock": 20
}
```

### Listar produtos por categoria
```bash
GET /products?category=electronics
```
