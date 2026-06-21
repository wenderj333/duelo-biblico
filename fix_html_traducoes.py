with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# Substituir textos hardcoded por IDs para traduzir via JS
fixes = [
    ('Escolhe o teu idioma:</p>', 'Escolhe o teu idioma:</p>'),
    ('<p style="color:rgba(255,255,255,0.55);font-size:12px;text-align:center;margin-bottom:10px;">Escolhe o teu idioma:</p>',
     '<p id="txt-escolhe" style="color:rgba(255,255,255,0.55);font-size:12px;text-align:center;margin-bottom:10px;">Escolhe o teu idioma:</p>'),
    ('<p style="font-size:11px;color:rgba(255,255,255,0.45);text-align:center;margin-bottom:8px;">Convida um amigo:</p>',
     '<p id="txt-convidar" style="font-size:11px;color:rgba(255,255,255,0.45);text-align:center;margin-bottom:8px;">Convida um amigo:</p>'),
]

for old, new in fixes:
    if old in c:
        c = c.replace(old, new)
        print(f"OK: {old[:30]}...")
    else:
        print(f"SKIP: {old[:30]}...")

# Adicionar traducao dos elementos no aplicarTraducao
old_func = "function aplicarTraducao(idioma){\n    const t=UI_TEXTOS[idioma]||UI_TEXTOS.pt;\n    const n=document.getElementById(\"nomeUsuario\"); if(n)n.placeholder=t.nome||\"O teu nome...\";\n    const b=document.getElementById(\"btn-jogar\"); if(b)b.textContent=t.jogar||\"Procurar Oponente\";\n}"
new_func = """function aplicarTraducao(idioma){
    const t=UI_TEXTOS[idioma]||UI_TEXTOS.pt;
    const n=document.getElementById("nomeUsuario"); if(n)n.placeholder=t.nome||"O teu nome...";
    const b=document.getElementById("btn-jogar"); if(b)b.textContent=t.jogar||"Procurar Oponente";
    const e=document.getElementById("txt-escolhe"); if(e)e.textContent=t.escolhe||"Escolhe o teu idioma:";
    const cv=document.getElementById("txt-convidar"); if(cv)cv.textContent=t.convidar||"Convida um amigo:";
    const oc=document.getElementById("online-count");
    if(oc){const n2=oc.textContent.split(" ")[0];oc.textContent=n2+" "+(t.online||"jogadores online");}
}"""

if old_func in c:
    c = c.replace(old_func, new_func)
    print("OK: aplicarTraducao actualizado")
else:
    print("ERRO: aplicarTraducao nao encontrado")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)