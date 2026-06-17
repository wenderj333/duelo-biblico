with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

old = "    </div>\r\n\r\n    <div id=\"pix-side\" class=\"pix-side\">"
new = "    </div>\r\n    <a href=\"https://sigo-com-fe.vercel.app/mural\" target=\"_blank\" style=\"display:flex;align-items:center;gap:8px;padding:10px 12px;border-radius:10px;background:linear-gradient(135deg,#6c47d4,#4a2270);color:white;text-decoration:none;font-size:12px;font-weight:700;margin-bottom:14px;justify-content:center;\">&#8592; Voltar ao Mural</a>\r\n\r\n    <div id=\"pix-side\" class=\"pix-side\">"

if old in c:
    c = c.replace(old, new)
    print("OK: botao adicionado")
else:
    print("ERRO: texto nao encontrado")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)