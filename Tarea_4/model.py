# model.py
import tensorflow as tf
from tensorflow.keras import layers, models

def build_celeba_base_model(input_shape=(128, 128, 3), num_classes=40):

  # arquitectura CNN base para entrenar con CelebA (40 atributos).

    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation='sigmoid')  # 40 características multietiqueta
    ], name="CelebA_Base_Model")
    
    return model


def build_face_classifier(base_model_path, freeze_features=True):
    """
    Carga el modelo pre-entrenado, remueve el clasificador de CelebA,
    congela sus capas y añade la nueva cabeza clasificadora binaria.
    """
    # 1. Cargar el modelo base pre-entrenado
    base_model = models.load_model(base_model_path)
    
    # 2. Tomar las capas convolucionales (excluyendo la capa densa final y dropout)
    feature_extractor = models.Sequential(base_model.layers[:-2], name="Feature_Extractor")
    
    # 3. Congelar los parámetros de las capas pre-entrenadas si se indica
    if freeze_features:
        for layer in feature_extractor.layers:
            layer.trainable = False

    # 4. Construir la nueva red binaria (Reconocimiento de rostro propio)
    model = models.Sequential([
        feature_extractor,
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(1, activation='sigmoid')  # 1 salida: 1 = Tu rostro, 0 = Otro
    ], name="Face_Recognition_Model")
    
    return model


def prepare_for_fine_tuning(model, unfreeze_from_layer=-3, learning_rate=1e-5):
    """
    Descongelamiento parcial de capas convolucionales para el refinamiento (Fine-Tuning).
    """
    # Descongelar el modelo en general
    model.trainable = True
    
    # Si queremos mantener congeladas las primeras capas y descongelar solo las últimas
    feature_extractor = model.layers[0]
    for layer in feature_extractor.layers[:unfreeze_from_layer]:
        layer.trainable = False
        
    for layer in feature_extractor.layers[unfreeze_from_layer:]:
        layer.trainable = True

    # Recompilar con una tasa de aprendizaje baja
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    return model