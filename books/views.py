from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Books
from .serializers import BookSerializer

class BookList(APIView):
    def get(self, request,pk=None):
        if pk:
            books = Books.objects.filter(id=pk)
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        else:
            books = Books.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        books = Books.objects.get(id=pk)
        serializer = BookSerializer(books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            books = Books.objects.get(id=pk)
        except:
            return Response({'message': 'data not found'})
        if books:
            books.delete()
            return Response({'message': 'Delete Successfull'},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'data not found'})
