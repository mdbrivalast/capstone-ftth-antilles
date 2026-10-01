import pandas as pd
df = pd.read_csv('capstone_from_exceldata.csv',sep=';', decimal=',')

longdf=pd.melt(df,id_vars=['Région'],
value_vars=['Raccordables FttH 2021','Raccordables FttH 2022','Raccordables FttH 2023','Raccordables FttH 2024','Raccordables FttH 2025',
'Abonnés FttH 2021','Abonnés FttH 2022','Abonnés FttH 2023','Abonnés FttH 2024','Abonnés FttH 2025'],
var_name='ColVar',
value_name='ColVal')

longdf[['Métriques','Année']] = longdf['ColVar'].str.extract(r"^(.*)\s+(\d+)$")
longdf['Métriques']=longdf['Métriques'].str.replace(' FttH','',n=1)
longdf=longdf.pivot(index=['Région','Année'], columns='Métriques', values='ColVal')
longdf=longdf.reset_index()

mini_df = df.loc[:, ['Région', 'Parc de Locaux']].copy()
mini_df['Parc de Locaux'] = mini_df['Parc de Locaux'].astype(int)

full_df=pd.merge(mini_df,longdf, how='inner',on=['Région'])
full_df['Taux_couverture'] = full_df['Raccordables'] / full_df['Parc de Locaux']
full_df['Take-up'] = full_df['Abonnés'] / full_df['Raccordables']

print(f'Le tableau pivoté full_df :\n\n{full_df}\n=========\nDtype :\n')
#Contrôle du typage après nettoyage
print(full_df.dtypes)
#parc en float, taux en float : jeu prêt

full_df.to_csv('capstone_processed_varianteB.csv', encoding='utf-8', index=False)