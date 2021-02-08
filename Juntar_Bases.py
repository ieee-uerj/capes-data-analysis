import os
import glob
import pandas as pd

path = "/home/gustavo/Downloads/Bases para juntar - Discentes" #pasta onde as bases estão guardadas (no meu caso, é claro)

all_files = glob.glob(os.path.join(path, "br-capes*.csv")) #"br-capes*.csv" é o início dos arquivos. Todos com "br-capes" serão juntados. ".csv" é a extensão

df_from_each_file = (pd.read_csv(f, sep=';',encoding='latin1') for f in all_files) #aqui é importante dar o comando pd.read_csv de forma certa. Na maioria dos artigos da internet acaba-se usando como boilerplate não se percebe que tem que definir o sep e o encoding "brasileiros"

df_merged = pd.concat(df_from_each_file, ignore_index=True) 

#colunas inúteis para serem removidas do dataset são definidas aqui

colunas_para_apagar=['CD_ENTIDADE_EMEC',
'NM_ENTIDADE_ENSINO','NM_MODALIDADE_PROGRAMA','CD_CONCEITO_CURSO'
'NM_GRAU_PROGRAMA','NM_PROGRAMA_IES',
'ID_PESSOA','TP_DOCUMENTO_DISCENTE','NR_DOCUMENTO_DISCENTE','NM_DISCENTE','DS_FAIXA_ETARIA'
,'DT_MATRICULA_DISCENTE',
'DT_SITUACAO_DISCENTE','NM_TESE_DISSERTACAO','NM_ORIENTADOR_PRINCIPAL',
'ID_ADD_FOTO_PROGRAMA','ID_ADD_FOTO_PROGRAMA_IES']

df_merged=df_merged.drop(columns=colunas_para_apagar)

###########################################################################
#o código tem umas letras "A" no meio da coluna de conceito. Como os metadados não dizem o que é e eles compõem uma parte pequiníssima do dataset, achei melhor tira-los.

#código para spotar os "A"s no dataframe (depois eu percebi que existe um jeito mais fácil mas deixei esse mesmo que funcionou)
valores_invalidos=[]
for i in range(len(df_merged)):
    try:
        int(df_merged.CD_CONCEITO_PROGRAMA[i])
    except ValueError:
        valores_invalidos.append(i)

#calculando quando % do dataset tem esses valores estranhos
print(str(round(100*len(valores_invalidos)/len(df_merged),2))+'%','de valores inválidos')

#tirando os valores
df_merged=df_merged.drop(valores_invalidos)

#transformando em int
df_merged.CD_CONCEITO_PROGRAMA=df_merged.CD_CONCEITO_PROGRAMA.astype('int64')

#ajeitando o index
df_merged.index=range(0,len(df_merged))
###########################################################################

#salvando o csv
df_merged.to_csv('Discentes_2013-2019.csv',encoding='latin1',index=False)

#para rodar o código basta ir no terminal/cmd e rodar "python Juntar_Bases.py"