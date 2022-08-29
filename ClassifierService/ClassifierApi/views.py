import os
from unittest import result
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User 
from datetime import date
import Prediction
import zipfile
from .models import *
from ClassifierService import settings
import requests
import base64
import numpy as np
from wsgiref.util import FileWrapper
import pandas as pd
from django.contrib import auth
from django.http import HttpResponse

#create LatLng object

# LatLng.objects.create(lat=0,lng=0,postaladd=1,countryAdress='countryAdd',stateAdress='stateAdd',cityAdress='cityAdd',route='routeAdd')




@api_view(['POST'])
def imageHandler(request):
    data = request.data['file']
    lat = request.data['lat']
    lng = request.data['lng']
    midleimg=open(settings.MEDIA_ROOT+"/userPics/middleimg.png","wb")
    midleimg.write(base64.b64decode(data))
    midleimg.close()
    print("IMAGE CONVERTED!!!!!")
    classify = Prediction.predict_profile("middleimg.png")
    print(classify)
    #os.remove(settings.MEDIA_ROOT+"/userPics/middleimg.png")
    if classify == "Pothole":
        addPoint(lat,lng)
    return Response(classify)


@api_view(['POST'])
def zipHandler(request):
    data = request.FILES['file']
    zip_model = zipFile.objects.create(zip=data)
    with zipfile.ZipFile(data, "r") as zip_ref:
        zip_ref.extractall(settings.MEDIA_ROOT + "/userPics/")
    resp = "GOT FILE!"
    print(resp)

    return Response(resp)



@api_view(['GET'])
def getPoints(request):
    all_val=LatLng.objects.all().values()
    lat_arr=[]
    lng_arr=[]
    for i in range(len(all_val)):
        lat_arr.append(str(LatLng.objects.all().values()[i]['lat']))
        lng_arr.append(str(LatLng.objects.all().values()[i]['lng']))
    points_array=[]
    # print(LatLng.objects.all().values()[0]['lat'])
    for i in range(len(lat_arr)):
       points_array.append([lat_arr[i],lng_arr[i]])
    return Response(points_array)



def addPoint(lat,lng):
    loc=settings.gmc.snap_to_roads(path=(lat,lng),interpolate=False)[0]["location"]

    lat=loc['latitude']
    lng=loc['longitude']
    print("HEREREr")
    add=settings.gmc.reverse_geocode(latlng=(lat,lng))
    add=add[0]['address_components']
    routeAdd=add[0]['long_name']
    cityAdd=add[4]['long_name']
    
    stateAdd=add[-3]['long_name']
    countryAdd=add[-2]['long_name']
    LatLng(lat=lat,lng=lng,postaladd=2,countryAdress=countryAdd,stateAdress=stateAdd,cityAdress=cityAdd,route=routeAdd)
    LatLng.save()


@api_view(['POST'])
def addpoint(request):
    lat=request.data['lat']
    lng=request.data['lng']
    loc=settings.gmc.snap_to_roads(path=(lat,lng),interpolate=False)[0]["location"]

    lat=loc['latitude']
    lng=loc['longitude']
    print(lat)
    add=settings.gmc.reverse_geocode(latlng=(lat,lng))
    add=add[0]['address_components']
    routeAdd=add[0]['long_name']
    cityAdd=add[4]['long_name']
    
    stateAdd=add[-3]['long_name']
    countryAdd=add[-2]['long_name']
    # postalAdd=add[-1]['long_name']
    obj=LatLng(lat=lat,lng=lng,postaladd=1,countryAdress=countryAdd,stateAdress=stateAdd,cityAdress=cityAdd,route=routeAdd)
    obj.save()
    return Response("done")




