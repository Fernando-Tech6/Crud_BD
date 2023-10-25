"""
Pandas dataframe para uma tabela no mysql
Será utilizado o sqlalchemy para conectar no banco de dados.
Será realizado a criação lendo de um dataframe e depois a inserção de novos dados de outro dataframe.

"""


import pandas as pd
from sqlalchemy import create_engine, text

print('######### Criação Dataframe ##############')

dados = {"emp_name": ["Beverly Lang", "Kameko French","Ursa George", "Ferris Brown",
"Noel Meyer", "Abel Kim", "Raphael Hull","Jack Salazar","May Stout", "Haviva Montoya" ],
"emp_mgr" : ["Mike Palomino", "Mike Palomino", "Rich Hernandez", "Dan Brodi", "Kari Phelps", 
"Rich Hernandez", "Kari Phelps", "Kari Phelps", "Rich Hernandez", "Mike Palomino"], 
"dealer_id": [2,2,3,1,1,3,1,1,3,2],  "sales": [16233,16233,15427,19745,19745,12369,8227 ,9710 ,9308 ,9308 ] }


df = pd.DataFrame(dados)
print(df)

####################  Conexão  ##############################
# string de conexão dialect+driver://username:password@host:port/database
def conectar():
  sqlengine = create_engine('mysql+pymysql://root:root@127.0.0.1/Estudos',  pool_recycle=3600, echo=True)
  return sqlengine .connect()

conn = conectar()


print('\n################  Criação e inserção de dados  ##################')

# Enviando o dataframe para o banco de dados, e criando uma tabela
# index - para não gerar uma colunas index

df.to_sql('TbWindow', conn, if_exists='fail', index=False)
conn.close

# Lendo dados da tabela criad,  utilizando metodos do PANDAS
df1 = pd.read_sql("SELECT * FROM Estudos.TbWindow", conn)
print(df1)
conn.close()

print('\n################  Novo Dataframe ##################')
dados_2 = {"emp_name": ["Beverly Lang", "Kameko French"] ,
"emp_mgr" : ["Mike Palomino", "Dan Brodi"], "dealer_id" : [2,1],  "sales": [16889,52336 ] }

df2 = pd.DataFrame(dados_2)
print(df2)

# Enviando o dataframe para o banco de dados, e criando uma tabela
conn = conectar()
df2.to_sql('TbWindow', conn, if_exists='append', index=False)
conn.close()

print('\n################  Resultado final ##################')

# Selecionando os dados da tabela, utilizando metodos do SQLALCHEMY
conn = conectar()

# for i in range(5):
query = "SELECT * FROM Estudos.TbWindow"
df_final = conn.execute(text(query))
print(df_final.fetchall())

conn.close()


# if __name__ == "__main__":
    