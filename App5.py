import xml.etree.ElementTree as ET

# Função para adicionar um novo contato
def adicionar_contato(root, nome, telefone, email):
    contato = ET.SubElement(root, 'contato')
    nome_element = ET.SubElement(contato, 'nome')
    nome_element.text = nome
    telefone_element = ET.SubElement(contato, 'telefone')
    telefone_element.text = telefone
    email_element = ET.SubElement(contato, 'email')
    email_element.text = email

# Função principal
def main():
    # Cria o elemento raiz do XML
    root = ET.Element('contatos')

    while True:
        print('Menu:')
        print('1. Adicionar contato')
        print('2. Salvar contatos e sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            nome = input('Digite o nome do contato: ')
            telefone = input('Digite o telefone do contato: ')
            email = input('Digite o e-mail do contato: ')
            adicionar_contato(root, nome, telefone, email)
        elif opcao == '2':
            tree = ET.ElementTree(root)
            tree.write('contatos.xml')
            print('Contatos salvos no arquivo contatos.xml. Encerrando o programa.')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    main()
 
 
