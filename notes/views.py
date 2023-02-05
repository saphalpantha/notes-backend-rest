from http import server
from itertools import count
from tkinter.messagebox import NO
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import NoteSerializer
from rest_framework import status
from .models import Note
# Create your views here.


@api_view(['GET'])
def getNotes(request):
    totalNo = Note.objects.all().count()
    note = Note.objects.all()
    serializer = NoteSerializer(note, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request,pk):
    totalNo = Note.objects.all().count()
    if pk > str(totalNo):
        return(Response("NO NOTES FOUND"))
    print("GET length" , totalNo)
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(serializer.data)



@api_view(['DELETE'])
def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note was deleted")


@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(body=data['body'])
    serializer = NoteSerializer(note, many=False)
    if serializer: return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
