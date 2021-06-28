from clinicas.clinica import Clinica
from tabelas.tabela import Tabela
from geradores.gerador import Gerador
# Builder = Doctor
# ConcetreBuilder = Tabela
# Produto = Gerador
# Dretor = Clinica

importar = Clinica()
doctor = Tabela()
importar.doctor = doctor

importar.criar_paciente_anamnese_completo()
doctor.product.list_parts()

