import mysql.connector
import pandas as pd
import plotly.express as px

# Se connecter à la base de données
conn = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='',
    database='apprentissage_effectif',
    auth_plugin='mysql_native_password'
)



#----------------------------------------------------------------------------------
# Exécuter une requête SQL pour récupérer les données
query = """
    SELECT libelle_diplome, COUNT(*) AS nombre_apprenants
    FROM Formation
    JOIN Diplomes ON Formation.ref_diplome = Diplomes.ref_diplome
    GROUP BY libelle_diplome
    ORDER BY nombre_apprenants DESC;
"""
df = pd.read_sql(query, conn)

# Créer une visualisation en violon avec un titre ajusté
fig = px.violin(df, y='libelle_diplome', x='nombre_apprenants', orientation='h', title='Répartition des apprenants par type de diplôme',
                labels={'nombre_apprenants': 'Nombre d\'apprenants', 'libelle_diplome': 'Type de diplôme'},
                points='all', box=True, hover_name='libelle_diplome', color='nombre_apprenants')

# Personnaliser la mise en page
fig.update_layout(xaxis_title='Nombre d\'apprenants', yaxis_title='Type de diplôme')
fig.update_traces(meanline_visible=True, jitter=0.05, scalemode='count')

# Ajuster la taille du texte du titre des diplômes
fig.update_layout(title_font=dict(size=18))

# Afficher la visualisation
fig.show()
#----------------------------------------------------------------------------------




#----------------------------------------------------------------------------------
# Exécuter une requête SQL pour récupérer les données
query_geo = """
    SELECT libelle_ville_site, COUNT(*) AS nombre_formations
    FROM Etablissement
    GROUP BY libelle_ville_site
    ORDER BY nombre_formations DESC;
"""
df_geo = pd.read_sql(query_geo, conn)

# Créer une visualisation de la répartition géographique
fig_geo = px.bar(df_geo, x='libelle_ville_site', y='nombre_formations', title='Répartition géographique des centres de formation')

# Afficher la visualisation
fig_geo.show()
#----------------------------------------------------------------------------------



#----------------------------------------------------------------------------------
# Exécuter une requête SQL pour récupérer les données
query_handicap = """
    SELECT handicap_oui_non_vide, COUNT(*) AS nombre_apprenants
    FROM Jeune
    GROUP BY handicap_oui_non_vide;
"""
df_handicap = pd.read_sql(query_handicap, conn)

# Créer une visualisation de l'accessibilité pour les handicapés
fig_handicap = px.pie(df_handicap, names='handicap_oui_non_vide', values='nombre_apprenants', title='Accessibilité des formations pour les apprenants handicapés')

# Afficher la visualisation
fig_handicap.show()
#----------------------------------------------------------------------------------



#----------------------------------------------------------------------------------
# Exécuter une requête SQL pour récupérer les données
query = """
    SELECT code_depart_jeune_insee, code_niveau, COUNT(*) AS nombre_apprenants
    FROM Jeune
    JOIN Formation ON Jeune.ref_formation = Formation.ref_formation
    JOIN Diplomes ON Formation.ref_diplome = Diplomes.ref_diplome
    GROUP BY code_depart_jeune_insee, code_niveau;
"""
df = pd.read_sql(query, conn)

# Créer une visualisation de la répartition des niveaux de diplôme par département
fig = px.bar(df, x='code_depart_jeune_insee', y='nombre_apprenants', color='code_niveau',
             title='Répartition des niveaux de diplôme par département',
             labels={'code_depart_jeune_insee': 'Département', 'nombre_apprenants': 'Nombre d\'apprenants'})

# Afficher la visualisation
fig.show()
#----------------------------------------------------------------------------------



# Fermer la connexion
conn.close()
