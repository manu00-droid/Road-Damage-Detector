from PIL import Image
import numpy as np
import os
from ClassifierService import settings
from keras.models import load_model
from PIL import Image, ImageOps


def get_profile_name(label):
    if label == 0:
        return "Pothole"
    if label == 1:
        return "Not-Pothole"
    if label == 2:
        return "Unknown"



print("Loading the model")
new_model = load_model(os.path.join(settings.BASE_DIR,"ClassifierApi/road_classificiation_model/keras_model.h5"))


def predict_profile(file):
    path=os.path.join(settings.MEDIA_ROOT,"userPics",file)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(path)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = new_model.predict(data)
    print(prediction)
    profile=get_profile_name(np.argmax(prediction))
    
    print("The predicted profile is a " , profile )
    return profile