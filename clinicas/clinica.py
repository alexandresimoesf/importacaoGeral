class Clinica:
    def __init__(self):
        self._doctor = None

    @property
    def doctor(self):
        return self._doctor

    @doctor.setter
    def doctor(self, doctor):
        self._doctor = doctor

    def criar_apenas_pacientes(self) -> None:
        self.doctor.tabela_pacientes()

    def criar_paciente_agenda(self) -> None:
        self.doctor.tabela_pacientes()
        self.doctor.tabela_agenda()

    def criar_paciente_agenda_prontuario(self) -> None:
        self.doctor.tabela_pacientes()
        self.doctor.tabela_prontuario()
        self.doctor.tabela_permissao_prontuario()
        self.doctor.tabela_agenda()

    def criar_paciente_anamnese(self) -> None:
        self.doctor.tabela_pacientes()
        self.doctor.tabela_agenda()
        self.doctor.tabela_anamnese()
