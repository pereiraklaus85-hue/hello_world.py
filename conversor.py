def converter_moeda(valor, cotacao, tipo="real_para_dolar"):
    """
    Converte valores entre Reais e Dólares.
    
    Parâmetros:
    - valor: valor numérico a ser convertido
    - cotacao: cotação do dólar
    - tipo: 'real_para_dolar' ou 'dolar_para_real' (padrão: 'real_para_dolar')
    
    Retorna o valor convertido.
    """
    if tipo == "real_para_dolar":
        return valor / cotacao
    elif tipo == "dolar_para_real":
        return valor * cotacao
    else:
        raise ValueError("Tipo inválido. Use 'real_para_dolar' ou 'dolar_para_real'.")