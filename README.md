# API Connect

API REST simples para gerenciamento de usuários, desenvolvida como parte da disciplina de **Desenvolvimento Back-End**.

O objetivo do projeto é permitir o cadastro, consulta, atualização e remoção de usuários utilizando requisições HTTP e respostas no formato JSON.

## Tecnologias utilizadas

- Python
- Flask
- Git
- GitHub
- Postman

## Estrutura do projeto

    api-connect/
    │
    ├── app.py
    ├── requirements.txt
    ├── .gitignore
    │
    ├── routes/
    │   └── user_routes.py
    │
    ├── controllers/
    │   └── user_controller.py
    │
    └── data/
        └── users.py

## Como executar

Clone o repositório:

    git clone URL_DO_REPOSITORIO

Entre na pasta:

    cd api-connect

Crie o ambiente virtual:

    python -m venv venv

No Windows, ative o ambiente:

    venv\Scripts\activate

Instale as dependências:

    pip install -r requirements.txt

Execute a aplicação:

    python app.py

A API ficará disponível em:

    http://127.0.0.1:5000

## Endpoints

| Método | Endpoint | Função | Status |
|---|---|---|---|
| GET | `/users` | Lista todos os usuários | 200 |
| GET | `/users/<id>` | Busca um usuário pelo ID | 200 |
| POST | `/users` | Cadastra um novo usuário | 201 |
| PUT | `/users/<id>` | Atualiza um usuário | 200 |
| DELETE | `/users/<id>` | Remove um usuário | 204 |

## Exemplo de cadastro

**Requisição**

    POST /users

**JSON enviado**

    {
      "name": "João Santos",
      "email": "joao@email.com"
    }

**Resposta**

    {
      "data": {
        "id": 3,
        "name": "João Santos",
        "email": "joao@email.com"
      }
    }

Status: **201 Created**

## Exemplo de erro de validação

Caso o nome ou e-mail não seja enviado:

    {
      "error": "Nome e e-mail são obrigatórios"
    }

Status: **400 Bad Request**

## Exemplo de usuário não encontrado

Ao buscar um ID que não existe:

    {
      "error": "Usuario não encontrado"
    }

Status: **404 Not Found**

## Persistência dos dados

Os usuários são armazenados em uma lista na memória enquanto a aplicação está rodando.

Como este projeto é um MVP simples, não foi utilizado um banco de dados. Quando o servidor é encerrado, os novos usuários cadastrados durante a execução são perdidos.

## .gitignore

O projeto utiliza um arquivo `.gitignore` para evitar o envio de arquivos locais e temporários para o GitHub.

Conteúdo utilizado:

    venv/
    __pycache__/
    *.pyc
    .vscode/
    .idea/
