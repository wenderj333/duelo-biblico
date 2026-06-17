with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

fixes = [
    ("ðŸ†", "🏆"),
    ("ðŸ''", "👑"),
    ("ðŸ"", "🔐"),
    ("ðŸ"¥", "🔥"),
    ("ðŸ"–", "📖"),
    ("ðŸ"²", "📲"),
    ("ðŸŽ®", "🎮"),
    ("â⬇ï¸", "⬇️"),
    ("â†'", "→"),
    ("Â·", "·"),
]

for bad, good in fixes:
    c = c.replace(bad, good)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK: emojis corrigidos")