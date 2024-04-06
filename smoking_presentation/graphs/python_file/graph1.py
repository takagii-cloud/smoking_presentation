import csv
import plotly.graph_objs as go


def lire_csv(nom_fichier):
    donnees_par_annee = {}
    with open(nom_fichier, newline='') as fichier_csv:
        lecteur = csv.DictReader(fichier_csv)
        for ligne in lecteur:
            annee = int(ligne['Year'])
            if annee % 10 != 0:  
                continue
            nombre_deces_hommes = float(ligne['male'])
            nombre_deces_femmes = float(ligne['female'])
            pays = ligne['Entity']
            if annee not in donnees_par_annee:
                donnees_par_annee[annee] = {'total_hommes': nombre_deces_hommes, 'total_femmes': nombre_deces_femmes, 'pays': {pays}}
            else:
                donnees_par_annee[annee]['total_hommes'] += nombre_deces_hommes
                donnees_par_annee[annee]['total_femmes'] += nombre_deces_femmes
                donnees_par_annee[annee]['pays'].add(pays)
    moyennes_par_annee = {annee: {'hommes': donnees_par_annee[annee]['total_hommes'] / len(donnees_par_annee[annee]['pays']),
                                  'femmes': donnees_par_annee[annee]['total_femmes'] / len(donnees_par_annee[annee]['pays'])}
                          for annee in donnees_par_annee}
    return moyennes_par_annee


nom_fichier = 'lungcancer.csv'  


donnees_par_annee = lire_csv(nom_fichier)


trace_hommes = go.Bar(x=list(donnees_par_annee.keys()), y=[donnees_par_annee[annee]['hommes'] for annee in donnees_par_annee],
                      name='men', marker=dict(color='lightblue'), width=3)
trace_femmes = go.Bar(x=list(donnees_par_annee.keys()), y=[donnees_par_annee[annee]['femmes'] for annee in donnees_par_annee],
                      name='women', marker=dict(color='pink'), width=3)
layout = go.Layout(title='Lung Cancer Mortality in the US',
                   xaxis=dict(title='Year', tickmode='linear', tick0=1950, dtick=10, range=[1950, 2010]),
                   yaxis=dict(title='Rate of lung cancer death per 100 000 men'))
fig = go.Figure(data=[trace_hommes, trace_femmes], layout=layout)


nom_fichier_html = 'iframe.html'
fig.write_html(nom_fichier_html)


with open(nom_fichier_html, 'r') as f:
    html_content = f.read()

with open('iframe.html', 'w') as iframe_file:
    iframe_file.write(f'<iframe srcdoc="{html_content}" width="800" height="600"></iframe>')
