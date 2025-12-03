# TP Wine - Courbe ROC
# Étapes du TP de l'Université Côte d'Azur

# ------------------------------
# 1. Import des bibliothèques
# ------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.metrics import roc_curve, auc, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.tree import DecisionTreeClassifier

# ------------------------------
# 2. Chargement du dataset Wine
# ------------------------------
wine = datasets.load_wine()

# ------------------------------
# 3. Construction du DataFrame X
# ------------------------------
X = pd.DataFrame(wine.data)

# ------------------------------
# 4. Construction du DataFrame y
# ------------------------------
y = pd.DataFrame(wine.target)

# ------------------------------
# 6. Binarisation des labels
# ------------------------------
y = label_binarize(y, classes=[0, 1, 2])

# ------------------------------
# 8-9. Nombre de classes et dimensions
# ------------------------------
n_classes = y.shape[1]
n_samples, n_features = X.shape

# ------------------------------
# 10. Séparation train/test
# ------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=0
)

# ------------------------------
# 11. Création et entraînement du modèle DecisionTreeClassifier
# ------------------------------
model_decisiontree = DecisionTreeClassifier(
    criterion="gini",
    random_state=100,
    max_depth=3,
    min_samples_leaf=5
)
model_decisiontree.fit(X_train, y_train)

# ------------------------------
# 12. Prédictions
# ------------------------------
y_score = model_decisiontree.predict(X_test)

# ------------------------------
# 13-14. Calcul des courbes ROC et AUC
# ------------------------------
tfp = dict()   # taux faux positifs
tvp = dict()   # taux vrais positifs
roc_auc = dict()

for i in range(n_classes):
    tfp[i], tvp[i], seuils = roc_curve(y_test[:, i], y_score[:, i])
    roc_auc[i] = auc(tfp[i], tvp[i])

# ------------------------------
# 15-21. Tracé de la courbe ROC pour la classe 1
# ------------------------------
plt.figure()
plt.plot(tfp[1], tvp[1], color='green', lw=2,
         label='courbe ROC (AUC = %0.3f)' % roc_auc[1])
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='dashdot')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('Taux Faux Positifs')
plt.ylabel('Taux Vrai Positifs')
plt.title('Exemple de courbe ROC')
plt.legend(loc='lower right')
plt.show()
