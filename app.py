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

def salvar_dados(lista):
    with open('alunos.json', 'w') as arquivo:
        json.dump(lista, arquivo)

def carregar_dados():
    try:
        with open('alunos.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def adicionar_aluno(lista):
    os.system('cls')
    nome_aluno = input('Nome do aluno: ')
    nome_responsavel = input('Nome do responsável: ')
    cpf = input('CPF do responsável: ')
    telefone = input('Celular do responsável: ')
    endereco = input('Endereço do aluno: ')
    lista.append({'nome_aluno': nome_aluno, 'nome_responsavel': nome_responsavel, 'cpf': cpf, 'telefone': telefone, 'endereco': endereco})
    salvar_dados(lista)
    print("Aluno adicionado com sucesso!")

def excluir_aluno(lista):
    nome_excluir = input("Qual aluno você quer excluir? ")
    
    for aluno in lista:
        if aluno['nome_aluno'] == nome_excluir:
            lista.remove(aluno)
            salvar_dados(lista)
            print("Aluno excluído com sucesso!")
            return
    print("Aluno não encontrado.")

def listar_alunos(lista):
    for indice, aluno in enumerate(lista):
        print(f"{indice+1}. {aluno['nome_aluno']} - {aluno['telefone']}")

def atualizar_aluno(lista):
    nome_atualizar = input("Qual aluno você quer atualizar? ")
    for aluno in lista:
        if aluno['nome_aluno'] == nome_atualizar:
            novo_nome_aluno = input("Novo nome do aluno: ")
            novo_nome_resp = input("Novo nome do responsável: ")
            novo_endereco = input("Novo endereço do aluno: ")
            novo_cpf = input("Novo CPF: ")
            novo_telefone = input("Novo telefone: ")

            aluno['nome_aluno'] = novo_nome_aluno
            aluno['nome_responsavel'] = novo_nome_resp
            aluno['endereco'] = novo_endereco
            aluno['cpf'] = novo_cpf
            aluno['telefone'] = novo_telefone
            
            salvar_dados(lista)
            print("Aluno atualizado com sucesso!")
            return
    print("Aluno não encontrado.")

def menu_principal(lista):
    while True:
        print("Selecione uma opção:")
        resposta = input("1 - Área Do Aluno\n2 - Informar Ida ao Colégio\n3 - Chat\n4 - Avaliar Serviço\n5 - Logout\nOpção: ")

        if resposta == '1':
            os.system('cls')
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
                    os.system('cls')
                    break
                else:
                    print("Resposta inválida.")
        elif resposta == '2':
            os.system('cls')
            print("Ida ao colégio notificada com sucesso!✅")
        elif resposta == '3':
            os.system('cls')
            print("Ainda estamos trabalhando nisso...⏳")
        elif resposta == '4':
            os.system('cls')
            print("Ainda estamos trabalhando nisso...⏳")
        elif resposta == '5':
            os.system('cls')
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
                lista = carregar_dados()
                menu_principal(lista)
            else:
                print("Login ou senha incorretos.")
        elif opcao == '2':
            print("Programa finalizado ❌")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
