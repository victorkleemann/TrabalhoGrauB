import csv

# Função para carregar os dados do DatabaseGatos.csv
def carregarDados(database):
    with open(database, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        dados = list(reader)
    return dados

# Função para salvar os dados no DatabaseGatos.csv
def salvarDados(database, dados):
    if not dados:
        print("Nenhum dado para salvar.")
        return

    fieldnames = dados[0].keys()
    with open(database, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        writer.writerows(dados)
    print("Dados salvos com sucesso!")

# Função para exibir o menu principal da ONG
def menuPrincipal():
    print("="*30)
    print("     ONG Adote Gatinhos     ")
    print("="*30)
    print("1) Cadastrar felino")
    print("2) Alterar status de felino")
    print("3) Consultar informações sobre felino")
    print("4) Apresentar estatísticas gerais")
    print("5) Filtragem de dados")
    print("6) Salvar")
    print("7) Sair do programa")
    escolha = input("Escolha uma opção: ")
    return escolha

# Função para cadastrar um novo felino
def cadastrarFelino(dados):
    novo_felino = {}
    novo_felino['Nome'] = input("Nome: ")
    novo_felino['Sexo'] = input("Sexo: ")
    novo_felino['Idade'] = input("Idade: ")
    novo_felino['Raça'] = input("Raça: ")
    novo_felino['Cor predominante'] = input("Cor predominante: ")
    novo_felino['Cadastrado'] = input("Cadastrado: ")
    novo_felino['FIV+'] = input("FIV+: ")
    novo_felino['FELV+'] = input("FELV+: ")
    novo_felino['Data de resgate'] = input("Data de resgate (dd/mm/aaaa): ")
    novo_felino['Adotado'] = input("Adotado: ")
    novo_felino['Lar Temporário'] = input("Lar Temporário: ")
    novo_felino['Data de Adoção/Hospedagem'] = input("Data de Adoção/Hospedagem (dd/mm/aaaa): ")
    novo_felino['Tutor'] = input("Tutor: ")
    novo_felino['Contato'] = input("Contato: ")
    novo_felino['Data da última vacina'] = input("Data da última vacina (dd/mm/aaaa): ")
    novo_felino['Data da última desvermifugação'] = input("Data da última desvermifugação (dd/mm/aaaa): ")
    novo_felino['Data do último antipulgas'] = input("Data do último antipulgas (dd/mm/aaaa): ")
    novo_felino['Informações extras'] = input("Informações extras: ")
    dados.append(novo_felino)

# Função para alterar o status do felino selecionado
def alterarStatus(dados):
    for i, felino in enumerate(dados):
        print(f"{i + 1}) {felino['Nome']}")
    escolha = int(input("Escolha um felino para alterar: ")) - 1

    if 0 <= escolha < len(dados):
        felino = dados[escolha]
        campos = list(felino.keys())
        for i, campo in enumerate(campos):
            print(f"{i + 1}) {campo}: {felino[campo]}")
        while True:
            campoEscolha = int(input("Escolha um campo para alterar (ou 0 para sair): ")) - 1
            if campoEscolha == -1:
                break
            if 0 <= campoEscolha < len(campos):
                novoValor = input(f"Novo valor para {campos[campoEscolha]}: ")
                felino[campos[campoEscolha]] = novoValor

# Função para consultar informações de um felino
def consultarFelino(dados):
    for i, felino in enumerate(dados):
        print(f"{i + 1}) {felino['Nome']}")
    escolha = int(input("Escolha um felino para consultar: ")) - 1

    if 0 <= escolha < len(dados):
        felino = dados[escolha]
        for campo, valor in felino.items():
            print(f"{campo}: {valor}")

# Função para apresentar estatísticas gerais
def apresentarEstatisticas(dados):
    total = len(dados)
    machos = sum(1 for felino in dados if felino['Sexo'].lower() == 'macho')
    femeas = total - machos
    adotados = sum(1 for felino in dados if felino['Adotado'].lower() == 'sim')
    nao_adotados = total - adotados

    fivNegativo = sum(1 for felino in dados if felino['FIV+'].lower() == 'não')
    fivPositivo = total - fivNegativo
    felvNegativo = sum(1 for felino in dados if felino['FELV+'].lower() == 'não')
    felvPositivo = total - felvNegativo

    print(f"Porcentagem de machos: {machos / total * 100:.2f}%")
    print(f"Porcentagem de fêmeas: {femeas / total * 100:.2f}%")
    print(f"Porcentagem de adotados: {adotados / total * 100:.2f}%")
    print(f"Porcentagem de não adotados: {nao_adotados / total * 100:.2f}%")
    print(f"Porcentagem de FIV-: {fivNegativo / total * 100:.2f}%")
    print(f"Porcentagem de FIV+: {fivPositivo / total * 100:.2f}%")
    print(f"Porcentagem de FELV-: {felvNegativo / total * 100:.2f}%")
    print(f"Porcentagem de FELV+: {felvPositivo / total * 100:.2f}%")

# Função para filtrar dados por período de resgate ou adoção
def filtrarDados(dados, filtro):
    anoInicio = int(input("Ano de início: "))
    anoFim = int(input("Ano de fim: "))
    data = 'Data de resgate' if filtro == 'resgate' else 'Data de Adoção/Hospedagem'
    
    for felino in dados:
        dataFiltrada = felino[data]
        if dataFiltrada:
            ano = int(dataFiltrada.split('/')[-1])
            if anoInicio <= ano <= anoFim:
                print(f"Nome: {felino['Nome']}, {data}: {felino[data]}")

# Função principal do programa
def menu():
    database = 'DatabaseGatos.csv'
    dados = carregarDados(database)
    
    while True:
        escolha = menuPrincipal()
        
        if escolha == '1':
            cadastrarFelino(dados)
        elif escolha == '2':
            alterarStatus(dados)
        elif escolha == '3':
            consultarFelino(dados)
        elif escolha == '4':
            apresentarEstatisticas(dados)
        elif escolha == '5':
            subopcao = input("1) Filtrar por resgate\n2) Filtrar por adoção\nEscolha uma opção: ")
            if subopcao == '1':
                filtrarDados(dados, 'resgate')
            elif subopcao == '2':
                filtrarDados(dados, 'adoção')
        elif escolha == '6':
            salvarDados(database, dados)
        elif escolha == '7':
            salvarDados(database, dados)
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()
