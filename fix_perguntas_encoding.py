import json

with open("perguntas_duelo.json", "r", encoding="utf-8") as f:
    raw = f.read()

# Corrigir double encoding
fixed = raw.encode("latin-1").decode("utf-8")

# Validar JSON
data = json.loads(fixed)
print(f"pt: {len(data.get('pt',[]))} perguntas")
print(f"es: {data['es'][0]['q']}")
print(f"fr: {data['fr'][0]['q']}")

with open("perguntas_duelo_fixed.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("OK")