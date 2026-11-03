from loader import load_json
data = load_json("data/curriculo.example.json")
print(data["habilidades"][3]["nome"])

from validator import validate_data
print(validate_data({}))
print(validate_data({"formacao": []}))
print(validate_data(data))