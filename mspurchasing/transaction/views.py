from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Vendor, PurchaseOrder, Product, Category, ProductType, Priority, Responsible
from .serializers import VendorSerializer, PurchaseOrderSerializer, ProductSerializer, CategorySerializer, ProductTypeSerializer, PrioritySerializer, ResponsibleSerializer

class VendorAPIView(APIView):
    def get(self, request):
        queryset = Vendor.objects.all()
        serializer = VendorSerializer(queryset, many=True)
        return Response(serializer.data)

class PurchaseOrderAPIView(APIView):
    def get(self, request):
        queryset = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseOrderDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return PurchaseOrder.objects.get(pk=pk)
        except PurchaseOrder.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        purchase_order = self.get_object(pk)
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        purchase_order = self.get_object(pk)
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        purchase_order = self.get_object(pk)
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductAPIView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class CategoryAPIView(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

class ProductTypeAPIView(APIView):
    def get(self, request):
        queryset = ProductType.objects.all()
        serializer = ProductTypeSerializer(queryset, many=True)
        return Response(serializer.data)

class PriorityAPIView(APIView):
    def get(self, request):
        queryset = Priority.objects.all()
        serializer = PrioritySerializer(queryset, many=True)
        return Response(serializer.data)

class ResponsibleAPIView(APIView):
    def get(self, request):
        queryset = Responsible.objects.all()
        serializer = ResponsibleSerializer(queryset, many=True)
        return Response(serializer.data)
