with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Adicionar fundo ao body
old = "background:url('https://res.cloudinary.com/degxiuf43/image/upload/v1781572333/duelo-biblico/jmzrst3lnzru9jrt2bzx.jpg') center center / cover no-repeat fixed;"
new_bg = "background:url('https://res.cloudinary.com/degxiuf43/image/upload/v1781603430/duelo-biblico/qvbrhcoqnithannhxjga.jpg') center center / cover no-repeat fixed;"

if old in content:
    content = content.replace(old, new_bg)
    print('Substituido URL antigo')
else:
    # Adicionar ao body
    content = content.replace(
        'body{font-family:',
        "body{background:url('https://res.cloudinary.com/degxiuf43/image/upload/v1781603430/duelo-biblico/qvbrhcoqnithannhxjga.jpg') center center / cover no-repeat fixed;font-family:"
    )
    print('Fundo adicionado ao body')

with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'r', encoding='utf-8') as f:
    c = f.read()
print('OK: ' + ('fundo OK' if 'qvbrhcoqnithannhxjga' in c else 'FALHOU'))