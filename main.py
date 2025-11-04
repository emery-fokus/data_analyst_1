import pandas as pd
import matplotlib.pyplot as plt

# Chargement du fichier Excel
fichier = "E-commerce_data.xlsx"
xls = pd.ExcelFile(fichier)

# Lecture de la feuille "customers"
customer = pd.read_excel(xls, sheet_name="customers")
customer.columns = customer.columns.str.strip()

# Conversion de la date d'inscription
customer["join_date"] = pd.to_datetime(customer["join_date"])
customer["annee_inscription"] = customer["join_date"].dt.year

# Analyse du nombre de clients par année
clients_par_annee = customer["annee_inscription"].value_counts().sort_index()

# Graphique en barres
clients_par_annee.plot(kind='bar', color='skyblue', figsize=(8, 5))
plt.title("Nombre de clients par année d'inscription")
plt.xlabel("Année")
plt.ylabel("Nombre de clients")
plt.tight_layout()
plt.show()

# Lecture de la feuille produits et ventes
produits = pd.read_excel(xls, sheet_name="produits")
ventes = pd.read_excel(xls, sheet_name="ventes")

# Fusion des données
df = ventes.merge(produits, left_on="produit_id", right_on="id")

# Calcul du chiffre d'affaires
df["chiffre_affaires"] = df["quantite"] * df["prix"]

ventes_par_produit = df.groupby("nom")["chiffre_affaires"].sum().reset_index()

# Visualisation 
plt.bar(ventes_par_produit["nom"], ventes_par_produit["chiffre_affaires"], color="red")
plt.title("Chiffre d'affaires par produit")
plt.xlabel("Produit")
plt.ylabel("CA (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calcul du CA total par client
ca_total = df.groupby("client_id")["chiffre_affaires"].sum().reset_index()














