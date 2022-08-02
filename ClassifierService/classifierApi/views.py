import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import Prediction


@api_view(['POST'])
def imageHandler(request):
    data = request.FILES['file']  # or self.files['image'] in your form
    path = default_storage.save(
        '/home/manav/PycharmProjects/ClassifierAPI/ClassifierService/classifierApi/' + str(data),
        ContentFile(data.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)
    print(tmp_file)
    classify = Prediction.predict_profile(tmp_file)
    print(classify)
    return Response(classify)
