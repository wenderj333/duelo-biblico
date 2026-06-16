with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = "body { font-family: Arial, sans-serif; background: linear-gradient(135deg,#1a0533,#2d1065); color: white; min-height: 100vh; display: flex; align-items: center; justify-content: center; }"
new = "body { font-family: Arial, sans-serif; background: url('https://res.cloudinary.com/degxiuf43/image/upload/v1781572333/duelo-biblico/jmzrst3lnzru9jrt2bzx.jpg') center center / cover no-repeat fixed; color: white; min-height: 100vh; display: flex; align-items: center; justify-content: center; }"

content = content.replace(old, new)

with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK: ' + ('background url' if 'cloudinary' in content else 'FALHOU'))
