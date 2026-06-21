with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'rb') as f:
    content = f.read()

# Melhorar auto-deteção - também verificar localStorage
content = content.replace(
    b'window._autoLang = lang;',
    b'window._autoLang = lang;\n        localStorage.setItem("duelo_lang", lang);'
)

content = content.replace(
    b'let socket,salaAtual="",idiomaAtual=window._autoLang||"pt"',
    b'let socket,salaAtual="",idiomaAtual=localStorage.getItem("duelo_lang")||window._autoLang||"pt"'
)

with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'wb') as f:
    f.write(content)
print('Feito!')
