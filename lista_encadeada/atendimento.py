class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEspera:
    def __init__(self):
        self.head = None
        self.contador_verde = 1
        self.contador_amarelo = 201

    def inserirSemPrioridade(self, novo_nodo):
        if not self.head:
            self.head = novo_nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def inserirComPrioridade(self, novo_nodo):
        if not self.head or self.head.cor == 'V':
            novo_nodo.proximo = self.head
            self.head = novo_nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == 'A':
                atual = atual.proximo
            novo_nodo.proximo = atual.proximo
            atual.proximo = novo_nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A para amarelo, V para verde): ").upper()
        if cor == 'A':
            numero = self.contador_amarelo
            self.contador_amarelo += 1
        elif cor == 'V':
            numero = self.contador_verde
            self.contador_verde += 1
        else:
            print("Cor inválida. Use apenas 'A' ou 'V'.")
            return

        novo_nodo = Nodo(numero, cor)
        
        if not self.head:
            self.head = novo_nodo
        elif cor == 'V':
            self.inserirSemPrioridade(novo_nodo)
        else:
            self.inserirComPrioridade(novo_nodo)

    def imprimirListaEspera(self):
        atual = self.head
        if not atual:
            print("Fila vazia.")
            return
        print("\n=== Lista de Pacientes na Fila de Espera ===")
        while atual:
            print(f"Cartão {atual.cor}-{atual.numero}")
            atual = atual.proximo

    def atenderPaciente(self):
        if not self.head:
            print("Nenhum paciente na fila.")
            return
        print(f"\nChamando paciente com cartão {self.head.cor}-{self.head.numero} para atendimento.")
        self.head = self.head.proximo

def menu():
    lista = ListaEspera()

    while True:
        print("\n===== MENU =====")
        print("1 – Adicionar paciente à fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            lista.inserir()
        elif opcao == "2":
            lista.imprimirListaEspera()
        elif opcao == "3":
            lista.atenderPaciente()
        elif opcao == "4":
            print("Encerrando programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
