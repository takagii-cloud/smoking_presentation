import csv
import plotly.graph_objs as go


def lire_csv(nom_fichier, pays):
    annees = []
    ventes = []
    with open(nom_fichier, newline='') as fichier_csv:
        lecteur = csv.DictReader(fichier_csv)
        for ligne in lecteur:
            if ligne['Entity'] == pays:
                annees.append(int(ligne['Year']))
                ventes.append(float(ligne['Sales']))  
    return annees, ventes


nom_fichier = 'salescigarettes.csv'


pays = 'United States'


annees, ventes = lire_csv(nom_fichier, pays)


trace = go.Scatter(x=annees, y=ventes, mode='lines+markers', name='Nombre de cigarettes vendues')
layout = go.Layout(title=f'Sales of cigarettes per adult and per day ({min(annees)}-{max(annees)})', xaxis=dict(title='Year', range=[1900, 2010], tick0=1900, dtick=10), yaxis=dict(title='Number of cigarettes per adult per day', range=[0, 12], tick0=2, dtick=2))
fig = go.Figure(data=[trace], layout=layout)


nom_fichier_html = 'iframe2.html'
fig.write_html(nom_fichier_html)

print(f"Le graphique a été sauvegardé dans le fichier {nom_fichier_html}.")
