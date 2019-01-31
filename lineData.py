from datetime import datetime

class LineData:

    def __init__(self, lineNumber, lineString):
        self.linha = lineNumber
        self.tipo_de_registro = lineString[0]
        # Dado Cadastral (Principal)
        if (self.tipo_de_registro == '1'):
            #self.indicador_full_diario = lineString[1].strip()
            #self.tipo_atualizacao = lineString[2].strip()
            self.cnpj = lineString[3:17]
            self.identificador_matriz_filial = self.readInt(lineString, 17,17)
            self.razaoSocial_nome_empresarial = lineString[18:168].strip()
            self.nome_fantasia = lineString[168:223].strip()
            self.situacao_cadastral = self.readInt(lineString, 223,225)
            self.data_situacao_cadastral = self.readDatetime(lineString, 225,233)
            self.motivo_situacao_cadastral = self.readInt(lineString, 233,235)
            self.nm_cidade = lineString[235:290].strip()
            self.co_pais = lineString[290:293].strip()
            self.nm_pais = lineString[293:363].strip()
            self.codigo_natureza_juridica = self.readInt(lineString, 363,367)
            self.data_inicio_atividade =  self.readDatetime(lineString, 367,375)
            self.cnae_fiscal = self.readInt(lineString, 375,382)
            self.descricao_tipo_logradouro = lineString[382:402].strip()
            self.logradouro = lineString[402:462].strip()
            self.numero = lineString[462:468].strip()
            self.complemento = lineString[468:624].strip()
            self.bairro = lineString[624:674].strip()
            self.cep = self.readInt(lineString, 674,682)
            self.uf = lineString[682:684].strip()
            self.codigo_municipio = self.readInt(lineString, 684,688)
            self.municipio = lineString[688:738].strip()
            self.ddd_1 = lineString[738:742].strip()
            self.telefone_1 = lineString[742:750].strip()
            self.ddd_2 = lineString[750:754].strip()
            self.telefone_2 = lineString[754:762].strip()
            self.nu_ddd_fax = lineString[762:766].strip()
            self.nu_fax = lineString[766:774].strip()
            self.correio_eletronico = lineString[774:889].strip()
            self.qualificacao_do_responsavel = self.readInt(lineString, 889,891)
            self.capital_social_da_empresa = float(lineString[891:905]) if lineString[891:905].strip() else None 
            self.porte_empresa = lineString[905:907].strip()
            self.opcao_pelo_simples = lineString[907:908].strip()
            self.data_opcao_pelo_simples = self.readDatetime(lineString,908,916)
            self.data_exclusao_do_simples = self.readDatetime(lineString, 916,924)
            self.opcao_pelo_mei = lineString[924:925].strip()
            self.situacao_especial = lineString[925:948].strip()
            self.data_situacao_especial = self.readDatetime(lineString, 948,956)
        # Sócio
        elif (self.tipo_de_registro == '2'):
            #self.indicador_full_diario = lineString[1:1].strip()
            #self.tipo_atualizacao = lineString[2:2].strip()
            self.cnpj = lineString[3:17].strip()
            self.identificador_de_socio = lineString[17:18].strip()
            self.nome_socio_razao_social = lineString[18:168].strip()
            self.cnpj_cpf_socio = lineString[168:182].strip()
            self.codigo_qualificacao_socio = lineString[182:184].strip()
            self.percentual_capital_social = self.readInt(lineString,184,189)
            self.data_entrada_sociedade = self.readDatetime(lineString, 189,197)
            self.codigo_pais = lineString[197:200].strip()
            self.nome_pais_socio = lineString[200:270].strip()
            self.cpf_representante_legal = lineString[270:281].strip()
            self.nome_representante = lineString[281:341].strip()
            self.codigo_qualificacao_representante_legal = lineString[341:183].strip()
        # CNAE Secundária
        elif self.tipo_de_registro == '6':
            #self.indicador_full_diario = lineString[1:1].strip()
            #self.tipo_atualizacao = lineString[2:2].strip()
            self.cnpj = lineString[3:17].strip()
            self.cnae_secundaria = self.readInt(lineString, 17,24)
        pass

    def readInt(self, string, start, end):
        return int(string[start:end]) if string[start:end].strip() else None

    def readDatetime(self, string, start, end):
        return datetime(int(string[start:(start+4)]), int(string[(start+4):(start+6)]), int(string[(start+6):end])) if string[start:end].strip() and int(string[start:end]) > 0 else None