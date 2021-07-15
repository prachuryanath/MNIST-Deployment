import requests

resp = requests.post("https://flask-mnist-pal.herokuapp.com/predict", files= {'file':open('download.png', 'rb')})

print(resp.text)