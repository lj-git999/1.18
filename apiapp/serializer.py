from rest_framework.serializers import ModelSerializer

from apiapp.models import Computer


class ComputerModelSerializer(ModelSerializer):
    class Meta:
        model = Computer
        fields = ("name", "price", "brand")