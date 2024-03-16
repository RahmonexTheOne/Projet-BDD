from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connexion à la base de données
conn = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='',
    database='apprentissage_effectif',
    auth_plugin='mysql_native_password'
)

# Route pour la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Route pour exécuter une requête SQL
@app.route('/query', methods=['POST'])
def execute_query():
    query = request.form['query']
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('result.html', data=data)



@app.route('/analyse_tendances_formation')
def analyse_tendances_formation():
    query = """
    SELECT libelle_diplome, COUNT(*) AS nombre_apprenants
    FROM Formation
    JOIN Diplomes ON Formation.ref_diplome = Diplomes.ref_diplome
    GROUP BY libelle_diplome
    ORDER BY nombre_apprenants DESC;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('result.html', data=data)


@app.route('/analyse_accessibilite')
def analyse_accessibilite():
    query = """
    SELECT IFNULL(handicap_oui_non_vide, 'Non précisé') AS handicap_oui_non_vide, 
    COUNT(*) AS nombre_apprenants_handicapes
    FROM Jeune
    GROUP BY handicap_oui_non_vide;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('result.html', data=data)


@app.route('/analyse_repartition_geographique')
def analyse_repartition_geographique():
    query = """
    SELECT libelle_ville_site, COUNT(*) AS nombre_formations
    FROM Etablissement
    GROUP BY libelle_ville_site
    ORDER BY nombre_formations DESC;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('result.html', data=data)

@app.route('/evaluation_diversite_apprenants')
def evaluation_diversite_apprenants():
    query = """
    SELECT code_sexe, COUNT(*) AS nombre_apprenants
    FROM Jeune
    GROUP BY code_sexe;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('result.html', data=data)

@app.route('/suivi_mobilite_interdepartementale')
def suivi_mobilite_interdepartementale():
    query = """
    SELECT code_depart_jeune_insee, COUNT(*) AS nombre_apprenants
    FROM Jeune
    GROUP BY code_depart_jeune_insee;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('result.html', data=data)

@app.route('/analyse_duree_formations')
def analyse_duree_formations():
    query = """
    SELECT libelle_diplome, AVG(duree_formation_mois) AS duree_formation_moyenne
    FROM Formation
    JOIN Diplomes ON Formation.ref_diplome = Diplomes.ref_diplome
    GROUP BY libelle_diplome;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('result.html', data=data)

@app.route('/analyse_repartition_formations_annee')
def analyse_repartition_formations_annee():
    query = """
    SELECT annee_formation, COUNT(*) AS nombre_formations
    FROM Formation
    GROUP BY annee_formation;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('result.html', data=data)

@app.route('/analyse_repartition_formations_secteur_activite')
def analyse_repartition_formations_secteur_activite():
    query = """
    SELECT code_naf_entreprise, COUNT(*) AS nombre_formations
    FROM Formation
    JOIN Entreprise ON Formation.ref_entreprise = Entreprise.ref_entreprise
    WHERE code_naf_entreprise IS NOT NULL
    GROUP BY code_naf_entreprise;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('result.html', data=data)

@app.route('/analyse_repartition_diplomes_niveau')
def analyse_repartition_diplomes_niveau():
    query = """
    SELECT code_niveau, GROUP_CONCAT(DISTINCT type_diplome SEPARATOR '/') AS types_diplomes, COUNT(*) AS nombre_diplomes
    FROM Diplomes
    GROUP BY code_niveau;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('result.html', data=data)

@app.route('/analyse_repartition_diplomes_type')
def analyse_repartition_diplomes_type():
    query = """
    SELECT diplome, libelle_diplome, COUNT(*) AS nombre_diplomes
    FROM Diplomes
    GROUP BY diplome
    ORDER BY nombre_diplomes DESC;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('result.html', data=data)



if __name__ == '__main__':
    app.run(debug=True)
