with open(r"C:\Users\wender\Desktop\duelo-biblico\index.html", "r", encoding="utf-8") as f:
    c = f.read()

old = "acordarServidor();\ncarregarPerfilSigo();"
new = """const urlParams = new URLSearchParams(window.location.search);
const langParam = urlParams.get('lang');
if (langParam) {
    const btn = document.querySelector('.idioma-btn[onclick*="' + langParam + '"]');
    if (btn) {
        document.querySelectorAll('.idioma-btn').forEach(b => b.classList.remove('ativo'));
        btn.classList.add('ativo');
        selecionarIdioma(langParam, btn);
    }
}
acordarServidor();
carregarPerfilSigo();"""

if old in c:
    c = c.replace(old, new)
    print("OK")
else:
    print("ERRO")

with open(r"C:\Users\wender\Desktop\duelo-biblico\index.html", "w", encoding="utf-8") as f:
    f.write(c)