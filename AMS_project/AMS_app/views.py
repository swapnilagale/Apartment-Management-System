from django.shortcuts import render
from .serializers import ApartmentSerializer,ApartmentTypeSerializer,Building,BuildingSerializer
from .models import ApartmentType,Apartment,Building
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status









class ApartmentList(APIView):

    def get(self,request):
        apartments = Apartment.objects.all()
        serializer = ApartmentSerializer(apartments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApartmentDetail(APIView):
  
    def get_object(self, pk):
      
        try:
            return Apartment.objects.get(pk=pk)
        except Apartment.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        apartment = self.get_object(pk)
        serializer = ApartmentSerializer(apartment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        apartment = self.get_object(pk)
        serializer = ApartmentSerializer(apartment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk, format=None):
        apartment = self.get_object(pk)
        serializer = ApartmentSerializer(apartment,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        apartment = self.get_object(pk)
        apartment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class BuildingList(APIView):

    def get(self,request):
        buildings = Building.objects.all()
        serializer = BuildingSerializer(buildings, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = BuildingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BuildingDetail(APIView):
  
    def get_object(self, pk):
      
        try:
            return Building.objects.get(pk=pk)
        except Building.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        building = self.get_object(pk)
        serializer = BuildingSerializer(building)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        building = self.get_object(pk)
        serializer = BuildingSerializer(building, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk, format=None):
        building = self.get_object(pk)
        serializer = BuildingSerializer(building,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        building = self.get_object(pk)
        building.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApartmentTypeList(APIView):

    def get(self,request):
        apartment_types = ApartmentType.objects.all()
        serializer = ApartmentTypeSerializer(apartment_types, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ApartmentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApartmentTypeDetail(APIView):
  
    def get_object(self, pk):
      
        try:
            return ApartmentType.objects.get(pk=pk)
        except ApartmentType.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        apartment_types = self.get_object(pk)
        serializer = ApartmentTypeSerializer(apartment_types)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        apartment_types = self.get_object(pk)
        serializer = ApartmentTypeSerializer(apartment_types, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk, format=None):
        apartment_types = self.get_object(pk)
        serializer = ApartmentTypeSerializer(apartment_types,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        apartment_types = self.get_object(pk)
        apartment_types.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
