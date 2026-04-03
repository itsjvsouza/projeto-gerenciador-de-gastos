import src.interface as ui
from datetime import datetime, date
import os
os.system('cls')

while True:

    inicio = int(input(ui.MENU_PRINCIPAL))

    if inicio == 1:

        while True:
            escolha = int(input(ui.MENU_DATA))

            if escolha == 1:
                data = date.today()
                data_usuario = data.strftime('%d/%m/%Y')
                
            elif escolha == 2:
                data_usuario = str(input('Digite a data (DD/MM/YYYY): '))
                data_obj = datetime.strptime(data_usuario, '%d/%m/%Y')
                data = data_obj.strftime('%Y-%m-%d')

            elif escolha == 3:
                break

            else:
                print('\nAção inválida.')
                continue

            descricao = str(input('\nDescrição: '))
            valor = float(input('\nValor: R$'))
            forma = str(input(ui.MENU_PAGAMENTO))

            if forma == '1':
                forma = 'Pix'
            
            elif forma == '2':
                forma = 'Crédito'

            confirmacao = int(input(f"\n{data_usuario}, {descricao}, R${valor}, {forma}" + ui.MENU_CONFIRMACAO))

            if confirmacao == 1:
                linha = (f'{data},{descricao},{valor},{forma}\n')

                with open('data/gastos.csv', 'a', encoding='utf-8') as arquivo:
                    arquivo.write(linha)
                
                print('\n\n\033[1;32mGasto salvo com sucesso!\033[m')
                
                pergunta = int(input(ui.MENU_REPETIR_GASTO))

                if pergunta == 1:
                    continue
                
                else:
                    break

            else:
                continue
    
    elif inicio == 2:
        
        while True:
            escolha = int(input(ui.MENU_MES))
            print()

            if escolha >= 1 and escolha <=12:  
                with open('data/gastos.csv', 'r', encoding='utf-8') as arquivo:
                    linhas = arquivo.readlines()

                total = 0

                for linha in linhas:
                    partes = linha.split(',')
                    valor = float(partes[2])
                    data_str = partes[0]
                    data = datetime.strptime(data_str, '%Y-%m-%d')
                    
                    if data.month == escolha:
                        print(linha)

                        total = total + valor

                print(f'\nTotal gasto no mês: R${total}')
                
                pergunta = int(input(ui.MENU_REPETIR_CONSULTA))

                if pergunta == 1:
                    continue
                
                else:
                    break

            elif escolha == 13:
                break

            else:
                print('Opção inválida.')
                continue
    
    elif inicio == 3:
        
        escolha = int(input(ui.MENU_EXCLUIR))

        if escolha >= 1 and escolha <= 12:
            with open('data/gastos.csv', 'r', encoding='utf-8') as arquivo:
                linhas = arquivo.readlines()
                enumerate(linhas)

            while True:
                
                linhas_mes = []
                
                for linha in linhas:
                    partes = linha.split(',')
                    data_str = partes[0]
                    data = datetime.strptime(data_str, '%Y-%m-%d')

                    if data.month == escolha:
                        linhas_mes.append(linha)
                    
                
                for i in range(len(linhas_mes)):
                    print(f'\n{i + 1} - {linhas_mes[i]}')  
                
                excluir = int(input("\nDigite o número do gasto que deseja excluir: "))

                if excluir >= 1 and excluir <= len(linhas_mes):

                    confirmacao = int(input(f"\n\n\033[1;31m{linhas_mes[excluir - 1]}\033[m" + ui.MENU_CONFIRMACAO_EXCLUSAO))

                    if confirmacao == 1:
                        linhas.remove(linhas_mes[excluir - 1])
                        del linhas_mes[excluir - 1]

                        with open('data/gastos.csv', 'w', encoding='utf-8') as arquivo:
                            arquivo.writelines(linhas)

                        print('\n\033[1;32mGasto excluído com sucesso!\033[m')

                        pergunta = int(input(ui.MENU_REPETIR_EXCLUSAO))

                        if pergunta == 1:
                            continue

                        else:
                            break

                    else:
                        continue
                    
                else:
                    print('\nNúmero inválido.')
                    continue

    elif inicio == 4:
        break

    else:
        print('\nAção inválida.')
