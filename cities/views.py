from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cities, Continent
from .serializers import CitiesSerializer

# class CitiesAPIView(generics.ListAPIView):
#     queryset = Cities.objects.all()
#     serializer_class = CitiesSerializer


class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer

    @action(methods=["get"], detail=False)
    def continents(self, request):
        continents = Continent.objects.all()
        return Response({"continents": [x.continent_name for x in continents]})
    


# class CitiesAPIList(generics.ListCreateAPIView):
#     queryset = Cities.objects.all()
#     serializer_class = CitiesSerializer

# class CitiesAPIUpdate(generics.UpdateAPIView):
#     queryset = Cities.objects.all()
#     serializer_class = CitiesSerializer

# class CitiesAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cities.objects.all()
#     serializer_class = CitiesSerializer




# Собственная реализация методов на разные запросы опираясь на базовый класс APIView

# class CitiesAPIView(APIView):
#     def get(self, request):
#         c = Cities.objects.all()
#         return Response({'posts': CitiesSerializer(c, many=True).data})
    
#     def post(self, request):
#         serializer = CitiesSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()     
#         return Response({'post': serializer.data})
    
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
        
#         try:
#             instance = Cities.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})

#         serializer = CitiesSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({"post": serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})

#         try:
#             instance = Cities.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})        
#         instance.delete()
#         return Response({"post": "delete post " + str(pk)})
    