import base64, urllib.request, json, urllib.parse

with open(r'C:\Users\wender\Desktop\duelo-biblico\bg2.jpeg', 'rb') as f:
    img_data = base64.b64encode(f.read()).decode()

data = urllib.parse.urlencode({
    'file': 'data:image/jpeg;base64,' + img_data,
    'upload_preset': 'sigo_com_fe',
    'folder': 'duelo-biblico'
}).encode()

req = urllib.request.Request('https://api.cloudinary.com/v1_1/degxiuf43/image/upload', data=data)
res = urllib.request.urlopen(req)
result = json.loads(res.read())
print('URL:', result['secure_url'])