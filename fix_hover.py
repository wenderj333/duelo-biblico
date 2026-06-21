with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'rb') as f:
    content = f.read()

# Remover hover do mobile e adicionar active em vez disso
content = content.replace(
    b'        .alt-btn:hover:not([disabled]) { background: rgba(240,192,64,0.14); border-color: #f0c040; transform: translateX(4px); }',
    b'        .alt-btn:hover:not([disabled]) { background: rgba(240,192,64,0.14); border-color: #f0c040; transform: translateX(4px); }\r\n        @media (hover: none) { .alt-btn:hover:not([disabled]) { background: rgba(255,255,255,0.07); border-color: rgba(255,255,255,0.13); transform: none; } }\r\n        .alt-btn:active:not([disabled]) { background: rgba(240,192,64,0.14); border-color: #f0c040; }'
)

with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'wb') as f:
    f.write(content)
print('CSS hover mobile corrigido!')
