with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'rb') as f:
    content = f.read()

content = content.replace(
    b'let socket, salaAtual="", idiomaAtual="pt", meuspontos=0, perguntaAtualNum=0;',
    b'const browserLang=(navigator.language||"pt").substring(0,2).toLowerCase();const idiomasSuportados=["pt","en","es","fr","de","it","ro"];let socket,salaAtual="",idiomaAtual=idiomasSuportados.includes(browserLang)?browserLang:"pt",meuspontos=0,perguntaAtualNum=0;'
)

with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'wb') as f:
    f.write(content)
print('Feito!')
