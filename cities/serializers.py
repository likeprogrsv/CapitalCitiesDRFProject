from rest_framework import serializers
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from .models import Cities


class CitiesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cities
        fields = "__all__"


# Кастомный пример сериализатора для понимания того как они работают,
# если придется писать свой собственный

# class CitiesSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     continent_id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Cities.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update",
#                                                   instance.time_update)
#         instance.is_published = validated_data.get("is_published",
#                                   instance.is_published)
#         instance.continent_id = validated_data.get("continent_id",
#                                   instance.continent_id)
#         instance.save()
#         return instance

# def encode():
#     model = CitiesModel("Oslo", "Oslo city")
#     model_sr = CitiesSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream = io.BytesIO(b'{"title": "Oslo",
#           "content": "recive Oslo city info"}')
#     data = JSONParser().parse(stream)
#     serializer = CitiesSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
