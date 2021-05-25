from math import sqrt


def segundo_grau(a, b, c):
    delta = (b ** 2) - (4 * a * c)

    if a == 0:
        print('O valor de A não pode ser igual a zero.')
    elif delta < 0:
        print('Delta igual a zero , a equação não possui raizes reais.')
    elif delta == 0:
        raiz_1 = (-b + sqrt(delta)) / (2 * a * c)
        raiz_2 = (-b + sqrt(delta)) / (2 * a * c)
        print("O valor de detla é igual a zero")
        print('Portanto os valores da raizes são iguais')
        print(f"x1:({raiz_1}) é igual a x2:({raiz_2})")
    else:
        raiz_1 = (-b + sqrt(delta)) / (2 * a * c)
        raiz_2 = (-b + sqrt(delta)) / (2 * a * c)
        print("O valor de delta foi um número positivo")
        print("Portanto existem duas raízes reais diferentes")
        print(f"x1({raiz_1}) x2({raiz_2}) ")


def quantidade_de_digitos(numero):
    quantidade = len(str(numero))
    print(f"Quantidade de digitos do número informado : ({quantidade})")


def area_tereno(comprimeto, largura):
    area = comprimeto * largura
    print(
        'A area do terreno informado é '
        f'igual a: {round(area,2)} metros quadrados.)'
    )


def quantida_de_sanduiche(quantidade):
    queijo = 0
    presunto = 0
    rodela_hamburguer = 0

    for contador in range(0, quantidade):
        queijo += 100
        presunto += 50
        rodela_hamburguer += 100
    print(f"""
Serão necessarios::
{queijo / 1000}kg de queijo
{presunto / 1000}kg de presunto
{rodela_hamburguer / 1000}kg de rodela de hamburguer
          """)


def calc_litros_refrigerante(
    quant_lata_350ml, quant_guarrafa_600ml, quant_garrafa_2l
):
    total_lata_350ml = 350 * quant_lata_350ml
    total_garrafa_600ml = 600 * quant_guarrafa_600ml
    total_guarrafa_2l = 2000 * quant_garrafa_2l
    total = (total_garrafa_600ml + total_guarrafa_2l + total_lata_350ml) / 1000
    print(f"Total de litros comprados : {total} litros")


def almento_salario(salario_atual):
    novo_salario = 0
    if 1500 <= salario_atual < 1750:
        novo_salario = salario_atual * 1.12
    elif 1750 <= salario_atual < 2000:
        novo_salario = salario_atual * 1.1
    elif 2000 <= salario_atual < 3000:
        novo_salario = salario_atual * 1.07
    else:
        novo_salario = salario_atual * 1.15
    print(f"Seu novo salario será de: {round(novo_salario, 2)} R$")


def verificar_c(a, b, c):
    if (a + b) > c:
        print(f"A({a}) + B({b}) é maior que C({c})")
    elif (a + b) < c:
        print(f"A({a}) + B({b}) é menor que C({c})")
    else:
        print(f"A({a}) + B({b}) é igual a C({c})")


def media_salarios():
    salarios = {}
    contador = 1
    media_salarios = 0
    sub_total = 0
    iniciar_variavel = True

    maior_salario = {
        'nome': '',
        'salario': 0
    }

    menor_salario = {
        'nome': '',
        'salario': 0
    }

    while True:
        print(f"Funcionario ({contador})")
        nome_funcionario = input('Digite o nome do funcionario: ')
        salario_functionario = float(
            input('Digite o salario do funcionario: ')
        )
        salarios.update({
            nome_funcionario: {
                'nome': nome_funcionario,
                'salario': salario_functionario
            }
        })
        print("\nDigite a palavra (fim) para parar ou qualquer outra tecla"
              " para continuar\n")
        opcao = input("Digite sua escolha: ")
        if opcao.lower() == 'fim':
            break
        contador += 1
    for v in salarios.values():
        sub_total += v['salario']
        media_salarios = (sub_total / contador)

        if iniciar_variavel:
            maior_salario = v
            menor_salario = v
            iniciar_variavel = False

        if maior_salario['salario'] < v['salario']:
            maior_salario = v
        else:
            menor_salario = v

    print(f'\nMedia dos salarios: {round(media_salarios,2)}')
    print(str(menor_salario['nome']) + ' tem o menor salario informado: ' +
          str(menor_salario['salario']) + 'R$')
    print(str(maior_salario['nome']) + ' tem o maior salario informado: ' +
          str(maior_salario['salario']) + 'R$')


def calc_desconto_previdenciario(salario):
    desconto = salario * 0.11
    if desconto <= 318.20:
        novo_salario = salario - desconto
        print(
            "\nO salario informado com disconto previdenciario "
            f"será de {novo_salario}R$"
            f'Desconto previdenciario cobrado: {desconto}R$.'
        )
    else:
        novo_salario = salario - 318.20
        print(
            "\nO salario informado com disconto previdenciario "
            f"será de {novo_salario}R$"
        )
        print('\nDesconto  previdencriario dobrado: 318.20R$.')


def calc_nome_altura_peso(
    nome_pessoa_1,
    altura_pessoa_1,
    peso_pessoa_1,
    nome_pessoa_2,
    altura_pessoa_2,
    peso_pessoa_2
):
    print('\n')
    if peso_pessoa_1 > peso_pessoa_2:
        print(f'{nome_pessoa_1} é o(a) mais peseado(a) com {peso_pessoa_1}kg.')
    elif peso_pessoa_1 == peso_pessoa_2:
        print(
            f'{nome_pessoa_1} e {nome_pessoa_2} tem o '
            f'mesmo peso de {peso_pessoa_1}kg.'
        )
    else:
        print(f'{nome_pessoa_2} é o(a) mais peseado(a) com {peso_pessoa_2}kg.')

    if altura_pessoa_1 > altura_pessoa_2:
        print(f'{nome_pessoa_1} é o(a) mais alto(a) com '
              f'{altura_pessoa_1} metros.')
    elif altura_pessoa_1 == altura_pessoa_2:
        print(
            f'{nome_pessoa_1} e {nome_pessoa_2} tem a mesma altura de '
            f'{altura_pessoa_1} metros.'
        )
    else:
        print(f'{nome_pessoa_2} é o(a) mais alto(a) com '
              f'{altura_pessoa_2} metros')
