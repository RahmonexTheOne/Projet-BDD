import pandas as pd
import mysql.connector

# Load the CSV file into a DataFrame
df = pd.read_csv('bulk_with_primary.csv')

# Replace NaN values with None in the DataFrame
df = df.where(pd.notnull(df), None)

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='',
    database='apprentissage_effectif',
    auth_plugin='mysql_native_password'
)

cursor = conn.cursor()

try:
    # Insertion dans les tables
    for index, row in df.iterrows():
        # Ignorer les lignes avec code_origine_prec_cfa égal à 999
        if row['code_origine_prec_cfa'] == 999:
            continue
        # Insertion dans la table Organisation
        sql = "INSERT INTO Organisation (id_og, libelle_og) VALUES (%s, %s)"
        val = (row.get('id_og'), row.get('libelle_og'))
        cursor.execute(sql, val)

        # Insertion dans la table Entreprise
        sql = "INSERT INTO Entreprise (code_insee_entreprise, code_naf_entreprise, depart_entreprise) VALUES (%s, %s, %s)"
        val = (row.get('code_insee_entreprise'), row.get('code_naf_entreprise'), row.get('depart_entreprise'))
        cursor.execute(sql, val)

        # Insertion dans la table Etablissement
        sql = "INSERT INTO Etablissement (id_etab, nom_complet_cfa, code_uai_site, nom_site_formation, adresse1_site, adresse2_site, adresse3_site, code_commune_site_insee, code_postal_site, libelle_ville_site, ref_og, ref_entreprise) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (row.get('id_etab'), row.get('nom_complet_cfa'), row.get('code_uai_site'), row.get('nom_site_formation'), row.get('adresse1_site'), row.get('adresse2_site'), row.get('adresse3_site'), row.get('code_commune_site_insee'), row.get('code_postal_site'), row.get('libelle_ville_site'), row.get('ref_og'), row.get('ref_entreprise'))
        cursor.execute(sql, val)

        # Insertion dans la table Diplomes
        sql = "INSERT INTO Diplomes (diplome, libelle_diplome, code_niveau, type_diplome, code_groupe_specialite, libelle_specialite, libelle_specialite_com, code_origine_prec_cfa, libelle_origine_prec_cfa, code_origine_annee_prec, libelle_origine_annee_prec) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (row.get('diplome'), row.get('libelle_diplome'), row.get('code_niveau'), row.get('type_diplome'), row.get('code_groupe_specialite'), row.get('libelle_specialite'), row.get('libelle_specialite_com'), row.get('code_origine_prec_cfa'), row.get('libelle_origine_prec_cfa'), row.get('code_origine_annee_prec'), row.get('libelle_origine_annee_prec'))
        cursor.execute(sql, val)

        # Insertion dans la table Formation
        sql = "INSERT INTO Formation (duree_formation_mois, annee_formation, num_section, ref_etab, ref_entreprise, ref_diplome) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (row.get('duree_formation_mois'), row.get('annee_formation'), row.get('num_section'), row.get('ref_etab'), row.get('ref_entreprise'), row.get('ref_diplome'))
        cursor.execute(sql, val)

        # Insertion dans la table Entreprise_Formation
        sql = "INSERT INTO Entreprise_formation (ref_entreprise, ref_formation) VALUES (%s, %s)"
        val = (row.get('ref_entreprise'), row.get('ref_formation'))
        cursor.execute(sql, val)

        # Insertion dans la table Jeune
        sql = "INSERT INTO Jeune (age_jeune_decembre, handicap_oui_non_vide, code_sexe, code_qualite, code_nationalite, code_pcs, libelle_pcs_parent, code_statut_jeune, code_depart_jeune_insee, code_commune_jeune_insee, code_postal_jeune, libelle_ville_jeune, ref_formation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (row.get('age_jeune_decembre'), row.get('handicap_oui_non_vide'), row.get('code_sexe'), row.get('code_qualite'), row.get('code_nationalite'), row.get('code_pcs'), row.get('libelle_pcs_parent'), row.get('code_statut_jeune'), row.get('code_depart_jeune_insee'), row.get('code_commune_jeune_insee'), row.get('code_postal_jeune'), row.get('libelle_ville_jeune'), row.get('ref_formation'))
        cursor.execute(sql, val)

        

    # Commit the changes and close the connection
    conn.commit()
    print("Data inserted successfully.")
except mysql.connector.Error as err:
    print("An error occurred:", err)

# Close the connection
conn.close()
