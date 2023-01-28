"""CapitalCitiesDRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from cities.views import (
    CitiesAPIList, CitiesAPIUpdate, CitiesAPIDestroy
)
# from rest_framework import routers
# from rest_framework_simplejwt.views import (
# TokenObtainPairView, TokenRefreshView, TokenVerifyView)
# from cities.routes import MyCustomRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/cities/', CitiesAPIList.as_view()),
    path('api/v1/cities/<int:pk>/', CitiesAPIUpdate.as_view()),
    path('api/v1/citiesdelete/<int:pk>/', CitiesAPIDestroy.as_view()),

    # пути в случае реализации с помощью токенов
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # пути в случае реализации с помощью JWT-токенов
    # path('api/token/', TokenObtainPairView.as_view(),
    #       name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(),
    #       name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(),
    #       name='token_verify'),
]


# Настройка маршрутов при определении одного представления на
# все основные методы запросов
# router = routers.DefaultRouter()
# # Добавить атрибут basename="cities" при переопределении get_queryset
# # во views если не будет строки queryset = Cities.objects.all()
# router.register(r'cities', CitiesViewSet)

# Можно использовать кастомные классы роутов
# router = MyCustomRouter()
# router.register(r'cities', CitiesViewSet)

# Пути url в случае использования маршрутов route
# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # http://127.0.0.1:8000/api/v1/cities/
#     path('api/v1/', include(router.urls))


# Старый вариант без использования роута

# path('api/v1/citieslist/', CitiesViewSet.as_view({"get": "list"})),
# path('api/v1/citieslist/<int:pk>/',
#       CitiesViewSet.as_view({"put": "update"})),
