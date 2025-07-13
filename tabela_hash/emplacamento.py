class NodoEstado:
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10

    def funcao_hash(self, sigla):
        if sigla == "DF":
            return 7
        return (ord(sigla[0]) + ord(sigla[1])) % 10

    def inserir_estado(self, sigla, nome):
        pos = self.funcao_hash(sigla)
        novo = NodoEstado(sigla, nome)
        novo.proximo = self.tabela[pos]
        self.tabela[pos] = novo

    def imprimir_tabela(self):
        print("\n=== Tabela Hash ===")
        for i in range(10):
            print(f"Posição {i}:", end=" ")
            atual = self.tabela[i]
            if not atual:
                print("Vazia")
            else:
                while atual:
                    print(f"{atual.sigla}", end=" -> ")
                    atual = atual.proximo
                print("None")

def main():
    th = TabelaHash()

    print("Tabela hash antes das inserções:")
    th.imprimir_tabela()

    estados = [
        ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
        ("BA", "Bahia"), ("CE", "Ceará"), ("ES", "Espírito Santo"), ("GO", "Goiás"),
        ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
        ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
        ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins"), ("DF", "Distrito Federal")
    ]

    for sigla, nome in estados:
        th.inserir_estado(sigla, nome)

    print("\nTabela hash após inserir os 26 estados + DF:")
    th.imprimir_tabela()

    # Implementação para inserção de um Estado fictício (Jamile Silva → JS)
    th.inserir_estado("JS", "Jamile Silva")

    print("\nTabela hash após inserir estado fictício:")
    th.imprimir_tabela()

if __name__ == "__main__":
    main()
