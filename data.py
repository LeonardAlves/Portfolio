PROJECTS = [
    {
        "slug": "pokedex",
        "title": "Pokédex Full Stack",
        "summary": "App full stack com CRUD, busca, filtros e paginação.",
        "description": "Frontend em React, API REST em Node/Express, MongoDB com Mongoose, "
                       "Docker Compose e importação de dados da PokeAPI via n8n.",
        "tags": ["React", "Node.js", "MongoDB", "Docker", "n8n"],
        "repo": "https://github.com/seu-usuario/pokedex",
        "demo": None,
    },
    # adicione os outros projetos aqui
]

def get_project(slug: str):
    return next((p for p in PROJECTS if p["slug"] == slug), None)