from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Artiste,Song
from .serializers import ArtisteSerializer,SongSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@csrf_exempt
@api_view(['GET','POST'])
def artiste_list_and_song_List(request):
    if request.method=='GET':
        artiste=Artiste.objects.all()
        song=Song.objects.all()
        art_serializer=ArtisteSerializer(artiste,many=True)
        song_serializer=SongSerializer(song,many=True)
        return Response({'Artiste':art_serializer.data + song_serializer.data})

    if request.method=='POST':
        art_serializer=ArtisteSerializer(data=request.data)
        if art_serializer.is_valid():
            art_serializer.save()
            return Response(art_serializer.data,status=status.HTTP_201_CREATED)

        song_serializer=SongSerializer(data=request.data)
        if song_serializer.is_valid():
            song_serializer.save()
            return Response(song_serializer.data,status=status.HTTP_201_CREATED)    

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def song_details(request,id):
    try:
        song=Song.objects.get(pk=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        song_serializer=SongSerializer(song)
        return Response(song_serializer.data) 
    elif request.method=='PUT':
        song_serializer=SongSerializer(song,data=request.data)
        if song_serializer.is_valid():
            song_serializer.save()
            return Response(song_serializer.data)
        return Response(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    elif request.method=='DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
























"""
from musicapp.models import Artiste, Song
from musicapp.serializers import ArtisteSerializer, SongSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#from songcrud import musicapp


class Artiste_and_Song_List(APIView):
 
    def get(self, request, format=None):
        musicapp = Artiste.objects.all()
        musicapp = Song.objects.all()
        serializer = ArtisteSerializer(musicapp, many=True)
        serializer = SongSerializer(musicapp, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArtisteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class SongDetails(APIView):
   
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Song = self.get_object(pk)
        serializer = SongSerializer(Song)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Song = self.get_object(pk)
        serializer = SongSerializer(Song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Song = self.get_object(pk)
        Song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""








