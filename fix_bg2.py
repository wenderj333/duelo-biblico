with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'https://res.cloudinary.com/degxiuf43/image/upload/v1781572333/duelo-biblico/jmzrst3lnzru9jrt2bzx.jpg',
    'https://res.cloudinary.com/degxiuf43/image/upload/v1781603430/duelo-biblico/qvbrhcoqnithannhxjga.jpg'
)

with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK: ' + ('novo fundo' if 'qvbrhcoqnithannhxjga' in content else 'FALHOU'))