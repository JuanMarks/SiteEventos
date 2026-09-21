# SiteEventos · Ninna Hub

Plataforma web de **gestão de eventos**. Empresas e administradores cadastram eventos (públicos ou privados), usuários se inscrevem, e após o evento recebem por e-mail um formulário de satisfação. O painel administrativo consolida inscrições e avaliações em gráficos, e há disparo de e-mail em massa (individual, por grupo ou via planilha Excel) e geração de relatórios em PDF.

## Stack

| Camada | Tecnologia |
|---|---|
| Backend | Django 4.1 · Django REST Framework |
| Banco | PostgreSQL |
| Frontend | Django Templates + Tailwind CSS (CDN) + Alpine.js |
| Gráficos | Chart.js |
| PDF / Excel | xhtml2pdf · pyexcel |
| Infra | Docker + docker-compose |

## Funcionalidades

- Autenticação por e-mail e senha, com recuperação de senha por link.
- Grupos de acesso: **Usuários Comuns**, **Empresa**, **ADM** e **Mantenedores**.
- Cadastro, edição e publicação de eventos, com upload de imagem.
- Inscrição/remoção de inscrição em eventos abertos.
- Formulário de satisfação (nota + opinião) e cálculo de nota média.
- **Painel administrativo** com KPIs e gráficos (publicação, inscritos por evento, distribuição de notas, usuários por grupo, top avaliados).
- Envio de e-mail em massa e relatórios de inscritos em PDF.

## Como rodar

### Opção 1 — Docker (recomendado)

Pré-requisito: Docker + Docker Compose.

```bash
cd Gestao_Novo
cp .env.example .env      # ajuste os valores (ver seção Variáveis de ambiente)
docker compose up --build
```

Acesse **http://localhost:8000**. O banco sobe em container (host na porta `5433` para não conflitar com um PostgreSQL local na `5432`).

Para popular dados de demonstração (somente com `DEBUG=True`):

```bash
docker compose exec web python manage.py seed_demo
```

Credenciais criadas pelo seed (login é por **e-mail**):

| Papel | E-mail | Senha |
|---|---|---|
| Admin | `admin@ninna.local` | `admin123` |
| Comum | `user1@ninna.local` … `user5@ninna.local` | `user123` |

Parar sem perder dados: `docker compose stop` (retomar com `docker compose start`).

### Opção 2 — Local (venv)

Pré-requisitos: Python 3.10 e um PostgreSQL rodando com um banco `site_eventos`.

```bash
cd Gestao_Novo
python -m venv ninna && ninna\Scripts\activate     # Windows
pip install -r requirements.txt
cp .env.example .env      # ajuste os valores
python manage.py migrate
python manage.py runserver
```

## Variáveis de ambiente

Definidas no arquivo `Gestao_Novo/.env` (nunca versionado — veja `.env.example`):

| Variável | Descrição |
|---|---|
| `SECRET_KEY` | Chave secreta do Django |
| `DEBUG` | `True` em desenvolvimento, `False` em produção |
| `ALLOWED_HOSTS` | Hosts permitidos, separados por vírgula |
| `SITE_URL` | URL base usada em links de e-mail |
| `DB_NAME` / `DB_USER` / `DB_PASSWORD` / `DB_HOST` / `DB_PORT` | Conexão com o PostgreSQL |
| `EMAIL_HOST` / `EMAIL_PORT` / `EMAIL_HOST_USER` / `EMAIL_HOST_PASSWORD` / `DEFAULT_FROM_EMAIL` | Envio de e-mail (SMTP) |
| `ADMIN_REGISTRATION_CODE` | Código exigido para se cadastrar como ADM (vazio bloqueia auto-cadastro de ADM) |

## Estrutura

```
Gestao_Novo/
├─ core/                 # settings, urls, wsgi/asgi
├─ apps/
│  ├─ cadastrar_eventos/ # eventos, inscrições, satisfação, PDF, API REST
│  ├─ usuarios/          # cadastro/login/dashboard + painel admin
│  ├─ enviar/            # e-mail em massa, recuperação de senha
│  ├─ arquivo_excel/     # upload de planilha
│  └─ abstrair/          # helpers (parse Excel, montagem de e-mail)
├─ templates/            # base.html (shell com sidebar), base_auth.html, telas
├─ Dockerfile · docker-compose.yml · requirements.txt
```

Para um mapa detalhado do projeto, veja [`CLAUDE.md`](CLAUDE.md).
