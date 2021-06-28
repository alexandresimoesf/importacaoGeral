from abc import ABC, abstractmethod, abstractproperty


class Doctor(ABC):

    @abstractproperty
    def produzir_sql(self):
        pass

    @abstractmethod
    def tabela_pacientes(self):
        pass

    @abstractmethod
    def tabela_prontuario(self):
        pass

    @abstractmethod
    def tabela_permissao_prontuario(self):
        pass

    @abstractmethod
    def tabela_agenda(self):
        pass

    @abstractmethod
    def tabela_anamnese(self):
        pass