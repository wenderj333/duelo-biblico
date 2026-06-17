with open(r"C:\Users\wender\Desktop\duelo-biblico\index.html", "r", encoding="utf-8") as f:
    c = f.read()

listener = """
// Receber dados do Sigo com Fe via postMessage
window.addEventListener('message', (event) => {
    if (event.origin !== 'https://sigo-com-fe.vercel.app') return;
    if (event.data.type === 'LOGIN_DATA') {
        const u = event.data.user;
        if (u.nome) {
            document.getElementById('nomeUsuario').value = u.nome;
            atualizarAvatar();
        }
        if (u.foto) {
            fotoBase64 = u.foto;
            const preview = document.getElementById('avatar-preview');
            preview.innerHTML = '';
            const img = document.createElement('img');
            img.src = u.foto;
            img.style = 'width:100%;height:100%;object-fit:cover;';
            preview.appendChild(img);
        }
        if (u.token) localStorage.setItem('sigo_token', u.token);
    }
});
"""

old = "carregarRanking();\nsetInterval(carregarRanking,30000);"
new = listener + "\ncarregarRanking();\nsetInterval(carregarRanking,30000);"

if old in c:
    c = c.replace(old, new)
    print("OK: listener adicionado")
else:
    print("ERRO: texto nao encontrado")

with open(r"C:\Users\wender\Desktop\duelo-biblico\index.html", "w", encoding="utf-8") as f:
    f.write(c)