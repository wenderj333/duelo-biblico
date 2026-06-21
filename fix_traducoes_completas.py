with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

old = 'UI_TEXTOS = {'
new = '''UI_TEXTOS = {
    pt:{
        procurando:"Aguardando um irmao para o duelo...",
        oponente:"Oponente",jogar:"Procurar Oponente",nome:"O teu nome...",
        convidar:"Convida um amigo:",online:"jogadores online",
        pix:"Para concorrer ao Premio PIX entra na",
        escolhe:"Escolhe o teu idioma:",copiar:"Copiar",copiado:"Copiado!"
    },
    en:{
        procurando:"Waiting for an opponent...",
        oponente:"Opponent",jogar:"Find Opponent",nome:"Your name...",
        convidar:"Invite a friend:",online:"players online",
        pix:"To compete for the PIX Prize join",
        escolhe:"Choose your language:",copiar:"Copy",copiado:"Copied!"
    },
    es:{
        procurando:"Esperando un oponente...",
        oponente:"Oponente",jogar:"Buscar Oponente",nome:"Tu nombre...",
        convidar:"Invita a un amigo:",online:"jugadores online",
        pix:"Para competir por el Premio PIX entra en",
        escolhe:"Elige tu idioma:",copiar:"Copiar",copiado:"Copiado!"
    },
    fr:{
        procurando:"En attente d un adversaire...",
        oponente:"Adversaire",jogar:"Trouver Adversaire",nome:"Ton nom...",
        convidar:"Invite un ami:",online:"joueurs en ligne",
        pix:"Pour concourir au Prix PIX rejoins",
        escolhe:"Choisis ta langue:",copiar:"Copier",copiado:"Copie!"
    },
    de:{
        procurando:"Warte auf einen Gegner...",
        oponente:"Gegner",jogar:"Gegner suchen",nome:"Dein Name...",
        convidar:"Lade einen Freund ein:",online:"Spieler online",
        pix:"Um den PIX-Preis zu gewinnen tritt bei",
        escolhe:"Waehle deine Sprache:",copiar:"Kopieren",copiado:"Kopiert!"
    },
    it:{
        procurando:"Aspettando un avversario...",
        oponente:"Avversario",jogar:"Cerca Avversario",nome:"Il tuo nome...",
        convidar:"Invita un amico:",online:"giocatori online",
        pix:"Per partecipare al Premio PIX unisciti a",
        escolhe:"Scegli la tua lingua:",copiar:"Copia",copiado:"Copiato!"
    },
    ro:{
        procurando:"Asteptand un adversar...",
        oponente:"Adversar",jogar:"Cauta Adversar",nome:"Numele tau...",
        convidar:"Invita un prieten:",online:"jucatori online",
        pix:"Pentru a concura la Premiul PIX intra pe",
        escolhe:"Alege limba ta:",copiar:"Copiaza",copiado:"Copiat!"
    }
};
const OLD_UI_TEXTOS = {'''

if old in c:
    c = c.replace(old, new)
    print("OK")
else:
    print("ERRO")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)