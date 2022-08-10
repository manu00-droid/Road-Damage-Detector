import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import Prediction
import zipfile
from .models import picture,zipFile
from ClassifierService import settings


@api_view(['POST'])
def imageHandler(request):

    print(request.FILES)
    data = request.FILES['file'] 
    pic_model=picture.objects.create(pic=data)
    classify = Prediction.predict_profile(settings.MEDIA_ROOT+"/userPics/"+str(data))
    print(classify)
    return Response(classify)


@api_view(['POST'])
def zipHandler(request):
    data = request.FILES['file']  
    zip_model=zipFile.objects.create(zip=data)
    with zipfile.ZipFile(data, "r") as zip_ref:
        zip_ref.extractall(settings.MEDIA_ROOT+"/userPics/")
    resp="GOT FILE!"
    print(resp)
    
    return Response(resp)
