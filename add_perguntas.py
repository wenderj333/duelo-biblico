import json

# Ler perguntas convertidas
with open(r'C:\Users\wender\Desktop\duelo-biblico\perguntas_duelo.json', 'r', encoding='utf-8') as f:
    duelo = json.load(f)

# Ler server.js
with open(r'C:\Users\wender\Desktop\SIGO COM FE\SIGO COM FE LOCAL\sigo-com-fe\backend\src\server.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Substituir as 10 perguntas pelas 269
perguntas_js = "const perguntasDuelo = " + json.dumps(duelo, ensure_ascii=False) + ";"

# Encontrar e substituir
import re
content = re.sub(
    r'const perguntasDuelo = \{.*?\};',
    perguntas_js,
    content,
    flags=re.DOTALL
)

with open(r'C:\Users\wender\Desktop\SIGO COM FE\SIGO COM FE LOCAL\sigo-com-fe\backend\src\server.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK: 269 perguntas adicionadas ao backend!')
