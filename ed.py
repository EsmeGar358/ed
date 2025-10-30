import pandas as pd
DataFrame = pd.read_csv("datos.csv")
DataFrame
#Agrupar datos por similitud
Group = DataFrame.groupby('CD')
Group
for CD, CD_DataFrame in Group:
    print(CD)
    print(CD_DataFrame)
Group.get_group('CHIHUAHUA')
