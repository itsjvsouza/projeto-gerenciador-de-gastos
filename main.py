from datetime import datetime

while True:

    inicio = int(input('\n1 - Adicionar gasto \n2 - Consultar gastos \n\nDigite o número correspondente à ação desejada: '))

    if inicio == 1:

        while True:
            d = int(input(('\n1 - Utilizar data de hoje \n2 - Digitar data \n\nOpção: ')))

            if d == 1:
                data = datetime.today()
                
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
            confirmacao = int(input(f'{data}, {descricao}, {valor}, {forma} \n1 - Sim \n2 - Não \n\nOs dados estão corretos? '))

            if confirmacao == 1:
                print('Gasto salvo com sucesso!')
            
            elif confirmacao == 2:
                continue
