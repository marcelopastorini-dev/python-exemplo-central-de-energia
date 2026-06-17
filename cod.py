def analisar_balanco_e_gerar_txt(injetada, consumida, meta_desejada_rs):
    TARIFA_CELESC = 0.75  # Valor estimado por kWh em SC com impostos
    
    # 1. Cálculos de Balanço e Finanças
    saldo_kwh = injetada - consumida
    
    if saldo_kwh >= 0:
        situacao = "GANHO (Crédito acumulado para o próximo mês)"
        financeiro_rs = saldo_kwh * TARIFA_CELESC
        texto_financeiro = f"+ R$ {financeiro_rs:.2f} economizados"
    else:
        situacao = "DÉFICIT (Cobrança complementar na fatura)"
        financeiro_rs = abs(saldo_kwh) * TARIFA_CELESC
        texto_financeiro = f"- R$ {financeiro_rs:.2f} a pagar de taxa extra"

    # 2. Verificação da Meta
    if saldo_kwh >= 0 and financeiro_rs >= meta_desejada_rs:
        meta_status = f"🎯 Parabéns! Meta atingida. Economia superou o objetivo de R$ {meta_desejada_rs:.2f}."
    elif saldo_kwh >= 0:
        meta_status = f"📉 Quase lá! O ganho foi bom, mas ficou abaixo da meta de R$ {meta_desejada_rs:.2f}."
    else:
        meta_status = "❌ Meta não atingida devido ao déficit de energia."

    # 3. Escrita Automática no Arquivo de Texto (.txt)
    # O modo 'w' cria o arquivo do zero ou substitui caso ele já exista
    with open("relatorio_fatura.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("======================================================\n")
        arquivo.write("         ⚡ PASTORINI ENERGIA - RELATÓRIO DE UNIDADE ⚡     \n")
        arquivo.write("======================================================\n")
        arquivo.write(f"Balanço de Energia : {saldo_kwh:+.2f} kWh\n")
        arquivo.write(f"Situação da Unidade: {situacao}\n")
        arquivo.write(f"Impacto Financeiro : {texto_financeiro}\n")
        arquivo.write(f"Status da Meta     : {meta_status}\n")
        arquivo.write("======================================================\n")
        arquivo.write("Gerado automaticamente via Script Python (Move Tecnologia)\n")

    return "✅ Sucesso! O arquivo 'relatorio_fatura.txt' foi gerado na pasta do seu projeto."


print("⚡ --- PASTORINI ENERGIA - GERADOR AUTOMÁTICO DE RELATÓRIOS --- ⚡\n")

# Entrada de dados do usuário
consumo_mes = float(input("Consumo atual da unidade (kWh gasto): "))
geracao_move = float(input("Energia injetada pela Move (kWh gerado): "))
meta_economia = float(input("Qual a meta de economia em Reais do cliente? R$ "))

# Executa a função que faz as contas e gera o arquivo físico .txt
mensagem_sucesso = analisar_balanco_e_gerar_txt(geracao_move, consumo_mes, meta_economia)

print(f"\n{mensagem_sucesso}\n")