@api_view(['POST'])
def zipHandlerwCSV(request):
    data = request.FILES['file']
    csv=request.FILES['csv']
    
    zip_model = zipFile_csv.objects.create(zip=data,csv=csv)
    with zipfile.ZipFile(data, "r") as zip_ref:
        zip_ref.extractall(settings.MEDIA_ROOT + "/userPics/picsfromZip")
    resp = "GOT FILE!"
    print(resp)
    imageHandlerZip_csv()
    print("Done")
    return Response(resp)



def imageHandlerZip_csv():
    file=settings.MEDIA_ROOT + "/userPics/picsfromZip"
    csv=os.listdir(settings.MEDIA_ROOT +"/userZip/csv")[0]
    print(csv)
    df=pd.read_csv(settings.MEDIA_ROOT +"/userZip/csv/"+csv)
    df=np.array(df)
    print(len(df))
    images=os.listdir(file)
    # print(images)
    for i in range(len(images)):
        print("picsfromZip/"+images[i])
        classify = Prediction.predict_profile("picsfromZip/"+images[i])
        # print(classify)
        if classify=="Pothole":
            index=int(images[i].split(".")[0])
            print(index,"HERERERERERERER")
            print(len(df))
            print(df[index-1][0])
            addPoint(df[index-1][0],df[index-1][1])
    for i in images:
        os.remove(settings.MEDIA_ROOT +"/userPics/picsfromZip/"+i)
            
@api_view(['POST'])
def login(request):
    una=request.data['email']
    pwd=request.data['pwd']
    found_user=users.objects.filter(email=una)
    if found_user is not None:
        # print(found_user.values()[0]["password"])
        if (found_user.values()[0]["password"])==pwd:
            print("HERERERERER")
            return Response(found_user.values()[0]["type"])

    else:
        return Response('False')
        
@api_view(['POST'])
def signup(request):


    email=request.data['email']
    pwd=request.data['pwd']
    fna=request.data['fna']
    lna=request.data['lna']
    type=request.data['typeGovOfficial']
    
    user=users.objects.create(type=type,password=pwd,first_Name=fna,last_Name=lna,email=email)
    user.save()
    return Response("DONE")



@api_view(['GET'])
def displayAllProjects(request):
    projects=Project.objects.all().values()
    return Response(projects)


@api_view(['POST'])
def displaySelectProjects(request):
    pid=request.data['pid']
    print(pid)
    Project_data=Project_det.objects.filter(p_id=pid).values()
    return Response(Project_data)

@api_view(['POST'])
def addProj(request):
    pid=request.data['pid']
    p_name=request.data['name']
    Project.objects.create(p_id=pid,p_name=p_name)
    print("Project created.")
    return Response("DONE")

@api_view(['POST'])
def updateProj(request):
    pid=request.data['pid']
    name=request.data['name']
    temp=request.data['temp']
    pH=request.data['pH']
    humid=request.data['humid']
    road_len_const=request.data['road_length']
    p_no=request.data['pno']
    proj_row=Project_det(pH=pH,temp=temp,humid=humid,p_name=name,p_no=p_no,road_len_const=road_len_const,p_id=pid)
    proj_row.save()
    print("Project created.")
    return Response("DONE")


@api_view(['POST'])
def getTypeFromEmail(request):
    email=request.data["email"]
    found_user=users.objects.filter(email=email)
    return Response(found_user.values()[0]["type"])

@api_view(['GET'])
def thingToClient(request):
    msg=requests.get("https://thingspeak.com/channels/1830210/feeds.csv")
    Currentdate=date.today()
    with open(settings.MEDIA_ROOT+f"/{Currentdate}.csv",'wb') as f:
        f.write(msg.content)
    f.close()
    df=pd.read_csv(settings.MEDIA_ROOT+f"/{Currentdate}.csv")
    df.to_csv(settings.MEDIA_ROOT+"/out.zip",compression='zip')
    
    zip_file = open(settings.MEDIA_ROOT+"/out.zip", 'rb')
    response = HttpResponse(FileWrapper(zip_file), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="%s"' % f'{Currentdate}'
    return response
    
