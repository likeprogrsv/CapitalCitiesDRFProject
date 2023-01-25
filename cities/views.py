from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Cities, Continent
from .serializers import CitiesSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly



class CitiesAPIList(generics.ListCreateAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class CitiesAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    permission_classes = (IsOwnerOrReadOnly, )

class CitiesAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    permission_classes = (IsAdminOrReadOnly, )




# Реализация представления без настройки ограничения прав доступа пользователей
# class CitiesViewSet(viewsets.ModelViewSet):
#     queryset = Cities.objects.all()             # Можно закоментировать при переопределении метода get_queryset, но поправить urls
#     serializer_class = CitiesSerializer

#     @action(methods=["get"], detail=False)
#     def continents(self, request):
#         continents = Continent.objects.all()
#         return Response({"continents": [x.continent_name for x in continents]})
    
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
        
#         if not pk:
#             return Cities.objects.all()[:5]

#         return Cities.objects.filter(pk=pk)



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
    