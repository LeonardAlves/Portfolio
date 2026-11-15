PROJECTS = [
    {
        "slug": "pokedex",
        "title": "Pokédex Full Stack",
        "summary": "App full stack com CRUD, busca, filtros e paginação.",
        "description": "Frontend em React, API REST em Node/Express, MongoDB com Mongoose, "
                       "Docker Compose e importação de dados da PokeAPI via n8n.",
        "tags": ["React", "Node.js", "MongoDB", "Docker", "n8n"],
        "repo": "https://github.com/LeonardAlves/Pokedex",
        "demo": None,
        "highlights": [
            "Cards de Pokémon com favoritos",
            "CRUD completo, pesquisa, filtros e paginação",
            "Importação automática de dados da PokeAPI via workflow no n8n",
            "Ambiente inteiro sobe com um comando (Docker Compose)",
        ],
        "architecture": [
            ("Frontend", "React"),
            ("API", "Node.js + Express"),
            ("Banco", "MongoDB + Mongoose"),
            ("Importação", "n8n + PokeAPI"),
            ("Infra", "Docker Compose"),
        ],
        "learned": "Conectar frontend, API, banco e importação, e entender como cada peça comunica com as outras.",
        "next_steps": ["Autenticação de usuários", "Testes automatizados"],
        "images": [
            "/static/img/pokedex-1.png",
            "/static/img/pokedex-2.png",
            "/static/img/pokedex-3.png",
            "/static/img/pokedex-4.png",
        
        ],
    },
]


def get_project(slug: str):
    return next((p for p in PROJECTS if p["slug"] == slug), None)