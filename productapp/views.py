from functools import partial
from django.shortcuts import get_object_or_404, render
from rest_framework import response

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status


class ProductDetails(APIView):
    def get_object(self,id):
        try:
            product = Product.objects.get(id=id)            
            return product
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        try:
            product = self.get_object(id)
            if(product is not None):
                serializer = ProductSerializer(product)
                return Response(serializer.data)
            else:
                return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

        except:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def put(self,request,id): #Update
        try:
            saved_product = get_object_or_404(Product.objects.all(),id=id)
            data = request.data
            serializer = ProductSerializer(instance=saved_product, data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Product Updated Successfully..!!'})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


    


    def delete(self,request,id): #Delete
        try:
            product = get_object_or_404(Product.objects.all(),id=id)
            product.delete()
            return Response({'message':'Product Deleted Successfully..!!'})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ProductList(APIView):

   

    def get(self,request):  # Read
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self,request): # Create
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Product Created Successfully..!!'})
        return Response(serializer.errors)
