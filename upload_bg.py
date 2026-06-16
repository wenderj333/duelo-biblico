import base64, urllib.request, json

# Ler a imagem
with open(r'C:\Users\wender\Desktop\duelo-biblico\bg.jpeg', 'rb') as f:
    img_data = base64.b64encode(f.read()).decode()

# Upload para Cloudinary
import urllib.parse
data = urllib.parse.urlencode({
    'file': 'data:image/jpeg;base64,' + img_data,
    'upload_preset': 'sigo_com_fe',
    'folder': 'duelo-biblico'
}).encode()

req = urllib.request.Request(
    'https://api.cloudinary.com/v1_1/degxiuf43/image/upload',
    data=data
)
res = urllib.request.urlopen(req)
result = json.loads(res.read())
print('URL:', result['secure_url'])
