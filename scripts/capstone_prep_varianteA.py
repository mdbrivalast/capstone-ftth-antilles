import pandas as pd
df = pd.read_csv('capstone_from_exceldata.csv',sep=';', decimal=',')

longdf1=pd.melt(df,id_vars=['Région'],
value_vars=['Raccordables FttH 2021','Raccordables FttH 2022','Raccordables FttH 2023','Raccordables FttH 2024','Raccordables FttH 2025'],
var_name='Année',
value_name='Raccordables')

longdf1['Année'] = longdf1['Année'].str.replace('Raccordables FttH ','',n=1)

longdf2=pd.melt(df,id_vars=['Région'],
value_vars=['Abonnés FttH 2021','Abonnés FttH 2022','Abonnés FttH 2023','Abonnés FttH 2024','Abonnés FttH 2025'],
var_name='Année',
value_name='Abonnés')

longdf2['Année'] = longdf2['Année'].str.replace('Abonnés FttH ','',n=1)
merged_df = pd.merge(longdf1, longdf2, how='inner', on=['Région', 'Année'])

mini_df = df.loc[:, ['Région', 'Parc de Locaux']].copy()
mini_df['Parc de Locaux'] = mini_df['Parc de Locaux'].astype(int)
full_df=pd.merge(mini_df,merged_df, how='inner',on=['Région'])

print(f'merged df = \n {merged_df}\n===')
#Contrôle du typage
#print(merged_df.dtypes)
print(f'mini df = \n {mini_df}\n===')
print(f'full_df = \n {full_df}\n===')
#Contrôle du typage après nettoyage
print(full_df.dtypes)
# parc en float, taux en float : jeu prêt

full_df.to_csv('capstone_processed_varianteA.csv', encoding='utf-8', index=False)
