class Gerador:

    def __init__(self) -> None:
        self.tabelas = []

    def add(self, tabela) -> None:
        self.tabelas.append(tabela)

    def listar_tarefas(self) -> None:
        print(f"Gerar : {', '.join(self.tabelas)}")
