import json
file =open("dane_pierwsze.json")
wspolczynniki=json.load(file)
print(wspolczynniki.keys())