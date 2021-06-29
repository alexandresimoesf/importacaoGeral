from interface.doctor import Doctor
from geradores.gerador import Gerador
from sqls.sql import sql_inicio,\
    paciente_colunas, agenda_colunas,\
    prontuario_colunas, permissao_prontuario_colunas,\
    anamnese_colunas


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

    @staticmethod
    def colunas(sql_colunas: str):
        return ('{}, ' * (len(sql_colunas.split(', ')) - 1)) + '{} ) VALUES ('

    def produzir_sql(self):
        self._product.add("PartA0")

    def tabela_pacientes(self, tabela='pacientes'):
        sql_base = sql_inicio % tabela
        sql_pacientes_colunas = self.colunas(paciente_colunas)
        print(sql_base, sql_pacientes_colunas)

    def tabela_prontuario(self, tabela='prontuario'):
        sql_base = sql_inicio % tabela
        sql_prontuario_colunas = self.colunas(prontuario_colunas)
        print(sql_base, sql_prontuario_colunas)

    def tabela_permissao_prontuario(self, tabela='permissao_prontuario'):
        sql_base = sql_inicio % tabela
        sql_permissao_prontuario_colunas = self.colunas(permissao_prontuario_colunas)
        print(sql_base, sql_permissao_prontuario_colunas)

    def tabela_agenda(self, tabela='agenda'):
        sql_base = sql_inicio % tabela
        sql_agenda_colunas = self.colunas(agenda_colunas)
        print(sql_base, sql_agenda_colunas)

    def tabela_anamnese(self, tabela='anamnese'):
        sql_base = sql_inicio % tabela
        sql_anamnese_colunas = self.colunas(anamnese_colunas)
        print(sql_base, sql_anamnese_colunas)
