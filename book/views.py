from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from rest_framework import status, mixins, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Books
from .serializers import BookSerializer,Register_serializer

# @api_view(['GET','POST','PUT'])
# def book_List(request):
#     if request.method == 'GET':
#         b = Books.objects.all()
#         bk = BookSerializer(b,many=True)
#         return Response(bk.data,status=status.HTTP_200_OK)
#     elif request.method=="POST" :
#         b = BookSerializer(data=request.data)
#
#         if b.is_valid():
#             b.save()
#             return Response(b.data,status=status.HTTP_201_CREATED)
#         return Response(b.errors,status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET','PUT','DELETE'])
# def book_details(request,pk):
#     try:
#         b=Books.objects.get(pk=pk)
#     except Books.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if(request.method=="GET"):
#         bk = BookSerializer(b)  # serialization- converting django format into json,(many= true-more objects )
#         return Response(bk.data, status=status.HTTP_200_OK)
#
#     elif (request.method == "PUT"):
#         b = BookSerializer(b,data=request.data)  # converting request data in json format into django format
#
#         if b.is_valid():  # validating data
#             b.save()  # saves the data into db after validation
#             return Response(b.data, status=status.HTTP_201_CREATED)
#
#     elif(request.method=="DELETE"):
#         b.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class based view

# define a parent class also -API view

# non primary-key based
# class BookListView(APIView):
#     def get(self,request):
#         b = Books.objects.all()  # Read all student records
#         bk = BookSerializer(b,many=True) # serialization- converting django format into json,(many= true-more objects )
#         return Response(bk.data,status=status.HTTP_200_OK)
#
#     def post(self,request):
#         b = BookSerializer(data=request.data)
#
#         if b.is_valid():  # validating data
#             b.save()  # saves the data into db after validation
#             return Response(b.data,status=status.HTTP_201_CREATED)
#         return Response(b.errors,status=status.HTTP_400_BAD_REQUEST)
#
# class BookDetailView(APIView):
#     def get_object(self,pk):
#         try:
#             return Books.objects.get(pk=pk)
#         except Books.DoesNotExist:
#             raise Http404
#
#     def get(self,request,pk):
#         b=self.get_object(pk)
#         bk = BookSerializer(b)  # serialization- converting django format into json,(many= true-more objects )
#         return Response(bk.data, status=status.HTTP_200_OK)
#
#     def put(self,request,pk):
#         b=self.get_object(pk)
#         bk = BookSerializer(b, data=request.data)  # converting request data in json format into django format
#
#         if bk.is_valid():  # validating data
#                 bk.save()  # saves the data into db after validation
#                 return Response(b.data, status=status.HTTP_201_CREATED)
#     def delete(self,request,pk):
#         b=self.get_object(pk)
#         b.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Mixins
# class BookListView(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
#     queryset= Books.objects.all()
#     serializer_class= BookSerializer
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
# class BookDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
#
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#
#     def put(self,request,pk):
#         return self.update(request,pk)
#
#     def delete(self,request,pk):
#         return self.destroy(request, pk)

# generics
# class BookListView(generics.ListCreateAPIView):
#     queryset= Books.objects.all()
#     serializer_class = BookSerializer
#
# class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer

# viewsets

# class BookView(viewsets.ModelViewSet):  # get, put, post , delete
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer

class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('search')
        print(query)
        if query:
            s=Books.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
            bk = BookSerializer(s,many=True)
        return Response(bk.data,status=status.HTTP_200_OK)


class Register(viewsets.ModelViewSet):  # get, put, post , delete

    queryset = User.objects.all()
    serializer_class = Register_serializer

# Authentication
class BookView(viewsets.ModelViewSet):  # get, put, post , delete
    # permission_classes = [IsAuthenticated]
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class LogoutApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'msg':'logout successfully'},status=status.HTTP_200_OK)

