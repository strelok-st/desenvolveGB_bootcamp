# declarando a lista de tuplas
dados_guardados = [
    ("Varinha Élfica da Aurora", 8, 120.50),
    ("Varinha de Carvalho do Sussurro Antigo", 5, 150.00),
    ("Varinha de Salgueiro da Lua Crescente", 10, 95.00),
    ("Grimório das Sombras Cintilantes", 3, 320.00),
    ("Livro dos Encantos Esquecidos", 7, 180.00),
    ("Tomo da Sabedoria Estelar", 2, 450.00),
    ("Cristal Ametista da Serenidade", 15, 65.00),
    ("Quartzo Rosa do Amor Eterno", 12, 58.00),
    ("Obsidiana Negra da Proteção", 9, 72.00),
    ("Pó de Fada Lumina", 25, 35.00),
    ("Baralho Brilhante da Intuição", 6, 90.00),
    ("Oráculo dos Sonhos Revelados", 4, 110.00),
    ("Caldeirão da Bruxaria Ancestral", 3, 280.00),
    ("Vela da Chama Violeta da Transmutação", 20, 22.00),
    ("Vela Dourada da Prosperidade", 18, 25.00),
    ("Incenso da Floresta Encantada", 30, 15.00),
    ("Amuleto do Dragão Guardião", 7, 75.00),
    ("Poção do Elixir da Vida", 10, 45.00),
    ("Poção da Sorte Líquida", 14, 38.00),
    ("Bola de Cristal da Visão Pura", 2, 500.00),
    ("Capa da Invisibilidade Noturna", 5, 210.00),
    ("Ervas da Sabedoria Antiga", 40, 18.00),
    ("Pena da Fênix Renascida", 1, 800.00),
    ("Chave Mestra dos Segredos", 8, 55.00),
    ("Boneco Vodu da Harmonia", 6, 130.00)
]

dic = {};

# criando o dicionário, com um loop que itera sobre os itens da lista, acessando os índices das tuplas e preenchendo o dicionário.
for item in dados_guardados:
	dic.update({item[0]:item[1]*item[2]})

print(dic)

# implementando o algoritmo de busca do maior valor com bucket
itens_valiosos = []
for item, valor in dic:
	dic.()
	


