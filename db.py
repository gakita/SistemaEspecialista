

jogos = [
    {
        "nome": "Assassins Creed 2",
        "caracteristicas": {
            "ação": 8,
            "aventura": 9,
            "historia": 10,
            "mundo aberto": 7,
            "graficos": 5,
            "trilha sonora": 5,
            "jogabilidade": 6
        }
    },
    {
        "nome": "Fifa 2014",
        "caracteristicas": {
            "futebol": 10,
            "graficos": 6,
            "trilha sonora": 8,
            "jogabilidade": 6,
            "multiplayer": 7,
            "simulação": 8,
            "realistico": 7
        }
    },
    {
        "nome": "Minecraft",
        "caracteristicas": {
            "graficos": 9,
            "trilha sonora": 10,
            "jogabilidade": 10,
            "multiplayer": 8,
            "sobrevivencia": 10,
            "sandbox": 10,
            "mundo aberto": 10,
            "combate": 6,
        }
    },
    {
        "nome": "The Witcher 3: Wild Hunt",
        "caracteristicas": {
            "ação": 9,
            "aventura": 10,
            "historia": 10,
            "mundo aberto": 10,
            "graficos": 9,
            "trilha sonora": 10,
            "jogabilidade": 9
        }
    },
    {
        "nome": "Call of Duty: Modern Warfare",
        "caracteristicas": {
            "ação": 9,
            "shooter": 10,
            "multiplayer": 9,
            "graficos": 8,
            "trilha sonora": 7,
            "jogabilidade": 8,
            "combate": 9,
        }
    },
    {
        "nome": "Portal 2",
        "caracteristicas": {
            "puzzle": 10,
            "história": 9,
            "multiplayer": 8,
            "graficos": 7,
            "trilha sonora": 8,
            "jogabilidade": 9,
            "originalidade": 10,
        }
    },
    {
        "nome": "The Legend of Zelda: Breath of the Wild",
        "caracteristicas": {
            "aventura": 10,
            "mundo aberto": 10,
            "história": 8,
            "graficos": 9,
            "trilha sonora": 9,
            "jogabilidade": 10,
            "exploração": 10,
        }
    },
    {
        "nome": "Dark Souls III",
        "caracteristicas": {
            "ação": 9,
            "aventura": 8,
            "dificuldade": 10,
            "mundo aberto": 8,
            "graficos": 8,
            "trilha sonora": 7,
            "jogabilidade": 7
        }
    },
    {
        "nome": "Overwatch",
        "caracteristicas": {
            "ação": 9,
            "shooter": 9,
            "multiplayer": 10,
            "graficos": 8,
            "trilha sonora": 7,
            "jogabilidade": 8,
            "teamwork": 9,
        }
    },
    {
        "nome": "Stardew Valley",
        "caracteristicas": {
            "simulação": 10,
            "sobrevivencia": 9,
            "mundo aberto": 7,
            "graficos": 6,
            "trilha sonora": 8,
            "jogabilidade": 9,
            "farming": 10,
        }
    },
    {
        "nome": "Red Dead Redemption 2",
        "caracteristicas": {
            "ação": 8,
            "aventura": 10,
            "historia": 10,
            "mundo aberto": 10,
            "graficos": 10,
            "trilha sonora": 9,
            "jogabilidade": 8
        }
    },
    {
        "nome": "Super Mario Odyssey",
        "caracteristicas": {
            "aventura": 9,
            "platformer": 10,
            "história": 7,
            "graficos": 8,
            "trilha sonora": 8,
            "jogabilidade": 10,
            "exploração": 9,
        }
    },
    {
        "nome": "Final Fantasy XV",
        "caracteristicas": {
            "ação": 8,
            "aventura": 9,
            "história": 8,
            "mundo aberto": 9,
            "graficos": 9,
            "trilha sonora": 9,
            "jogabilidade": 8
        }
    },
    {
        "nome": "Doom Eternal",
        "caracteristicas": {
            "ação": 10,
            "shooter": 10,
            "graficos": 9,
            "trilha sonora": 10,
            "jogabilidade": 9,
            "intensidade": 10,
            "combate": 10,
        }
    },
    {
        "nome": "Animal Crossing: New Horizons",
        "caracteristicas": {
            "simulação": 10,
            "relaxante": 10,
            "graficos": 8,
            "trilha sonora": 7,
            "jogabilidade": 8,
            "multiplayer": 6,
            "originalidade": 9,
        }
    }
]

for i in jogos:
  i["OCORRENCIAS"]=0
  i["PERCENTUAL"]=0

todas_opcoes = []

for jogo in jogos:
    for opcao in jogo["caracteristicas"]:
        if opcao not in todas_opcoes:
            todas_opcoes.append(opcao)