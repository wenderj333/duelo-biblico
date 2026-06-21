with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'rb') as f:
    content = f.read()

# Adicionar secao mobile com info PIX e ranking abaixo do lobby
mobile_info = b"""
    <!-- INFO MOBILE (so aparece no telemovel) -->
    <div id="mobile-info" style="display:none; margin-top:14px;">
        <div style="background:linear-gradient(135deg,#1a0a3e,#3d1a7a);border-radius:14px;padding:14px;text-align:center;border:1px solid rgba(246,216,96,0.3);margin-bottom:10px;">
            <div style="font-size:11px;color:rgba(255,255,255,0.6);font-weight:700;letter-spacing:1px;">PREMIO PIX DA SEMANA</div>
            <div id="pix-valor-mobile" style="font-size:26px;font-weight:900;color:#f6d860;">R$ 10,00</div>
            <div style="font-size:11px;color:rgba(255,255,255,0.5);">Lider no domingo ganha!</div>
        </div>
        <div style="background:rgba(255,255,255,0.05);border-radius:14px;padding:14px;border:1px solid rgba(255,255,255,0.1);">
            <div style="font-size:12px;font-weight:800;color:#f6d860;margin-bottom:10px;">&#x1F3C6; MURAL DA GLORIA</div>
            <div id="top3-mobile" style="font-size:12px;color:rgba(255,255,255,0.8);">Carregando...</div>
        </div>
    </div>
"""

# Inserir antes do fecho do lobby
content = content.replace(
    b'    <!-- RESULTADO -->',
    mobile_info + b'    <!-- RESULTADO -->'
)

# CSS para mostrar no mobile
css_mobile_info = b"""
        @media (max-width: 720px) {
            #mobile-info { display: block !important; }
        }
"""
content = content.replace(
    b'        @media (max-width: 720px) {',
    css_mobile_info + b'        @media (max-width: 720px) {'
)

# JS para carregar dados no mobile
js_mobile = b"""
// Mobile info
function atualizarMobileInfo(){
    if(window.innerWidth > 720) return;
    fetch(BACKEND_URL+"/api/duelo/ranking").then(r=>r.json()).then(d=>{
        if(d.pix) document.getElementById("pix-valor-mobile").textContent="R$ "+d.pix;
        const top=d.ranking||[];
        const el=document.getElementById("top3-mobile");
        if(!el) return;
        if(top.length===0){el.textContent="Nenhuma partida ainda. Seja o primeiro!";return;}
        el.innerHTML=top.slice(0,3).map((j,i)=>
            '<div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid rgba(255,255,255,0.08)">'+
            '<span>'+(i===0?"&#x1F947; ":i===1?"&#x1F948; ":"&#x1F949; ")+j.nome+'</span>'+
            '<span style="color:#f6d860;font-weight:700">'+j.pontos+' pts</span></div>'
        ).join("");
    }).catch(()=>{});
}
atualizarMobileInfo();
"""
content = content.replace(b'atualizarJogadoresOnline();\n// ===== RANKING =====', js_mobile + b'atualizarJogadoresOnline();\n// ===== RANKING =====')

with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'wb') as f:
    f.write(content)
print('Info mobile adicionada!')
