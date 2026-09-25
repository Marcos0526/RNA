# dataset.py
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def get_celeba_generators(csv_path, img_dir, target_size=(128, 128), batch_size=32, validation_split=0.2):
    # Cargar las etiquetas de atributos
    df = pd.read_csv(csv_path)
    
    # Keras requiere que los valores del dataframe sean string para clasificación multietiqueta
    attr_cols = list(df.columns[1:])
    df[attr_cols] = df[attr_cols].astype(str)
    
    # Generador con normalización
    datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=validation_split
    )
    
    train_gen = datagen.flow_from_dataframe(
        dataframe=df,
        directory=img_dir,
        x_col=df.columns[0],
        y_col=attr_cols,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='raw',
        subset='training'
    )
    
    val_gen = datagen.flow_from_dataframe(
        dataframe=df,
        directory=img_dir,
        x_col=df.columns[0],
        y_col=attr_cols,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='raw',
        subset='validation'
    )
    
    return train_gen, val_gen


def get_face_recognition_generators(data_dir, target_size=(128, 128), batch_size=16, validation_split=0.2):
    """
    Carga las imágenes de tu rostro y de otras personas aplicando Data Augmentation sintético.
    Estructura esperada en data_dir:
        - data_dir/my_face/
        - data_dir/others/
    """
    datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
        fill_mode='nearest',
        validation_split=validation_split
    )
    
    train_gen = datagen.flow_from_directory(
        data_dir,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='binary',
        subset='training',
        shuffle=True
    )
    
    val_gen = datagen.flow_from_directory(
        data_dir,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='binary',
        subset='validation',
        shuffle=False
    )
    
    return train_gen, val_gen