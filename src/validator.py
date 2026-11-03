def validate_data(data):
    erros = []
    sesoes_obrigatorias = ["dados_pessoais", "habilidades", "projetos", "perfis", "formacao"]
    for secao in sesoes_obrigatorias:
        if data.get(secao) is None:
            erros.append(f"Campo '{secao}' ausente.")
    return erros

