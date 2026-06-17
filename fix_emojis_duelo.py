with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

fixes = [
    ("ðŸ†", chr(0x1F3C6)),
    ("ðŸ''", chr(0x1F451)),
    ("ðŸ"", chr(0x1F510)),
    ("ðŸ"¥", chr(0x1F525)),
    ("ðŸ"–", chr(0x1F4D6)),
    ("ðŸ"²", chr(0x1F4F2)),
    ("ðŸŽ®", chr(0x1F3AE)),
    ("â†'", chr(0x2192)),
    ("Â·", chr(0xB7)),
]

for bad, good in fixes:
    c = c.replace(bad, good)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK: emojis corrigidos")