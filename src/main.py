from loader import load_json
from validator import validate_data

data = load_json("data/curriculo.example.json")

erros = validate_data(data)

if erros:    
    print("Erro de validação:")
    for erro in erros:
        print(erro)

else:
    print("Dados validados com sucesso!")
    