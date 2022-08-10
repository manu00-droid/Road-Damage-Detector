import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import Prediction
import zipfile
from .models import picture
from ClassifierService import settings


@api_view(['POST'])
def imageHandler(request):

    print(request.FILES)
    s = request.FILES['file'] 
    pic_model=picture.objects.create(pic=s)
    classify = Prediction.predict_profile(settings.MEDIA_ROOT+"/userPics/"+str(s))
    print(classify)
    return Response(classify)


# @api_view['POST']
# def zipHandler(request):
#     data = request.FILES['file']  # or self.files['image'] in your form
#     path = default_storage.save(
#         '/home/manav/PycharmProjects/ClassifierAPI/ClassifierService/classifierApi/static/' + str(data),
#         ContentFile(data.read()))
#     path = '/home/manav/PycharmProjects/ClassifierAPI/ClassifierService/classifierApi/static/' + str(data)

#     with zipfile.ZipFile(path, "r") as zip_ref:
#         zip_ref.extractall("/home/manav/PycharmProjects/ClassifierAPI/ClassifierService/classifierApi/static")

