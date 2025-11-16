# TP : Clustering avec K-Means

# -----------------------------
# Exercice 1 : Clustering sur données simulées
# -----------------------------

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. Génération des données
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title("Nuage de points des données simulées")
plt.show()

# 2. Application de K-Means
kmeans = KMeans(n_clusters=4, random_state=0)
y_kmeans = kmeans.fit_predict(X)

print("Classe prédite du 2ème point :", y_kmeans[1], "Vraie classe :", y_true[1])
print("Classe prédite du 5ème point :", y_kmeans[4], "Vraie classe :", y_true[4])

# 3. Visualisation des clusters
for i in range(4):
    plt.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], s=50)
plt.title("Clusters identifiés par K-Means")
plt.show()

# -----------------------------
# Exercice 2 : Clustering sur le dataset Wine
# -----------------------------

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. Chargement des données
df = pd.read_csv("wine.csv")
print(df.head(10))
print(df.info())
print(df.isnull().sum())

# 2. Préparation des données pour PCA
# Suppression de la colonne 'Class'
donnees = df.drop("Class", axis=1).to_numpy()
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(donnees)

# 3. Application de K-Means
kmeans = KMeans(n_clusters=3, random_state=0)
classe_kmeans = kmeans.fit_predict(reduced_data)
labels_uniques = np.unique(classe_kmeans)
print("Valeurs des classes prédites :", labels_uniques)

# 4. Visualisation des clusters prédits
for label in labels_uniques:
    to_plot = reduced_data[np.where(classe_kmeans == label)[0]]
    plt.scatter(to_plot[:, 0], to_plot[:, 1], s=20)
plt.title("Clusters prédits par K-Means (Wine)")
plt.show()

# 5. Visualisation par vraies classes
classe = df["Class"]
labels_uniques = np.unique(classe)
for label in labels_uniques:
    to_plot = reduced_data[np.where(classe == label)[0]]
    plt.scatter(to_plot[:, 0], to_plot[:, 1], s=20)
plt.title("Répartition des vins selon les vraies classes")
plt.show()