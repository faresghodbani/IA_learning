# TP Arbres de décision - Iris

# 1. Import des librairies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn import metrics
from sklearn.datasets import load_iris

# 2. Chargement du dataset
iris = load_iris()

# 3. Construction du DataFrame des données
donnees = pd.DataFrame(iris.data)
donnees.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

# 4. Construction du DataFrame des classes
target = pd.DataFrame(iris.target)

# 5. Séparation train/test
x_train, x_test, y_train, y_test = train_test_split(
    donnees,
    target,
    test_size=0.30,
    random_state=1
)

# 6. Création et entraînement du modèle
model_decisiontree = DecisionTreeClassifier(
    criterion="entropy",
    random_state=100,
    max_depth=3,
    min_samples_leaf=5
)
model_decisiontree.fit(x_train, y_train)

# 7. Prédictions
y_pred = model_decisiontree.predict(x_test)

# 8. Évaluation
precision = accuracy_score(y_test, y_pred) * 100
print("Précision du modèle :", precision, "%")

print("\nMatrice de confusion :")
print(confusion_matrix(y_test, y_pred))

print("\nRapport de classification :")
print(classification_report(y_test, y_pred))

print("Mean Absolute Error :", metrics.mean_absolute_error(y_test, y_pred))
print("Mean Squared Error :", metrics.mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error :", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# 9. Visualisation de l'arbre
fn = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
cn = ['setosa', 'versicolor', 'virginica']

plt.figure(figsize=(7,5))
plot_tree(
    model_decisiontree,
    feature_names=fn,
    class_names=cn,
    filled=True
)
plt.show()
