import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import Prediction
import zipfile


@api_view(['POST'])
def imageHandler(request):
    print(request.FILES)
    data = request.FILES['file']  # or self.files['image'] in your form
    path = default_storage.save(
        '/home/manav/PycharmProjects/ClassifierAPI/ClassifierService/classifierApi/static/' + str(data),
        ContentFile(data.read()))
    path = '/home/manav/PycharmProjects/ClassifierAPI/ClassifierService/classifierApi/static/' + str(data)
    classify = Prediction.predict_profile(path)
    print(classify)
    return Response(classify)


@api_view['POST']
def zipHandler(request):
    data = request.FILES['file']  # or self.files['image'] in your form
    path = default_storage.save(
        '/home/manav/PycharmProjects/ClassifierAPI/ClassifierService/classifierApi/static/' + str(data),
        ContentFile(data.read()))
    path = '/home/manav/PycharmProjects/ClassifierAPI/ClassifierService/classifierApi/static/' + str(data)

    with zipfile.ZipFile("file.zip", "r") as zip_ref:
        zip_ref.extractall("targetdir")
