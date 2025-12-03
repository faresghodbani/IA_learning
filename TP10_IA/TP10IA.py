# -----------------------------
# Tp Réseaux de Kohonen (SOM) – Wine Dataset
# -----------------------------

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from random import random
from sklearn_som.som import SOM
from sklearn.preprocessing import StandardScaler

# -----------------------------
# 1. Charger les données
# -----------------------------
wine = datasets.load_wine()
X = wine.data
label = wine.target

print("Shape X:", X.shape)
print("Classes:", set(label))

# -----------------------------
# 2. Normalisation des données (recommandé)
# -----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# 3. Créer le SOM
# -----------------------------
m, n = 16, 16       # dimensions de la grille
dim = X.shape[1]    # 13 caractéristiques
som = SOM(m=m, n=n, dim=dim, random_state=1234)

# -----------------------------
# 4. Entraîner le SOM : 1 époque (aperçu)
# -----------------------------
som.fit(X_scaled, epochs=1)
predictions_1 = som.predict(X_scaled)

x1 = predictions_1 // m + [random() for _ in range(len(predictions_1))]
y1 = predictions_1 % m + [random() for _ in range(len(predictions_1))]

# -----------------------------
# 5. Entraîner le SOM : 100 époques (apprentissage complet)
# -----------------------------
som.fit(X_scaled, epochs=100)
predictions_100 = som.predict(X_scaled)

x100 = predictions_100 // m + [random() for _ in range(len(predictions_100))]
y100 = predictions_100 % m + [random() for _ in range(len(predictions_100))]

# -----------------------------
# 6. Visualisation : scatter plots
# -----------------------------
colors = ['red', 'green', 'blue']

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(6, 10))

# Scatter 1 époque
ax[0].scatter(x1, y1, c=label, cmap=ListedColormap(colors))
ax[0].set_title("SOM projection – After 1 epoch")
ax[0].set_xlabel("X (grid)")
ax[0].set_ylabel("Y (grid)")

# Scatter 100 époques
ax[1].scatter(x100, y100, c=label, cmap=ListedColormap(colors))
ax[1].set_title("SOM projection – After 100 epochs")
ax[1].set_xlabel("X (grid)")
ax[1].set_ylabel("Y (grid)")

plt.tight_layout()
plt.show()

# -----------------------------
# 7. Visualisation : carte des distances
# -----------------------------
plt.figure(figsize=(6,5))
img = plt.imshow(som.transform(X_scaled), aspect='auto')
plt.title("SOM distance map")
plt.xlabel("Neurons")
plt.ylabel("Samples")
plt.colorbar(img)
plt.show()
