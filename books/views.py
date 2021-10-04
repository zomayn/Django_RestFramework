from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Books
from .serializers import BooksSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/booksList/',
        'Detail View': '/bookdetail/<str:pk>/',
        'Create': '/bookcreate',
        'Update': '/bookupdate/<str:pk>/',
        'Delete': '/bookdelete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def booksList(request):
    books = Books.objects.all()
    serializer = BooksSerializer(books,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def booksDetail(request,pk):
    books = Books.objects.get(id=pk)
    serializer = BooksSerializer(books,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def booksCreate(request):
    serializer = BooksSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def booksUpdate(request,pk):
    books = Books.objects.get(id=pk)
    serializer = BooksSerializer(instance=books,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def booksDelete(request,pk):
    books = Books.objects.get(id=pk)
    books.delete()

    return Response('Item is deleted successfully')