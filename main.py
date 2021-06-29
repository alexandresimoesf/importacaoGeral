from clinicas.clinica import Clinica
from tabelas.tabela import Tabela
from geradores.gerador import Gerador
# Builder = Doctor
# ConcetreBuilder = Tabela
# Produto = Gerador
# Dretor = Clinica

importar = Clinica()
doctor = Tabela(id_da_clinica=83)
importar.doctor = doctor

# importar.criar_paciente_anamnese_completo()
# doctor.product.listar_tarefas()
doctor.tabela_pacientes()
doctor.tabela_agenda()
doctor.tabela_prontuario()
doctor.tabela_permissao_prontuario()
doctor.tabela_anamnese()