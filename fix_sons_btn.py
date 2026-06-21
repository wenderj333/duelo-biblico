with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# Adicionar variavel de som activado
old = "// Sons"
new = """// Sons
let somActivado = false;"""
c = c.replace(old, new)

# Modificar tocarSom para verificar se está activado
old2 = "function tocarSom(som){ try{ som.currentTime=0; som.volume=0.5; som.play().catch(()=>{}); }catch(e){} }"
new2 = """function tocarSom(som){ if(!somActivado) return; try{ som.currentTime=0; som.volume=0.5; som.play().catch(()=>{}); }catch(e){} }
function activarSom(){ somActivado=true; document.getElementById("btn-som").style.display="none"; tocarSom(somAcerto); }"""
c = c.replace(old2, new2)

# Adicionar botao de activar som antes do botao de jogar
old3 = '<button class="btn" id="btn-jogar" onclick="conectarAoJogo()">Procurar Oponente</button>'
new3 = '''<button id="btn-som" onclick="activarSom()" style="width:100%;padding:10px;margin-top:10px;margin-bottom:6px;border-radius:10px;border:none;background:rgba(255,255,255,0.1);color:white;cursor:pointer;font-size:13px;display:flex;align-items:center;justify-content:center;gap:8px;">🔊 Activar Som</button>
        <button class="btn" id="btn-jogar" onclick="conectarAoJogo()">Procurar Oponente</button>'''
c = c.replace(old3, new3)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK")