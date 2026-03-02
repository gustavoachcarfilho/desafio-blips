# Lead Management API - Desafio Blips 🚀

API assíncrona para gerenciamento de Leads, desenvolvida com foco em alta performance, escalabilidade e separação de responsabilidades. O projeto utiliza **FastAPI** e **MongoDB**, totalmente containerizado com **Docker**.

## 1. 🏗 Arquitetura do Projeto (Padrão Spring-like)
Inspirado na organização do ecossistema Java/Spring, o projeto utiliza uma estrutura modular para facilitar a manutenção e testes:

- **Controllers (`app/api/v1/`)**: Utiliza `APIRouter` para gerenciar as rotas e injeção de dependências, equivalente aos `@RestController` do Spring.
- **Repositories (`app/repositories/`)**: Camada de abstração para o MongoDB (Motor), isolando a lógica de persistência.
- **Services (`app/services/`)**: Centraliza integrações externas, como o consumo da API DummyJSON.
- **Models/DTOs (`app/models/`)**: Uso intensivo de Pydantic V2 para validação rigorosa de dados e contratos de entrada/saída.
- **Core (`app/core/`)**: Configurações globais e singleton da conexão com o banco de dados.



## 2. 🛠 Stack Tecnológica
- **Linguagem:** Python 3.11
- **Framework:** FastAPI (Assíncrono)
- **Banco de Dados:** MongoDB (NoSQL)
- **Driver DB:** Motor (Async driver)
- **Validação:** Pydantic V2
- **Infraestrutura:** Docker & Docker Compose

## 3. 🚀 Como Executar

### Pré-requisitos
- Docker e Docker Compose instalados na máquina.

### Passo a Passo
1. Clone o repositório.
2. Na raiz do projeto, execute o comando para construir e subir os serviços:
   ```bash
   docker-compose up --build -d
   
3. A API estará disponível em: http://localhost:8000

4. 📖 Documentação e Testes (Swagger)
O FastAPI gera automaticamente a especificação OpenAPI. Para testar os endpoints:
👉 Acesse: http://localhost:8000/docs

Endpoints:
POST /leads/: Cria um lead e integra dados de nascimento de API externa.

GET /leads/: Lista todos os leads persistidos.

GET /leads/{id}: Busca detalhada por ID (UUID/ObjectId).

5. 🐳 Detalhes do Docker
Networking: Os containers se comunicam via rede interna do Docker; a API localiza o banco através do hostname mongodb.

Persistência: Utiliza volumes Docker para garantir que os dados do MongoDB não sejam perdidos ao reiniciar os containers.

6. 📝 Notas de Desenvolvimento
O tratamento de erros (HTTP 404, 422, 500) foi implementado seguindo padrões RESTful.

A conversão de ObjectId do MongoDB para strings JSON foi tratada via Annotated e BeforeValidator no Pydantic V2 para evitar erros de serialização.

Desenvolvido por Gustavo Achcar Filho
Engenheiro de Software & Estudante de Sistemas de Informação
