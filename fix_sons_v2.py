with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# Substituir sons por Web Audio API
old = """// Sons
let somActivado = false;
const somAcerto = new Audio("https://assets.mixkit.co/active_storage/sfx/2018/2018-preview.mp3");
const somErro = new Audio("https://assets.mixkit.co/active_storage/sfx/2955/2955-preview.mp3");
const somVitoria = new Audio("https://assets.mixkit.co/active_storage/sfx/2013/2013-preview.mp3");
const somDerrota = new Audio("https://assets.mixkit.co/active_storage/sfx/2955/2955-preview.mp3");
function tocarSom(som){ if(!somActivado) return; try{ som.currentTime=0; som.volume=0.5; som.play().catch(()=>{}); }catch(e){} }
function activarSom(){ somActivado=true; document.getElementById("btn-som").style.display="none"; tocarSom(somAcerto); }"""

new = """// Sons Web Audio API
let audioCtx = null;
let somActivado = false;

function getCtx(){ if(!audioCtx) audioCtx = new (window.AudioContext||window.webkitAudioContext)(); return audioCtx; }

function tocarSom(tipo){
    if(!somActivado) return;
    try{
        const ctx = getCtx();
        const o = ctx.createOscillator();
        const g = ctx.createGain();
        o.connect(g); g.connect(ctx.destination);
        if(tipo==="acerto"){ o.frequency.value=880; o.type="sine"; g.gain.setValueAtTime(0.3,ctx.currentTime); g.gain.exponentialRampToValueAtTime(0.001,ctx.currentTime+0.3); o.start(); o.stop(ctx.currentTime+0.3); }
        else if(tipo==="erro"){ o.frequency.value=220; o.type="sawtooth"; g.gain.setValueAtTime(0.3,ctx.currentTime); g.gain.exponentialRampToValueAtTime(0.001,ctx.currentTime+0.4); o.start(); o.stop(ctx.currentTime+0.4); }
        else if(tipo==="vitoria"){ [523,659,784,1047].forEach((f,i)=>{ const o2=ctx.createOscillator(); const g2=ctx.createGain(); o2.connect(g2); g2.connect(ctx.destination); o2.frequency.value=f; o2.type="sine"; g2.gain.setValueAtTime(0.3,ctx.currentTime+i*0.15); g2.gain.exponentialRampToValueAtTime(0.001,ctx.currentTime+i*0.15+0.2); o2.start(ctx.currentTime+i*0.15); o2.stop(ctx.currentTime+i*0.15+0.2); }); }
        else if(tipo==="derrota"){ [330,220,165].forEach((f,i)=>{ const o2=ctx.createOscillator(); const g2=ctx.createGain(); o2.connect(g2); g2.connect(ctx.destination); o2.frequency.value=f; o2.type="sawtooth"; g2.gain.setValueAtTime(0.3,ctx.currentTime+i*0.2); g2.gain.exponentialRampToValueAtTime(0.001,ctx.currentTime+i*0.2+0.3); o2.start(ctx.currentTime+i*0.2); o2.stop(ctx.currentTime+i*0.2+0.3); }); }
    }catch(e){}
}
function activarSom(){ somActivado=true; getCtx(); document.getElementById("btn-som").style.display="none"; tocarSom("acerto"); }"""

if old in c:
    c = c.replace(old, new)
    print("OK: sons Web Audio API")
else:
    print("ERRO")

# Corrigir chamadas aos sons
c = c.replace("tocarSom(somAcerto);", 'tocarSom("acerto");')
c = c.replace("tocarSom(somErro);", 'tocarSom("erro");')
c = c.replace("tocarSom(euVenci ? somVitoria : somDerrota);", 'tocarSom(euVenci ? "vitoria" : "derrota");')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("Concluido!")