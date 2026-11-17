# Portfólio · Leonardo Alves

Meu site pessoal de portfólio, onde reúno os projetos que construo enquanto estudo desenvolvimento full stack. O site é renderizado no servidor, com poucas dependências e quase nenhum JavaScript.

## Funcionalidades

- Página inicial com apresentação e lista de projetos
- Filtro por tecnologia sem recarregar a página (HTMX)
- Página de detalhe de cada projeto: descrição, tecnologias, funcionalidades, arquitetura, aprendizados e próximos passos
- Carrossel de capturas de tela, com ampliação ao clicar (lightbox) e navegação por teclado
- Layout responsivo e tema escuro
- Projetos cadastrados em um único arquivo Python, sem banco de dados

## Stack

| Camada | Tecnologia |
|---|---|
| Backend | Python 3.12 + FastAPI |
| Templates | Jinja2 |
| Estilo | Tailwind CSS v4 (CLI standalone) |
| Interatividade | HTMX |
| Infra | Docker |

## Estrutura do projeto

```
portfolio/
├── main.py                  # rotas da aplicação
├── data.py                  # lista de projetos (PROJECTS)
├── requirements.txt
├── Dockerfile
├── static/
│   ├── src/input.css        # entrada do Tailwind
│   ├── css/output.css       # CSS gerado
│   └── img/                 # capturas de tela dos projetos
└── templates/
    ├── base.html            # layout base
    ├── home.html
    ├── project_detail.html
    └── partials/
        └── project_list.html   # trecho de HTML usado pelo HTMX
```

## Como funciona

- `GET /` renderiza a home com todos os projetos e as tags disponíveis.
- `GET /projects?tag=React` devolve **apenas o trecho HTML** da lista filtrada. O HTMX troca esse trecho na página, sem recarregar.
- `GET /projects/{slug}` renderiza a página de detalhe do projeto.

## Rodando localmente

Pré-requisitos: Python 3.12 e Git.

```bash
git clone https://github.com/LeonardAlves/Portfolio.git
cd Portfolio
python -m venv .venv
```

Ative o ambiente virtual:

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate
```

Instale as dependências e suba o servidor:

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Acesse http://localhost:8000.

### Tailwind (só se for alterar o visual)

O `output.css` já vem gerado no repositório. Para alterar classes nos templates, baixe o [binário standalone do Tailwind](https://github.com/tailwindlabs/tailwindcss/releases) para a raiz do projeto e rode:

```bash
# modo de desenvolvimento (recompila ao salvar)
./tailwindcss -i static/src/input.css -o static/css/output.css --watch

# build final minificado
./tailwindcss -i static/src/input.css -o static/css/output.css --minify
```

No Windows, use `.\tailwindcss.exe` no lugar de `./tailwindcss`.

## Rodando com Docker

```bash
docker build -t portfolio .
docker run -p 8000:8000 portfolio
```

## Adicionando um novo projeto

Basta incluir um item na lista `PROJECTS` do `data.py` e salvar as imagens em `static/img/`:

```python
{
    "slug": "nome-do-projeto",
    "title": "Nome do Projeto",
    "summary": "Frase curta que aparece no card da home.",
    "description": "Texto de introdução da página do projeto.",
    "tags": ["Python", "FastAPI"],
    "repo": "https://github.com/LeonardAlves/nome-do-repo",
    "demo": None,
    "highlights": ["Funcionalidade 1", "Funcionalidade 2"],
    "architecture": [("Backend", "FastAPI"), ("Frontend", "HTMX")],
    "learned": "O que aprendi com o projeto.",
    "next_steps": ["Próximo passo"],
    "images": ["/static/img/nome-1.webp"],
}
```

O card na home, os botões de filtro por tag e a página de detalhe são gerados automaticamente. Campos vazios (como `demo` ou `images`) simplesmente não aparecem na página.

## Deploy

O projeto tem um `Dockerfile` e roda em qualquer plataforma que aceite containers (Render, Railway, Fly.io ou um VPS). Antes de publicar, gere o CSS minificado e faça commit do `static/css/output.css`.

## Próximos passos

- [ ] Seção "Sobre mim" e download do currículo
- [ ] Formulário de contato com HTMX
- [ ] SEO: meta tags por página, Open Graph e `sitemap.xml`
- [ ] Testes com `pytest` e `TestClient`
- [ ] CI/CD com GitHub Actions

## Autor

**Leonardo Alves**

- GitHub: [@LeonardAlves](https://github.com/LeonardAlves)
- LinkedIn: [In.LeonardoAlves](https://www.linkedin.com/in/leonardo-santos-alves/)
