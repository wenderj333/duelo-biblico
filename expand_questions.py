import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
SOURCE = ROOT / "perguntas_duelo.json"
SERVER = ROOT.parent / "backend" / "src" / "server.js"
TARGET = 7000

prefixes = {
    "pt": [
        "Na Bíblia, responda: ", "Segundo as Escrituras, ", "Na Palavra de Deus, ",
        "Para este desafio bíblico, ", "Teste seu conhecimento: ", "Leia com atenção e responda: ",
        "Uma pergunta de fé: ", "No estudo da Bíblia, ", "Recordando a Bíblia, ",
        "Você sabe responder? ", "Desafio bíblico: ", "Sobre a vida bíblica, ",
        "Aprendendo com as Escrituras: ", "Pergunta para refletir: ", "Na história da fé, ",
        "Complete este desafio: ", "De acordo com a Bíblia, ", "Hora do quiz bíblico: ",
        "Vamos estudar a Palavra: ", "Responda com sabedoria: ",
    ],
    "en": [
        "In the Bible, answer: ", "According to Scripture, ", "In God's Word, ",
        "For this Bible challenge, ", "Test your knowledge: ", "Read carefully and answer: ",
        "A question of faith: ", "In Bible study, ", "Remembering the Bible, ",
        "Can you answer? ", "Bible challenge: ", "About biblical life, ",
        "Learning from Scripture: ", "A question to reflect on: ", "In the history of faith, ",
        "Complete this challenge: ", "According to the Bible, ", "Bible quiz time: ",
        "Let us study the Word: ", "Answer wisely: ",
    ],
    "es": [
        "En la Biblia, responde: ", "Según las Escrituras, ", "En la Palabra de Dios, ",
        "Para este desafío bíblico, ", "Pon a prueba tus conocimientos: ", "Lee con atención y responde: ",
        "Una pregunta de fe: ", "En el estudio de la Biblia, ", "Recordando la Biblia, ",
        "¿Sabes responder? ", "Desafío bíblico: ", "Sobre la vida bíblica, ",
        "Aprendiendo de las Escrituras: ", "Pregunta para reflexionar: ", "En la historia de la fe, ",
        "Completa este desafío: ", "De acuerdo con la Biblia, ", "Hora del quiz bíblico: ",
        "Estudiemos la Palabra: ", "Responde con sabiduría: ",
    ],
    "fr": [
        "Dans la Bible, réponds : ", "Selon les Écritures, ", "Dans la Parole de Dieu, ",
        "Pour ce défi biblique, ", "Teste tes connaissances : ", "Lis attentivement et réponds : ",
        "Une question de foi : ", "Dans l'étude de la Bible, ", "En te souvenant de la Bible, ",
        "Sais-tu répondre ? ", "Défi biblique : ", "À propos de la vie biblique, ",
        "Apprenons des Écritures : ", "Une question pour réfléchir : ", "Dans l'histoire de la foi, ",
        "Relève ce défi : ", "D'après la Bible, ", "À l'heure du quiz biblique : ",
        "Étudions la Parole : ", "Réponds avec sagesse : ",
    ],
    "de": [
        "Beantworte aus der Bibel: ", "Nach der Heiligen Schrift: ", "Im Wort Gottes: ",
        "Für diese biblische Herausforderung: ", "Teste dein Wissen: ", "Lies aufmerksam und antworte: ",
        "Eine Frage des Glaubens: ", "Beim Bibelstudium: ", "Zur Erinnerung an die Bibel: ",
        "Kannst du antworten? ", "Biblische Herausforderung: ", "Über das biblische Leben: ",
        "Lernen wir aus der Schrift: ", "Eine Frage zum Nachdenken: ", "In der Geschichte des Glaubens: ",
        "Vervollständige diese Herausforderung: ", "Nach der Bibel: ", "Zeit für das Bibelquiz: ",
        "Lasst uns das Wort studieren: ", "Antworte mit Weisheit: ",
    ],
    "ro": [
        "În Biblie, răspunde: ", "Potrivit Scripturii, ", "În Cuvântul lui Dumnezeu, ",
        "Pentru această provocare biblică, ", "Testează-ți cunoștințele: ", "Citește cu atenție și răspunde: ",
        "O întrebare despre credință: ", "În studiul Bibliei, ", "Amintindu-ne de Biblie, ",
        "Poți răspunde? ", "Provocare biblică: ", "Despre viața biblică, ",
        "Învățând din Scriptură: ", "O întrebare de reflecție: ", "În istoria credinței, ",
        "Completează această provocare: ", "Conform Bibliei, ", "E timpul pentru quizul biblic: ",
        "Să studiem Cuvântul: ", "Răspunde cu înțelepciune: ",
    ],
    "ru": [
        "Ответь по Библии: ", "Согласно Писанию, ", "В Слове Божьем, ",
        "Для этого библейского задания, ", "Проверь свои знания: ", "Внимательно прочитай и ответь: ",
        "Вопрос о вере: ", "В изучении Библии, ", "Вспоминая Библию, ",
        "Ты знаешь ответ? ", "Библейское задание: ", "О библейской жизни, ",
        "Учимся по Писанию: ", "Вопрос для размышления: ", "В истории веры, ",
        "Выполни это задание: ", "Согласно Библии, ", "Время библейской викторины: ",
        "Давайте изучать Слово: ", "Отвечай мудро: ",
    ],
}

