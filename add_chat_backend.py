with open(r'C:\Users\wender\Desktop\SIGO COM FE\SIGO COM FE LOCAL\sigo-com-fe\backend\src\server.js', 'r', encoding='utf-8') as f:
    content = f.read()

chat_socket = """
  socket.on('chatMsg', (d) => {
    const { salaId, msg, nome } = d;
    if (duelSalas[salaId]) {
      ioduelo.to(salaId).emit('chatMsg', { nome, msg });
    }
  });

"""
content = content.replace("  socket.on('desafiarJogador'", chat_socket + "  socket.on('desafiarJogador'")

with open(r'C:\Users\wender\Desktop\SIGO COM FE\SIGO COM FE LOCAL\sigo-com-fe\backend\src\server.js', 'w', encoding='utf-8') as f:
    f.write(content)
print('Chat backend adicionado!')
