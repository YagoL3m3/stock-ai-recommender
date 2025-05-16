import pandas as pd
import os
from IPython.display import display

empresas = ["ABEV3", "AZUL4", "BTOW3", "B3SA3", "BBSE3", "BRML3", "BBDC4", "BRAP4", "BBAS3", "BRKM5", "BRFS3", "BPAC11", "CRFB3", "CCRO3", "CMIG4", "HGTX3", "CIEL3", "COGN3", "CPLE6", "CSAN3", "CPFE3", "CVCB3", "CYRE3", "ECOR3", "ELET6", "EMBR3", "ENBR3", "ENGI11", "ENEV3", "EGIE3", "EQTL3", "EZTC3", "FLRY3", "GGBR4", "GOAU4", "GOLL4", "NTCO3", "HAPV3", "HYPE3", "IGTA3", "GNDI3", "ITSA4", "ITUB4", "JBSS3", "JHSF3", "KLBN11", "RENT3", "LCAM3", "LAME4", "LREN3", "MGLU3", "MRFG3", "BEEF3", "MRVE3", "MULT3", "PCAR3", "PETR4", "BRDT3", "PRIO3", "QUAL3", "RADL3", "RAIL3", "SBSP3", "SANB11", "CSNA3", "SULA11", "SUZB3", "TAEE11", "VIVT3", "TIMS3", "TOTS3", "UGPA3", "USIM5", "VALE3", "VVAR3", "WEGE3", "YDUQ3"]
#fundamentus = {
#    "ABEV3": balanco_dre_abev3,
#    "MGLU3": balanco_dre_mglu3
#}
fundamentus = {}
arquivos = os.listdir("balancos")
for arquivo in arquivos:
    nome = arquivos[-9:-4]
    if "11" in nome:
        nome = arquivos[-10:-4]
    if nome in empresas:
        #pega o balanço da empresa
        balanco = pd.read_excel(f'balancos/{arquivo}', sheet_name=0)
        #Na primeira coluna colocar o titulo com o nome da empresa
        balanco.iloc[0,0] = nome
        #pegar 1° linha e tornar um cabeçalho
        balanco.columns = balanco.iloc[0]
        balanco = balanco[1:]
        #tornar a 1° coluna (que agora tem o nome da empresa)
        balanco = balanco.set_index(nome)
        dre = pd.read_excel(f'balancos/{arquivo}', sheet_name=1)
        #Na primeira coluna colocar o titulo com o nome da empresa
        dre.iloc[0,0] = nome
        #pegar 1° linha e tornar um cabeçalho
        dre.columns = balanco.iloc[0]
        dre = balanco[1:]
        #tornar a 1° coluna (que agora tem o nome da empresa)
        dre = balanco.set_index(nome)
        display(balanco)
        display(dre)
        break