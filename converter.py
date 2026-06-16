import json

# Ler perguntas originais
with open(r'C:\Users\wender\Desktop\SIGO COM FE\SIGO COM FE LOCAL\sigo-com-fe\frontend\src\data\perguntas.json', 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

# Converter para formato do duelo
duelo = { 'pt': [], 'en': [], 'es': [], 'fr': [], 'de': [], 'ro': [], 'ru': [] }

for p in perguntas:
    # PT
    if p.get('q') and p.get('opts'):
        duelo['pt'].append({'q': p['q'], 'a': p['opts'], 'c': p.get('r', 0)})
    # EN
    if p.get('en_q') and p.get('en_opts'):
        duelo['en'].append({'q': p['en_q'], 'a': p['en_opts'], 'c': p.get('r', 0)})
    # ES
    if p.get('es_q') and p.get('es_opts'):
        duelo['es'].append({'q': p['es_q'], 'a': p['es_opts'], 'c': p.get('r', 0)})
    # FR
    if p.get('fr_q') and p.get('fr_opts'):
        duelo['fr'].append({'q': p['fr_q'], 'a': p['fr_opts'], 'c': p.get('r', 0)})
    # DE
    if p.get('de_q') and p.get('de_opts'):
        duelo['de'].append({'q': p['de_q'], 'a': p['de_opts'], 'c': p.get('r', 0)})
    # RO
    if p.get('ro_q') and p.get('ro_opts'):
        duelo['ro'].append({'q': p['ro_q'], 'a': p['ro_opts'], 'c': p.get('r', 0)})
    # RU
    if p.get('ru_q') and p.get('ru_opts'):
        duelo['ru'].append({'q': p['ru_q'], 'a': p['ru_opts'], 'c': p.get('r', 0)})

# Guardar
with open(r'C:\Users\wender\Desktop\duelo-biblico\perguntas_duelo.json', 'w', encoding='utf-8') as f:
    json.dump(duelo, f, ensure_ascii=False, indent=2)

for lang, qs in duelo.items():
    print(f'{lang}: {len(qs)} perguntas')
