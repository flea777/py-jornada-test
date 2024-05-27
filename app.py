import os
import json

def carregar_dados_login(filename='login_data.json'):
    try:
        with open(filename, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro ao decodificar o JSON.")
        return []

def autenticar_usuario(login_data):
    login = input('Login: ')
    senha = input('Senha: ')
    for usuario in login_data:
        if usuario['login'] == login and usuario['senha'] == senha:
            return True
    return False

def salvar_dados(lista, filename='alunos.json'):
    with open(filename, 'w') as arquivo:
        json.dump(lista, arquivo)

def carregar_dados(filename='alunos.json'):
    try:
        with open(filename, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def adicionar_aluno(lista):
    os.system('clear')
    nome_aluno = input('Nome do aluno: ')
    nome_responsavel = input('Nome do responsável: ')
    cpf = input('CPF do responsável: ')
    telefone = input('Celular do responsável: ')
    endereco = input('Endereço do aluno: ')
    lista.append({'nome_aluno': nome_aluno, 'nome_responsavel': nome_responsavel, 'cpf': cpf, 'telefone': telefone, 'endereco': endereco})
    salvar_dados(lista)
    print("Aluno adicionado com sucesso!")

def excluir_aluno(lista):
    cpf_excluir = input("Digite o CPF do aluno que você quer excluir: ")
    
    for aluno in lista:
        if aluno['cpf'] == cpf_excluir:
            lista.remove(aluno)
            salvar_dados(lista)
            print("Aluno excluído com sucesso!")
            return
    print("Aluno não encontrado.")

def listar_alunos(lista):
    for indice, aluno in enumerate(lista):
        print(f"{indice+1}. {aluno['nome_aluno']} - {aluno['telefone']}")

def atualizar_aluno(lista):
    cpf_atualizar = input("Digite o CPF do aluno que você quer atualizar: ")
    for aluno in lista:
        if aluno['cpf'] == cpf_atualizar:
            novo_nome_aluno = input("Novo nome do aluno: ")
            novo_nome_resp = input("Novo nome do responsável: ")
            novo_endereco = input("Novo endereço do aluno: ")
            novo_telefone = input("Novo telefone: ")

            aluno['nome_aluno'] = novo_nome_aluno
            aluno['nome_responsavel'] = novo_nome_resp
            aluno['endereco'] = novo_endereco
            aluno['telefone'] = novo_telefone
            
            salvar_dados(lista)
            print("Aluno atualizado com sucesso!")
            return
    print("Aluno não encontrado.")

def menu_responsaveis(lista):
    while True:
        print("Área do Aluno🚌")
        resposta = input("1 - Adicionar Aluno\n2 - Excluir Aluno\n3 - Listar Alunos\n4 - Atualizar Aluno\n5 - Voltar\nOpção: ")

        if resposta == "1":
            adicionar_aluno(lista)
        elif resposta == "2":
            excluir_aluno(lista)
        elif resposta == "3":
            listar_alunos(lista)
        elif resposta == "4":
            atualizar_aluno(lista)
        elif resposta == "5":
            os.system('clear')
            break
        else:
            print("Resposta inválida.")

def menu_principal():
    while True:
        print("Selecione uma opção:")
        resposta = input("1 - Cadastro de Responsáveis/Alunos\n2 - Cadastro de Motoristas\n3 - Cadastro de Escolas\n4 - Logout\nOpção: ")

        if resposta == '1':
            os.system('clear')
            lista = carregar_dados()
            menu_responsaveis(lista)
        elif resposta == '2':
            os.system('clear')
            print("Cadastro de Motoristas ainda não implementado...⏳")
        elif resposta == '3':
            os.system('clear')
            print("Cadastro de Escolas ainda não implementado...⏳")
        elif resposta == '4':
            os.system('clear')
            print("Logout realizado com sucesso!")
            break
        else:
            print("Opção inválida.")

def main():
    login_data = carregar_dados_login()
    if not login_data:
        print("Nenhum dado de login carregado.")
        return False
    
    while True:
        print("1 - Logar\n2 - Sair")
        opcao = input("Opção: ")

        if opcao == '1':
            if autenticar_usuario(login_data):
                print("Autenticação bem-sucedida!")
                menu_principal()
            else:
                print("Login ou senha incorretos.")
        elif opcao == '2':
            print("Programa finalizado ❌")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
