#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import path
import sys
import re

planilhas = {
    u'CÂMPUS ÁGUAS LINDAS.csv': 3647,
    u'CÂMPUS ANÁPOLIS.csv': 699,
    u'CÂMPUS APARECIDA DE GOIÂNIA.csv': 210,
    u'CÂMPUS CIDADE DE GOIÁS.csv': 696,
    u'CÂMPUS FORMOSA.csv': 2012,
    u'CÂMPUS GOIÂNIA.csv': 212,
    u'CÂMPUS GOIÂNIA OESTE.csv': 3646,
    u'CÂMPUS INHUMAS.csv': 238,
    u'CÂMPUS ITUMBIARA.csv': 244,
    u'CÂMPUS JATAÍ.csv': 241,
    u'CÂMPUS LUZIÂNIA.csv': 209,
    u'CÂMPUS SENADOR CANEDO.csv': 3648,
    u'CÂMPUS URUAÇU.csv': 161,
    u'CÂMPUS VALPARAÍSO.csv': 3649
}

for item in planilhas.iteritems():
    try:
        file_csv = open(path.join(path.curdir, item[0]), 'r+')
    except:
        e = sys.exc_info()[1]
        print (u'\n\tNão foi possível abrir o arquivo: \"%s\"' % item[0])
        print (u'\n\t\aErro: %s' % e)
        continue
    new_lines = []
    new_line_items = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    file_csv.readline()
    for line in file_csv:
        # COLUNAS DO ARQUIVO CSV
        # 00: CO_ALUNO_NAO_IDENTIFICADO
        # 01: CO_ALUNO
        # 02: NO_ALUNO
        # 03: NO_NOME_SOCIAL
        # 04: DS_CODIGO_ALUNO
        # 05: NO_MAE_ALUNO
        # 06: CO_PESSOA_FISICA_ALUNO
        # 07: DS_SENHA
        # 08: CO_MATRICULA
        # 09: CO_CICLO_MATRICULA
        # 10: CO_STATUS_CICLO_MATRICULA
        # 11: CO_CURSO
        # 12: NU_CARGA_HORARIA
        # 13: DT_DATA_INICIO
        # 14: DT_DATA_FIM_PREVISTO
        # 15: CO_UNIDADE_ENSINO
        # 16: CO_PERIODO_CADASTRO
        # 17: NO_CICLO_MATRICULA
        # 18: ST_ATIVO
        # 19: CO_TIPO_OFERTA_CURSO
        # 20: CO_TIPO_INSTITUICAO
        # 21: CO_INSTITUICAO
        # 22: CO_PORTFOLIO
        # 23: CO_TIPO_NIVEL_OFERTA_CURSO
        # 24: CO_TIPO_PROGRAMA_CURSO
        # 25: ST_CARGA
        # 26: DT_DATA_FINALIZADO
        # 27: NU_VAGAS_OFERTADAS
        # 28: NU_TOTAL_INSCRITOS
        # 29: ST_ETEC
        # 30: CO_POLO
        # 31: UAB
        # 32: ST_PREVISTO
        # 33: NU_VAGAS_PREVISTAS
        # 34: CO_CURSO_SUPERIOR_CORRELATO
        # 35: NU_CARGA_HORARIA_ESTAGIO
        # 36: NO_ARQUIVO
        # 37: NO_CAMINHO_ARQUIVO
        # 38: ST_ESTAGIO
        # 39: ST_EXPERIMENTAL
        # 40: NO_STATUS_MATRICULA
        # 41: CO_PESSOA_FISICA
        # 42: NU_RG
        # 43: SG_SEXO
        # 44: DT_NASCIMENTO
        # 45: NO_PESSOA_FISICA
        # 46: NU_CPF
        # 47: CO_PESSOA
        # 48: CO_CARGO
        # 49: DS_ORGAO_EXPEDIDOR
        # 50: SG_UF_ORG_EXPED
        # 51: DS_CARGO
        # 52: CO_UNIDADE_ENSINO_IMPORTACAO
        # 53: CO_MATRICULA_RESPONSAVEL
        # 54: NO_SOCIAL
        # USAREMOS OS CAMPOS:
        # 02; 46; 11; 13; 14; 17; 19; 30; 40
        line_items = line.split(';')
        new_line_items[0] = line_items[2].strip('\"')
        new_line_items[1] = line_items[46].strip('\"')
        new_line_items[2] = line_items[11].strip('\"')
        new_line_items[3] = line_items[13].strip('\"')
        new_line_items[4] = line_items[14].strip('\"')
        new_line_items[5] = line_items[17].strip('\"')
        new_line_items[6] = line_items[19].strip('\"')
        new_line_items[7] = line_items[30].strip('\"')
        new_line_items[8] = line_items[40].strip('\"')
        # VERIFICA SE CURSO EH DO TIPO EAD:
        re_ead = re.compile(u'^.*[AÀÁ]\s*DIST[AÂ]NCIA.*$')
        match_ead = re_ead.search(new_line_items[5])
        if match_ead:
            cursos = [338565, 338569, 338571, 338572, 338573, 338574, 338575,
                338578, 338580, 338581, 338582, 338583]
            if int(new_line_items[2]) not in cursos:
                continue
        else:
            cursos = [
                2, 3, 5, 6, 16, 18, 28, 29, 31, 32, 34, 36, 39, 40, 43, 47, 48,
                51, 52, 60, 67, 73, 74, 75, 80, 82, 85, 93, 95, 98, 120, 121,
                125, 131, 135, 144, 145, 149, 154, 158, 172, 181, 52824, 52833,
                52840, 52842, 52843, 52845, 52850, 52855, 52856, 52858, 52865,
                52921, 52927, 52933, 52942, 52943, 52947, 52953, 52955, 52958,
                52987, 52993, 52997, 52999, 53000, 53002, 53003, 53006, 53008,
                53011, 53012, 53013, 53015, 53032, 53175, 53176, 53320, 53409,
                53430, 53438, 53452, 53453, 63981, 124846, 143913, 204293,
                204295, 246114, 272602, 272632, 272658, 272724, 272742, 273527,
                276053, 276054, 276993, 276994, 280772, 315396, 319635, 333929,
                338565, 338569, 338571, 338572, 338573, 338574, 338575, 338578,
                338580, 338581, 338582, 338583, 339641, 339665, 339672, 340703,
                352434, 362343
            ]
            if int(new_line_items[2]) not in cursos:
                continue
        # AJUSTA O CPF
        cpf = '000.000.000-00'
        new_line_items[1] = cpf
        # AJUSTA AS DATAS
        dt_inicio = new_line_items[3][8:10] + '/' + new_line_items[3][5:7] + '/' + new_line_items[3][0:4]
        dt_fim = new_line_items[4][8:10] + '/' + new_line_items[4][5:7] + '/' + new_line_items[4][0:4]
        new_line_items[3] = dt_inicio
        new_line_items[4] = dt_fim
        # CRIA UMA LINHA NOVA E ADICIONA SE NÃO FOR UMA LINHA REPETIDA
        new_line = ';'.join(new_line_items)
        new_line = new_line + '\n'
        if new_line in new_lines:
            print(new_line)
            continue
        new_lines.append(new_line)
    file_csv.seek(0)
    file_csv.truncate()
    file_csv.write('NO_ALUNO;NU_CPF;CO_CURSO;DT_DATA_INICIO;DT_DATA_FIM_PREVISTO;NO_CICLO_MATRICULA;CO_TIPO_OFERTA_CURSO;CO_POLO;NO_STATUS_MATRICULA\n')
    file_csv.writelines(new_lines)
    file_csv.flush()
    file_csv.close()