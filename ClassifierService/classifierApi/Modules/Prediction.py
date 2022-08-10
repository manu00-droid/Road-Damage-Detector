from PIL import Image
import numpy as np
import cv2
import tensorflow as tf
import os
from ClassifierService import settings

def convert_to_array(img):
    im = cv2.imread(img)
    img = Image.fromarray(im, 'RGB')
    image = img.resize((224, 224))
    return np.array(image)


def get_profile_name(label):
    if label == 0:
        return "Good"
    if label == 1:
        return "Poor"
    if label == 2:
        return "Satisfactory"
    if label == 3:
        return "Very_Poor"


print("Loading the model")
new_model = tf.keras.models.load_model(os.path.join(settings.BASE_DIR,"classifierApi/road_classificiation_model"))


def predict_profile(file):
    print("Predicting .................................")
    img = cv2.imread(file)
    print(type(img))
    # ar = self.convert_to_array(img)
    ar = img
    ar = ar / 255
    ar = cv2.resize(ar, (224, 224))
    a = []
    a.append(ar)
    a = np.array(a)
    score = new_model.predict(a, verbose=1)
    print(score)
    label_index = np.argmax(score)
    print(label_index)
    acc = np.max(score)
    profile = get_profile_name(label_index)
    print(profile)
    print("The predicted profile is a " + profile + " with accuracy =    " + str(acc))
    return profile
