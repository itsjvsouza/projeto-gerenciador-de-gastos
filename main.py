from datetime import datetime

while True:

    inicio = int(input('\n1 - Adicionar gasto \n2 - Consultar gastos \n\nDigite o número correspondente à ação desejada: '))

    if inicio == 1:

        while True:
            d = int(input(('\n1 - Utilizar data de hoje \n2 - Digitar data \n\nOpção: ')))

            if d == 1:
                data = datetime.today()
                data_usuario = data.strftime('%d/%m/%Y')
                
            elif d == 2:
                data_usuario = str(input('Digite a data (DD/MM/YYYY): '))
                data_obj = datetime.strptime(data_usuario, '%d/%m/%Y')
                data = data_obj.strftime('%Y-%m-%d')
                
            else:
                print('Ação inválida.')
                continue

            descricao = str(input('Descrição: '))
            valor = float(input('Valor: R$'))
            forma = str(input('Forma (Pix ou Crédito): '))
            confirmacao = int(input(f'{data_usuario}, {descricao}, {valor}, {forma} \n1 - Sim \n2 - Não \n\nOs dados estão corretos? '))

            if confirmacao == 1:
                linha = (f'{data}, {descricao}, {valor}, {forma}')

                with open('data/gastos.csv', 'a') as arquivo:
                    arquivo.write(linha)
                
                print('\nGasto salvo com sucesso!')
                break
            
            else:
                continue
