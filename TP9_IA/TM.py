from keras.models import load_model  # TensorFlow est requis pour Keras
from PIL import Image, ImageOps  # pillow
import numpy as np

# Désactiver la notation scientifique pour plus de lisibilité
np.set_printoptions(suppress=True)

# Charger le modèle
model = load_model("keras_Model.h5", compile=False)

# Charger les labels
# Chaque ligne dans labels.txt correspond à une classe
with open("labels.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# Créer un tableau pour stocker l'image (forme attendue par le modèle)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Remplacer par le chemin de l'image que tu veux tester
image_path = "test_image.jpg"
image = Image.open(image_path).convert("RGB")

# Redimensionner et recadrer l'image pour 224x224
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# Convertir l'image en tableau numpy
image_array = np.asarray(image)

# Normaliser l'image
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Charger l'image dans le tableau
data[0] = normalized_image_array

# Faire la prédiction
prediction = model.predict(data)

# Trouver la classe prédite et la confiance
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

# Afficher le résultat
print(f"Class: {class_name}")
print(f"Confidence Score: {confidence_score:.4f}")
