with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'rb') as f:
    content = f.read()

css_mobile = b"""
        @media (max-width: 720px) {
            .sidebar { display: none; }
            .main { padding: 8px !important; }
            .card { padding: 16px 12px !important; }
            #perguntaTexto { font-size: 15px !important; min-height: auto !important; margin-bottom: 12px !important; }
            .alt-btn { font-size: 13px !important; padding: 10px 12px !important; margin: 5px 0 !important; }
            .timer-normal, .timer-urgente { font-size: 28px !important; }
            #lobby { padding: 16px 12px !important; }
            .lang-btn { padding: 5px 10px !important; font-size: 12px !important; }
        }
"""

# Substituir o media query existente
content = content.replace(
    b'        @media (max-width: 720px) {\r\n            .sidebar { display: none; }\r\n            .main { padding: 10px; }\r\n        }',
    css_mobile
)

with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'wb') as f:
    f.write(content)
print('CSS mobile melhorado!')
