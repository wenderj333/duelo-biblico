with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'rb') as f:
    content = f.read()

# Remover classe ativo do PT por defeito e adicionar via JS
content = content.replace(
    b'<button class="idioma-btn ativo" onclick="selecionarIdioma(\'pt\',this)">PT</button>',
    b'<button class="idioma-btn" onclick="selecionarIdioma(\'pt\',this)" id="btn-pt">PT</button>'
)

# Adicionar script de auto-selecao logo após os botoes de idioma
js_auto = b"""
<script>
// Auto-selecionar idioma do browser
(function(){
    const bl = (navigator.language||navigator.userLanguage||'pt').substring(0,2).toLowerCase();
    const suportados = ['pt','en','es','fr','de','it','ro'];
    const lang = suportados.includes(bl) ? bl : 'pt';
    const btn = document.querySelector('.idioma-btn[onclick*="\''+lang+'\'"]');
    if(btn){ 
        document.querySelectorAll('.idioma-btn').forEach(b=>b.classList.remove('ativo'));
        btn.classList.add('ativo');
        window._autoLang = lang;
    } else {
        document.getElementById('btn-pt').classList.add('ativo');
    }
})();
</script>
"""
content = content.replace(
    b'<script>\nconst BACKEND_URL',
    js_auto + b'<script>\nconst BACKEND_URL'
)

# Usar _autoLang na inicializacao
content = content.replace(
    b'const browserLang=(navigator.language||"pt").substring(0,2).toLowerCase();const idiomasSuportados=["pt","en","es","fr","de","it","ro"];let socket,salaAtual="",idiomaAtual=idiomasSuportados.includes(browserLang)?browserLang:"pt"',
    b'let socket,salaAtual="",idiomaAtual=window._autoLang||"pt"'
)

with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'wb') as f:
    f.write(content)
print('Auto-idioma corrigido!')
