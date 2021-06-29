sql_inicio = 'INSERT INTO public.%s ('

###########################################################################################

paciente_colunas = 'id_paciente_dermacapelli, cel, data_cadastro, ' \
                   'nascimento, ' \
                   'nome, profissao, sexo, status_P, ' \
                   'tel, flagagenda, compartilhar_prontuario, ' \
                   'config_cadastro_completo, cpf_obrigatorio, ' \
                   'ucase_nome'

###########################################################################################

agenda_colunas = 'data_agendada, data_agendada_timestamp, horario, descricao, etiqueta, ' \
                 'status, status_consulta, confirm_consulta, codigo_saida, data_solicitacao,' \
                 'tipo_atendimento, is_encaixe, data_atendimento, data_finalizacao,' \
                 'paciente_online, fk_clinica_id, fk_medico_id,' \
                 'fk_paciente_id, fk_especializacao_id, fk_forma_atendimento_id'

###########################################################################################

prontuario_colunas = ' datacriacao, fk_paciente_id,' \
                     ' coluna_extra, coluna_extra'

prontuario_coluna_now = 'SELECT now()'
prontuario_coluna_id_clinica = 'id from public.paciente where paciente.id_paciente_dermacapelli = {}'

###########################################################################################

permissao_prontuario_colunas = ' modificado_em, fk_medico_id, fk_prontuario_id, fk_rede_clinica_id,' \
                               ' escrita, leitura, coluna_extra, coluna_extra, coluna_extra'

permissao_prontuario_coluna_now = 'now()'
permissao_prontuario_coluna_fk_paciente = '(SELECT id FROM public.prontuario WHERE fk_paciente_id = (SELECT id FROM paciente where paciente.id_paciente_CLINICA={} LIMIT 1))'
permissao_prontuario_coluna_fk_clinica = '(SELECT fk_rede_clinica_id FROM public.clinica WHERE id = ({})), false, false)'

###########################################################################################

anamnese_colunas = 'anamnese, checksum, datacriacao, fk_responsavel_id, fk_prontuario_id'
