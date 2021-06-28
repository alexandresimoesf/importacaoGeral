from interface.doctor import Doctor
from geradores.gerador import Gerador
from sqls.sql import Agenda, Pacientes, Prontuario, Anamnese


class Tabela(Doctor):

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._product = Gerador()

    @property
    def product(self) -> Gerador:
        product = self._product
        self.reset()
        return product

    def produzir_sql(self):
        self._product.add("PartA0")

    def tabela_pacientes(self):
        self._product.add("Pacientes")

    def tabela_prontuario(self):
        self._product.add("Prontuario")

    def tabela_permissao_prontuario(self):
        self._product.add("Permissao prontuario")

    def tabela_agenda(self):
        self._product.add("Agenda")

    def tabela_anamnese(self):
        self._product.add("Anamnese")
