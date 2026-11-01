from loader import load_json
data = load_json("data/curriculo.example.json")
print(data["habilidades"][3]["nome"])