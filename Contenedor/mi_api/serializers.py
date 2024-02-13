from rest_framework import serializers
from App1.models import AutorDb, FraseDb

# Serializador de modelo
class AutorDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorDb
        fields = '__all__'


class AutorConFraseSerializer(serializers.ModelSerializer):
    frases = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='frases-detail')
    class Meta:
        model = AutorDb
        fields = '__all__'


class FraseDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = FraseDb
        fields = '__all__'