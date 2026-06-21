with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# Adicionar sons no inicio do script
old = "const BACKEND_URL = \"https://sigo-com-fe-api.onrender.com\";"
new = """const BACKEND_URL = "https://sigo-com-fe-api.onrender.com";

// Sons
const somAcerto = new Audio("https://assets.mixkit.co/active_storage/sfx/2018/2018-preview.mp3");
const somErro = new Audio("https://assets.mixkit.co/active_storage/sfx/2955/2955-preview.mp3");
const somVitoria = new Audio("https://assets.mixkit.co/active_storage/sfx/2013/2013-preview.mp3");
const somDerrota = new Audio("https://assets.mixkit.co/active_storage/sfx/2955/2955-preview.mp3");
function tocarSom(som){ try{ som.currentTime=0; som.volume=0.5; som.play().catch(()=>{}); }catch(e){} }"""

if old in c:
    c = c.replace(old, new)
    print("OK: sons adicionados")
else:
    print("ERRO: texto nao encontrado")

# Tocar som ao acertar
old2 = "btn.classList.add(\"correta\");"
new2 = "btn.classList.add(\"correta\"); tocarSom(somAcerto);"
c = c.replace(old2, new2)

# Tocar som ao errar
old3 = "btn.classList.add(\"errada\");"
new3 = "btn.classList.add(\"errada\"); tocarSom(somErro);"
c = c.replace(old3, new3)

# Tocar som de vitoria/derrota no fim
old4 = "jogadores.sort((a,b)=>b.pontos-a.pontos);"
new4 = """jogadores.sort((a,b)=>b.pontos-a.pontos);
        const euVenci = jogadores[0].nome === window.meuNomeGlobal;
        tocarSom(euVenci ? somVitoria : somDerrota);"""
c = c.replace(old4, new4)

print("OK: sons de acerto erro e fim adicionados")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)