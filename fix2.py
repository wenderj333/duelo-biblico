with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
content = re.sub(r'[\U00010000-\U0010ffff]', '', content)
content = content.replace('BÃ¡blico', 'Biblico')
content = content.replace('FÃ©', 'Fe')
content = content.replace('Ã¡', 'a')
content = content.replace('Ã©', 'e')

with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('OK: ' + str(len(content)) + ' chars')
