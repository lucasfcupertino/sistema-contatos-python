print('Bem-vindo vindo a lista de contatos Lucas Freitas Cupertino.\n')

id_global = [5584584, 5584585, 5584586]
lista_contatos = []
indice_id = 0 # Índice usado para controlar qual ID será atribuído a cada novo contato.

# Função cadastrar_contatos:
# Recebe a lista de IDs (ide) como parâmetro.
# Pede os dados do usuário e armazena cada contato no dicionário "lista_contatos".
# O ID é atribuído automaticamente de acordo com a ordem de cadastro.
def cadastrar_contatos(ide):
    global indice_id

    if indice_id >= len(ide): # Verifica se ainda existem IDs disponíveis.
        print('Todos os IDs já foram usados.')
        return

    print('\n========== MENU CADASTRAR CONTATOS ==========')
    print('Para o cadastramento, preencha os espaços abaixo:')
    nome = input('Nome: ')
    atv = input('Atividade: ')
    telefone = input('Telefone: ')

    id_atual = ide[indice_id] # ID é atribuído automaticamente conforme o índice atual
    print(f'ID do contato: {id_atual}\n')

    # Dicionário contendo os dados do contato
    contato = {
        'nome': nome,
        'atividade': atv,
        'telefone': telefone,
        'identidade': id_atual,
    }
    lista_contatos.append(contato.copy()) # Adiciona o contato à lista principal.
    indice_id += 1 # Passa para o próximo ID disponível.

# Função consulta_contatos:
# Exibe um menu para consultar todos os contatos, consultar por ID.
# ou consultar por atividade (mostrando todos os contatos que exercem a mesma atividade).
def consulta_contatos():
    opcoes = {
        '1': 'Consultar Todos',
        '2': 'Consultar por ID',
        '3': 'Consultar por Setor',
        '4': 'Voltar para o Menu'
    }

    while True:
        print('\n======= MENU CONSULTA DE CONTATOS =======')
        print('Escolha uma opção:')
        for num, (opcao) in opcoes.items():
            print(f'{num} - {opcao}')

        escolha = input('Digite um número: ')

        # Mostra todos os contatos cadastrados.
        if escolha == '1':
            print('Lista de contatos: ')
            if not lista_contatos:
                print('Nenhum contato cadastrado.')
                continue
            else:
                for contato in lista_contatos:
                    print('\n======== CONTATO CADASTRADO =======')
                    print(f'Nome: {contato["nome"]}')
                    print(f'Atividade: {contato["atividade"]}')
                    print(f'Telefone: {contato["telefone"]}')
                    print(f'ID: {contato["identidade"]}')

        # Consulta de um contato específico por ID.
        elif escolha == '2':
            id_digitado = (input('Informe o ID: '))

            for contato in lista_contatos:
                if str(contato['identidade']) == id_digitado:
                    print('\n======== CONTATO CADASTRADO =======')
                    print(f'Nome: {contato["nome"]}')
                    print(f'Atividade: {contato["atividade"]}')
                    print(f'Telefone: {contato["telefone"]}')
                    print(f'ID: {contato["identidade"]}')
                    break
            else:
                print('ID não encontrado.')

        # Consulta por atividade — mostra todos os contatos com a mesma atividade.
        elif escolha == '3':
            atv_digitada = input('Digite a atividade do contato: ')
            encontrou = False # Flag para saber se algum contato foi encontrado.

            for contato in lista_contatos:
                if contato['atividade'].lower() == atv_digitada.lower():
                    print('\n======== CONTATOS CADASTRADOS =======')
                    print(f'Nome: {contato["nome"]}')
                    print(f'Atividade: {contato["atividade"]}')
                    print(f'Telefone: {contato["telefone"]}')
                    print(f'ID: {contato["identidade"]}')
                    encontrou = True

            if not encontrou:
                print('Atividade não encontrada.')

        elif escolha == '4': # Retorna ao menu principal.
            print('Voltando para o Menu...\n')
            return

        # Caso o usuário digite uma opção inválida.
        else:
            print('Opção inválida.')
            continue

# Função remover_contato:
# Permite excluir um contato com base no ID informado.
# Antes de remover, exibe os dados do contato e pede confirmação do usuário.
def remover_contato():
        id_digitada = input('Digite o ID do contato que deseja remover: ')

        for contato in lista_contatos:
            if str(contato['identidade']) == id_digitada:
                print(f'Nome: {contato["nome"]}')
                print(f'Atividade: {contato["atividade"]}')
                print(f'Telefone: {contato["telefone"]}')
                print(f'ID: {contato["identidade"]}')

                # Confirmação de remoção.
                escolha = input('Deseja remover esse contato? (sim/não): ')
                if escolha.lower() == 'sim':
                    lista_contatos.remove(contato)
                    print('Contato removido com sucesso!')
                else:
                    print('Remoção cancelada.')
                break
        else:
            print('ID inválido.')

# MENU PRINCIPAL
while True:
    print('========== MENU PRINCIPAL ==========')
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar Contato')
    print('2 - Consultar Contato')
    print('3 - Remover Contato')
    print('4 - Encerrar Programa')
    dig = input('Digite o número: ')

    if dig == '1':
        cadastrar_contatos(id_global)
    elif dig == '2':
        consulta_contatos()
    elif dig == '3':
        remover_contato()
    elif dig == '4':
        print('Encerrando Programa...')
        break
    else:
        print('Opção inválida.')