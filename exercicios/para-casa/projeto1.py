dataset = [ 
    {'ano_receita': 2022, 'mes_receita': '1', 'faturamento': 49179, 'despesas': 6295},
    {'ano_receita': 2022, 'mes_receita': '2', 'faturamento': 12018, 'despesas': 43329},
    {'ano_receita': 2022, 'mes_receita': '3', 'faturamento': 23524, 'despesas': 49376},
    {'ano_receita': 2022, 'mes_receita': '4', 'faturamento': 29615, 'despesas': 16973},
    {'ano_receita': 2022, 'mes_receita': '5', 'faturamento': 26527, 'despesas': 43742},
    {'ano_receita': 2022, 'mes_receita': '6', 'faturamento': 48400, 'despesas': 11447},
    {'ano_receita': 2022, 'mes_receita': '7', 'faturamento': 27219, 'despesas': 25593},
    {'ano_receita': 2022, 'mes_receita': '8', 'faturamento': 46787, 'despesas': 19018},
    {'ano_receita': 2022, 'mes_receita': '9', 'faturamento': 32306, 'despesas': 13522},
    {'ano_receita': 2022, 'mes_receita': '10', 'faturamento': 27106, 'despesas': 15969},
    {'ano_receita': 2022, 'mes_receita': '11', 'faturamento': 15255, 'despesas': 20105},
    {'ano_receita': 2022, 'mes_receita': '12', 'faturamento': 23864, 'despesas': 32509},
    {'ano_receita': 2023, 'mes_receita': '1', 'faturamento': 47240, 'despesas': 55776},
    {'ano_receita': 2023, 'mes_receita': '2', 'faturamento': 42771, 'despesas': 36819},
    {'ano_receita': 2023, 'mes_receita': '3', 'faturamento': 18008, 'despesas': 35853},
    {'ano_receita': 2023, 'mes_receita': '4', 'faturamento': 21857, 'despesas': 6940},
    {'ano_receita': 2023, 'mes_receita': '5', 'faturamento': 29735, 'despesas': 59626},
    {'ano_receita': 2023, 'mes_receita': '6', 'faturamento': 33704, 'despesas': 30072},
    {'ano_receita': 2023, 'mes_receita': '7', 'faturamento': 26515, 'despesas': 12129},
    {'ano_receita': 2023, 'mes_receita': '8', 'faturamento': 18149, 'despesas': 21663},
    {'ano_receita': 2023, 'mes_receita': '9', 'faturamento': 46176, 'despesas': 12564},
    {'ano_receita': 2023, 'mes_receita': '10', 'faturamento': 24649, 'despesas': 58127},
    {'ano_receita': 2023, 'mes_receita': '11', 'faturamento': 44484, 'despesas': 5304},
    {'ano_receita': 2023, 'mes_receita': '12', 'faturamento': 30840, 'despesas': 5055},
    {'ano_receita': 2024, 'mes_receita': '1', 'faturamento': 28726, 'despesas': 25133},
    {'ano_receita': 2024, 'mes_receita': '2', 'faturamento': 34962, 'despesas': 26537},
    {'ano_receita': 2024, 'mes_receita': '3', 'faturamento': 49424, 'despesas': 29649},
    {'ano_receita': 2024, 'mes_receita': '4', 'faturamento': 42698, 'despesas': 54170},
    {'ano_receita': 2024, 'mes_receita': '5', 'faturamento': 37237, 'despesas': 48453},
    {'ano_receita': 2024, 'mes_receita': '6', 'faturamento': 30665, 'despesas': 8782},
    {'ano_receita': 2024, 'mes_receita': '7', 'faturamento': 39597, 'despesas': 12261},
    {'ano_receita': 2024, 'mes_receita': '8', 'faturamento': 49326, 'despesas': 18862},
    {'ano_receita': 2024, 'mes_receita': '9', 'faturamento': 19043, 'despesas': 48517},
    {'ano_receita': 2024, 'mes_receita': '10', 'faturamento': 24464, 'despesas': 24215},
    {'ano_receita': 2024, 'mes_receita': '11', 'faturamento': 11635, 'despesas': 8190},
    {'ano_receita': 2024, 'mes_receita': '12', 'faturamento': 39303, 'despesas': 14418}
]

def menu():
    print("----MENU---")
    print("Adicionar novo registro: Digite - 1")
    print("Calcular a receita: Digite - 2")
    print("Calcular Melhor e Pior ano : Digite - 3")
    

    opcao = input("Digite a opção desejada: ")
    
    if opcao == "1":
        adicionar_registro()
    elif opcao == "2":
        calcular_receita()
    elif opcao == "3":
        melhor_pior_ano()
    elif opcao == "4":
        saida()
    else:
        print("Opção inválida! Por favor, digite uma opção válida: ")
        menu()
        



def adicionar_registro(): 
    print("Opção escolhida: adicionar registro.")
    print("Digite os dados a seguir para adicionarmos o registro:")
    ano_receita = int(input("Digite o ano correspondente: "))
    mes_receita = input("Digite o mês correspondente: ")
    faturamento = int(input("Digite o faturamento desse mês: "))
    despesas = int(input("Digite as depesas deste mês: "))
    
    novo_registro = {
        "ano": ano_receita,
        "mes": mes_receita,
        "faturamento": faturamento,
        "despesas": despesas,
    }
    dataset.append(novo_registro)
    print(dataset)


         

def calcular_receita():
    ano = int(input("Por favor, indique o ano para o qual você gostaria de calcular a receita: "))
    valor_total = 0
    mes_receita = 0
    receita_maior = 0   

    for el in dataset:
        ano_el = el.get("ano_receita")
        if ano_el == ano:
            receita = el.get("faturamento") - el.get("despesas")  
            valor_total += receita
            if receita > receita_maior:
                receita_maior = receita
                mes_receita = el.get("mes_receita")

    print(f"A soma das receitas é: {valor_total}")
    print(f"O mês {mes_receita} foi o mais lucrativo desse ano, e o valor foi {receita_maior}")



def melhor_pior_ano():
    melhor_ano = None
    pior_ano = None
    melhor_receita = 0
    pior_receita = 0

    for item in dataset:
        ano = item['ano_receita']
        receita = item['faturamento'] - item['despesas']
        
        if receita > melhor_receita or melhor_ano is None:
            melhor_receita = receita
            melhor_ano = ano
        
        if receita < pior_receita or pior_ano is None:
            pior_receita = receita
            pior_ano = ano

    print(f"O ano com a melhor receita foi: {melhor_ano}")
    print(f"O ano com a pior receita foi: {pior_ano}")

def saida():
    print("Saindo do sistema......")

menu()




