with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'rb') as f:
    content = f.read()

antigo = b'UI_TEXTOS = {\r\n    pt:{procurando:"Aguardando um irmao para o duelo...",oponente:"Oponente"},\r\n    en:{procurando:"Waiting for an opponent...",oponente:"Opponent"},\r\n    es:{procurando:"Esperando un oponente...",oponente:"Oponente"},\r\n    fr:{procurando:"En attente d un adversaire...",oponente:"Adversaire"},\r\n    de:{procurando:"Warte auf einen Gegner...",oponente:"Gegner"},\r\n    it:{procurando:"Aspettando un avversario...",oponente:"Avversario"},\r\n    ro:{procurando:"Asteptand un adversar...",oponente:"Adversar"}\r\n};'

novo = b'UI_TEXTOS = {\r\n    pt:{procurando:"Aguardando um irmao para o duelo...",oponente:"Oponente",desafiar:"Desafiar",desafioEnviado:"Desafio enviado!",desafioRec:"te desafia!",aceitar:"Aceitar",recusar:"Recusar",jogadoresOnline:"Jogadores Online"},\r\n    en:{procurando:"Waiting for an opponent...",oponente:"Opponent",desafiar:"Challenge",desafioEnviado:"Challenge sent!",desafioRec:"challenges you!",aceitar:"Accept",recusar:"Decline",jogadoresOnline:"Online Players"},\r\n    es:{procurando:"Esperando un oponente...",oponente:"Oponente",desafiar:"Desafiar",desafioEnviado:"Desafio enviado!",desafioRec:"te desafia!",aceitar:"Aceptar",recusar:"Rechazar",jogadoresOnline:"Jugadores en Linea"},\r\n    fr:{procurando:"En attente d un adversaire...",oponente:"Adversaire",desafiar:"Defier",desafioEnviado:"Defi envoye!",desafioRec:"vous defie!",aceitar:"Accepter",recusar:"Refuser",jogadoresOnline:"Joueurs en Ligne"},\r\n    de:{procurando:"Warte auf einen Gegner...",oponente:"Gegner",desafiar:"Herausfordern",desafioEnviado:"Herausforderung gesendet!",desafioRec:"fordert dich heraus!",aceitar:"Annehmen",recusar:"Ablehnen",jogadoresOnline:"Spieler Online"},\r\n    it:{procurando:"Aspettando un avversario...",oponente:"Avversario",desafiar:"Sfidare",desafioEnviado:"Sfida inviata!",desafioRec:"ti sfida!",aceitar:"Accetta",recusar:"Rifiuta",jogadoresOnline:"Giocatori Online"},\r\n    ro:{procurando:"Asteptand un adversar...",oponente:"Adversar",desafiar:"Provoaca",desafioEnviado:"Provocare trimisa!",desafioRec:"te provoaca!",aceitar:"Accepta",recusar:"Refuza",jogadoresOnline:"Jucatori Online"}\r\n};\r\nfunction t(chave){ return (UI_TEXTOS[idiomaAtual]||UI_TEXTOS.pt)[chave]||chave; }'

if antigo in content:
    content = content.replace(antigo, novo)
    print('Substituido!')
else:
    print('ERRO')

with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'wb') as f:
    f.write(content)
