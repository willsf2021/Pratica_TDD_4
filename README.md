# 📋 Agenda de Contatos - Django TDD

> Projeto desenvolvido para a disciplina **Desenvolvimento Web 3** com foco em Test-Driven Development (TDD)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![Coverage](https://img.shields.io/badge/Coverage->90%25-brightgreen.svg)](https://coverage.readthedocs.io/)

## 📝 Sobre o Projeto

Sistema de agenda de contatos desenvolvido seguindo metodologia TDD (Test-Driven Development), com autenticação restrita para usuários com e-mail institucional `@fatec.sp.gov.br`.

### ✨ Funcionalidades

#### Sprint 1 ✅
- 🔐 Sistema de Login/Logout
- 🎓 Autenticação restrita para e-mails institucionais (@fatec.sp.gov.br)
- 🏠 Página inicial protegida

#### Sprint 2 ✅
- ➕ Cadastrar contatos
- 📋 Listar contatos
- ✏️ Atualizar contatos
- 🗑️ Remover contatos
- 🔒 Proteção de rotas (apenas usuários autenticados)
- 🧪 Cobertura de testes acima de 90%

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **Django 4.x**
- **SQLite** (banco de dados)
- **Coverage.py** (análise de cobertura de testes)
- **Bootstrap** (frontend)

## 📦 Instalação

### Linux
```bash
git clone https://github.com/orlandosaraivajr/Pratica_TDD_4.git
cd Pratica_TDD_4/
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd agenda/
python manage.py migrate
python manage.py test
coverage run --source='.' manage.py test 
coverage html
python manage.py createsuperuser
python manage.py runserver
```

### Windows
```bash
git clone https://github.com/orlandosaraivajr/Pratica_TDD_4.git
cd Pratica_TDD_4/
virtualenv venv
cd venv\Scripts
activate.bat
cd ..\..
pip install -r requirements.txt
cd agenda/
python manage.py migrate
python manage.py test
coverage run --source='.' manage.py test 
coverage html
python manage.py createsuperuser
python manage.py runserver
```

## 🔑 Credenciais de Acesso

Ao criar o superusuário, utilize:

- **Username:** admin
- **E-mail:** seu.email@fatec.sp.gov.br
- **Password:** fatec

## 🧪 Testes

### Executar testes
```bash
python manage.py test
```

### Gerar relatório de cobertura
```bash
coverage run --source='.' manage.py test
coverage html
```

O relatório HTML estará disponível em `htmlcov/index.html`

## 📊 Estrutura do Projeto
```
Pratica_TDD_4/
│
├── agenda/
│   ├── core/              # App principal
│   │   ├── models.py      # Modelo Agenda
│   │   ├── views.py       # Views do CRUD
│   │   ├── forms.py       # Formulários
│   │   ├── tests.py       # Testes unitários
│   │   └── urls.py        # Rotas
│   │
│   ├── agenda/            # Configurações do projeto
│   └── manage.py
│
├── requirements.txt
└── README.md
```

## 🗃️ Modelo de Dados

### Agenda
- **nome_complet** (CharField): Nome do contato
- **email** (EmailField): E-mail do contato
- **telefone** (CharField): Telefone do contato
- **observações** (CharField): Observações do contato

## 🔒 Segurança

- ✅ Todas as rotas do CRUD são protegidas por `@login_required`
- ✅ Autenticação apenas com e-mail institucional
- ✅ Validação de domínio no momento do cadastro
- ✅ Proteção contra CSRF habilitada

## 📈 Cobertura de Testes

O projeto mantém cobertura de testes **acima de 90%**, incluindo:

- ✅ Testes de autenticação
- ✅ Testes de CRUD completo
- ✅ Testes de validação de formulários
- ✅ Testes de proteção de rotas
- ✅ Testes de modelos

## 🎯 Rotas Principais

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página inicial (protegida) |
| `/login/` | GET, POST | Login de usuários |
| `/logout/` | GET | Logout de usuários |
| `/contatos/` | GET | Listar contatos |
| `/contatos/novo/` | GET, POST | Cadastrar contato |
| `/contatos/<id>/editar/` | GET, POST | Editar contato |
| `/contatos/<id>/deletar/` | POST | Deletar contato |

## 👨‍💻 Desenvolvimento

### Boas Práticas Aplicadas

- 🧪 **TDD**: Testes escritos antes da implementação
- 📝 **Clean Code**: Código limpo e legível
- 🔄 **DRY**: Don't Repeat Yourself
- 🎯 **SOLID**: Princípios de design orientado a objetos
- 📚 **Documentação**: Código bem documentado

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais na disciplina **Desenvolvimento Web 3** da FATEC.

## 👤 Autor

**Seu Nome**
- E-mail institucional: seu.email@fatec.sp.gov.br
- GitHub: [@seu-usuario](https://github.com/seu-usuario)

## 🙏 Agradecimentos

- Prof. Orlando Saraiva Jr. - Criador do repositório base
- FATEC - Faculdade de Tecnologia de São Paulo
- Colegas da disciplina Desenvolvimento Web 3

---

⭐ Desenvolvido com Django e TDD | FATEC 2025