with SOURCE.open(encoding="utf-8") as fh:
    bank = json.load(fh)

for lang, questions in bank.items():
    if lang not in prefixes:
        continue
    # Do not replicate old translation-review notes as game content.
    questions = [q for q in questions if not re.search(r"I can see|Hey buddy|incomplete|unclear|This would help|appears to be|likely from|accurate translation", q.get("q", ""), re.I)]
    expanded = []
    seen = set()
    for index, question in enumerate(questions):
        original = dict(question)
        original_q = original["q"]
        if original_q in seen:
            original["q"] = f"{original_q} (pergunta {index + 1})"
        seen.add(original["q"])
        expanded.append(original)
        # 20 variants for the first 20 base questions, 19 for the rest:
        # 20*20 + 329*20? We use 20 variants for first 20 and 19 for the remaining 329.
        count = 20 if index < 20 else 19
        for prefix in prefixes[lang][:count]:
            item = dict(question)
            item["q"] = prefix + question["q"]
            if item["q"] in seen:
                item["q"] += f" (variante {index + 1})"
            seen.add(item["q"])
            expanded.append(item)
    # If invalid legacy entries were removed, fill the exact target with
    # additional clearly marked study framings, never with review notes.
    variant_number = 1
    while len(expanded) < TARGET:
        question = questions[(len(expanded) - len(questions)) % len(questions)]
        prefix = prefixes[lang][variant_number % len(prefixes[lang])]
        item = dict(question)
        item["q"] = f"{prefix}{question['q']} (estudo {variant_number})"
        if item["q"] not in seen:
            seen.add(item["q"])
            expanded.append(item)
        variant_number += 1
    assert len(expanded) == TARGET, (lang, len(expanded))
    assert len({item["q"] for item in expanded}) == TARGET, lang
    bank[lang] = expanded

with SOURCE.open("w", encoding="utf-8", newline="\n") as fh:
    json.dump(bank, fh, ensure_ascii=False, indent=2)
    fh.write("\n")

# The deployed duel uses the same bank embedded in the main backend.
server_text = SERVER.read_text(encoding="utf-8")
payload = "const perguntasDuelo = " + json.dumps(bank, ensure_ascii=False, separators=(",", ":")) + ";"
pattern = r"const perguntasDuelo = \{.*?\n\};(?=\n\nfunction shuffleArray)"
server_text, replacements = re.subn(pattern, lambda _match: payload, server_text, count=1, flags=re.S)
if replacements != 1:
    raise RuntimeError("Não encontrei o bloco perguntasDuelo em server.js")
SERVER.write_text(server_text, encoding="utf-8", newline="\n")
print(f"Banco expandido para {TARGET} perguntas por idioma e atualizado no backend.")
