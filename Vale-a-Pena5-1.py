def solicitar_dados():
    print("\nBem vindo ao Vale-A-Pena!\n Esse programa calcula se é mais vantajoso financeiramente comprar a vista ou a prazo")
    print("\n=== Entrada de Dados ===")
    preco_sem_desc = float(input("Digite o valor do produto à vista (preço cheio, SEM desconto) (R$): "))
    valor_parcela = float(input("Digite o valor de cada parcela (R$): "))
    parcelas = int(input("Digite o número de parcelas: "))
    juros_mensal = float(input("Digite o rendimento mensal da sua conta (%): ")) / 100
    return preco_sem_desc, valor_parcela, parcelas, juros_mensal


def simular_pagamento(preco_sem_desc, valor_parcela, parcelas, juros_mensal):
    saldo = preco_sem_desc
    tabela = []
    saldos = []
    rendimentos = []

    for mes in range(1, parcelas + 1):
        rendimento = saldo * juros_mensal
        saldo += rendimento
        saldo_antes = saldo
        saldo -= valor_parcela

        tabela.append({
            "Mês": mes,
            "Rendimento": round(rendimento, 2),
            "Saldo antes da parcela": round(saldo_antes, 2),
            "Parcela paga": valor_parcela,
            "Saldo final do mês": round(saldo, 2)
        })

        saldos.append(saldo)
        rendimentos.append(rendimento)

    return tabela, saldos, rendimentos, saldo



def exibir_resultados(preco_sem_desc, valor_parcela, parcelas, saldo_final, tabela, saldos, rendimentos):
    total_parcelado = valor_parcela * parcelas
    economia_vs_sem_desc = preco_sem_desc - saldo_final

    vantagem = "✅ Comprar parcelado é mais vantajoso." if saldo_final > 0 else "❌ Melhor pagar à vista."

    print("\n==== Comparação de Compra ====")
    print(f"Total pago parcelado: R${total_parcelado:.2f}")
    print(f"Saldo final após {parcelas} meses: R${saldo_final:.2f}")
    print(f"Valor total pago ao comprar parcelado vs. à vista: R${economia_vs_sem_desc:.2f}")
    print(f"Conclusão: {vantagem}")

    print("\n=== Tabela Mensal ===")
    print(f"{'Mês':<5}{'Rendimento':<15}{'Saldo antes':<20}{'Parcela paga':<15}{'Saldo final':<15}")
    for linha in tabela:
        print(f"{linha['Mês']:<5}{linha['Rendimento']:<15}{linha['Saldo antes da parcela']:<20}"
              f"{linha['Parcela paga']:<15}{linha['Saldo final do mês']:<15}")

    print("\n=== Gráfico de Barra (Evolução do Saldo) ===")
    max_saldo = max(saldos)
    for mes, saldo in enumerate(saldos, start=1):
        barras = int(saldo / max_saldo * 50) if max_saldo != 0 else 0
        print(f"Mês {mes:2} | {'#' * barras} ({round(saldo, 2)} R$)")

    print("\n=== Gráfico de Rendimento Mensal ===")
    max_rendimento = max(rendimentos) if rendimentos else 1
    for mes, rendimento in enumerate(rendimentos, start=1):
        barras = int(rendimento / max_rendimento * 50) if max_rendimento != 0 else 0
        print(f"Mês {mes:2} | {'#' * barras} ({round(rendimento, 2)} R$)")


def main():
    while True:
        preco_sem_desc, valor_parcela, parcelas, juros_mensal = solicitar_dados()

        tabela, saldos, rendimentos, saldo_final = simular_pagamento(preco_sem_desc, valor_parcela, parcelas, juros_mensal)

        exibir_resultados(preco_sem_desc, valor_parcela, parcelas, saldo_final, tabela, saldos, rendimentos)

        repetir = input("\nDeseja fazer outra simulação? (s para sim / n para não): ").strip().lower()
        if repetir != 's':
            print("Encerrando a sessão...")
            break


if __name__ == "__main__":
    main()
