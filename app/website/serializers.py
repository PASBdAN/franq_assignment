from rest_framework import serializers
from website.models import Lead, Costumer


class LeadSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    email = serializers.CharField(max_length=60)
    phone = serializers.CharField(max_length=60)
    product_id = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Lead` instance, given the validated data.
        """
        return Lead.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Lead` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.product_id = validated_data.get('product_id', instance.product_id)
        instance.save()
        return instance

class CostumerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    email = serializers.CharField(max_length=60)
    phone = serializers.CharField(max_length=60)
    address = serializers.CharField(max_length=60)
    job = serializers.CharField(max_length=60)
    cpf = serializers.CharField(max_length=60)
    cnpj = serializers.CharField(max_length=60)

    def create(self, validated_data):
        """
        Create and return a new `Costumer` instance, given the validated data.
        """
        return Costumer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Costumer` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.job = validated_data.get('job', instance.job)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.cnpj = validated_data.get('cnpj', instance.cnpj)
        instance.save()
        return instance