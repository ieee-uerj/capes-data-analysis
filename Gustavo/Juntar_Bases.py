#Usei esse código para juntar as bases de discentes. Depois de entende-lo basta mudar o que for nescessário para juntar as outras bases

import os
import glob
import pandas as pd
import inspect

#usado para tirar uns avisos chatos de "mixed type"
import warnings
warnings.filterwarnings("ignore") 

print('Importando as bases')

df1=pd.read_csv('data/Para_juntar/juntar-Docentes_Cursos_features2013-2019.csv', sep=',',encoding='latin1')
df2=pd.read_csv('data/Para_juntar/juntar-Features_docentes_dicentes_teses.csv', sep=',',encoding='latin1')
df3=pd.read_csv('data/Para_juntar/juntar-programas_e_financiadores.csv', sep=',',encoding='latin1')

print('Juntando as bases')
#Como evitar colunas com o mesmo nome duplicadas na base "mergida"(kkkkkkkkkk): https://www.pauldesalvo.com/how-to-remove-or-prevent-duplicate-columns-from-a-pandas-merge/

temp = pd.merge(df1,df2,how='inner',on=['CD_PROGRAMA_IES','AN_BASE'], suffixes=('', '_drop'))
temp.drop([col for col in temp.columns if 'drop' in col], axis=1, inplace=True)

df_merged=pd.merge(temp,df3,how='inner',on=['CD_PROGRAMA_IES','AN_BASE'], suffixes=('', '_drop'))
df_merged.drop([col for col in df_merged.columns if 'drop' in col], axis=1, inplace=True)

#ajeitando o index
df_merged.index=range(0,len(df_merged))
###########################################################################

print('Salvando o arquivo')
#salvando o csv
df_merged.to_csv('data/Para_juntar/Grande Base2.csv',encoding='latin1',index=False)

#para rodar o código basta ir no terminal/cmd e rodar "python Juntar_Bases.py"
