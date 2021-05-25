import functions

while True:
    print("""
Escolha uma opção disponivel abaixo:
(1):Calcular uma equação do segundo grau.
(2):Calcular a quantidade de digitos de um número.
(3):Calcular a area de um terreno.
(4):Calcular a quantidade de ingredientes de um sanduíche.
(5):Calcular a quantidade de litros de refrigerantes.
(6):Calcular aumento salarial de um funcionario.
(7):Comparar peso e altura de duas pessoas.
(8):Calcular a soma de A e B.
(9):Calcular a media de sálarios de uma empresa.
(10):Calcular o desconto previdenciário.
      """)
    opcao = (
        input('\nDigite uma das opções apresentadas acima ou '
              'digite o número 0 ou a palarava "sair" '
              'para terminar a execução: ')
    )

    if opcao == '0' or opcao.lower() == 'sair':
        print('Saindo...')
        break
    elif opcao == '1':
        print('\nOpção(1)')
        print('Calcular uma equação do segundo grau\n')
        a = int(input('Digite o valor de A: '))
        b = int(input('Digite o valor de B: '))
        c = int(input('Digite o valor de C: '))
        print('Resultado: ')
        functions.segundo_grau(a, b, c)
    elif opcao == '2':
        print('\nOpção(2)')
        print('Calcular a quantidade de digitos de um número')
        numero = int(input('Digite um número: '))
        functions.quantidade_de_digitos(numero)
    elif opcao == '3':
        print('\nOpção(3)')
        print('Calcular a area de um terreno')
        largura = float(input('Digite a largura do terreno em metros: '))
        comprimento = float(
            input('Digite o comprimento do terreno em metros: '))
        functions.area_tereno(comprimento, largura)
    elif opcao == '4':
        print('\nOpção(4)')
        print('Calcular a quantidade de ingredientes de um sanducihe')
        quantidade = int(
            input('Digite a quantidade de sanduíches que deseja: ')
        )
        functions.quantida_de_sanduiche(quantidade)
    elif opcao == '5':
        print('\nOpção(5)')
        print('Calcular a quantidade de litros de refrigerantes')
        quant_lata_350ml = int(
            input('Digite a quantidade de latas de 350ml: '))
        quant_garrafa_600ml = int(
            input('Digite a quantidade de guarrafas de 600ml: '))
        quant_garrafa_2L = int(
            input('Digite a quantidade de garrafas de 2 litros: '))
        functions.calc_litros_refrigerante(
            quant_lata_350ml,
            quant_garrafa_600ml,
            quant_garrafa_2L
        )
    elif opcao == '6':
        print('\nOpção(6)')
        print('Calcular aumento salárial de um funcionario')
        salario = float(input('Digite o salário do funcionario: '))
        functions.almento_salario(salario)
    elif opcao == '7':
        print('\nOpção(7)')
        print('Comparar peso e altura de duas pessoas')
        nome_primeira_pessoa = input("Digite o nome da primeira pessoa: ")
        altura_primeira_pessoa = float(
            input("Digite a altura da primeira pessoa: "))
        peso_primeira_pessoa = float(
            input('Digite o peso da primeira pessoa: '))
        nome_segunda_pessoa = input("\n\nDigite o nome da segunda pessoa: ")
        altura_segunda_pessoa = float(
            input("Digite a altura da segunda pessoa: "))
        peso_segunda_pessoa = float(
            input('Digite o peso da segunda pessoa: '))

        functions.calc_nome_altura_peso(
            nome_primeira_pessoa,
            altura_primeira_pessoa,
            peso_primeira_pessoa,
            nome_segunda_pessoa,
            altura_segunda_pessoa,
            peso_segunda_pessoa,
        )
    elif opcao == '8':
        print('\nOpção(8)')
        print('Calcular a soma de A e B.')
        a = float(input('Digite um valor para A: '))
        b = float(input('Digite um valor para B: '))
        c = float(input('Digite um valor para C: '))
        functions.verificar_c(a, b, c)
    elif opcao == '9':
        print('\nOpção(9)')
        print('Calcular a media de sálarios de uma empresa.')
        functions.media_salarios()
    elif opcao == '10':
        print('\nOpção(10)')
        print('Calcular o desconto previdenciário.')
        salario = float(input('Digite o salario: '))
        functions.calc_desconto_previdenciario(salario)
    else:
        print('\n******* -> Opacão escolhida invalida tente novamente '
              '<- *******.\n')
