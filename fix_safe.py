with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace(
    '<button class="btn" onclick="conectarAoJogo()">Procurar Oponente</button>',
    '<button class="btn" id="btn-jogar" onclick="conectarAoJogo()">Procurar Oponente</button>'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK")