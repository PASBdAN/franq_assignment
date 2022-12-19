from rest_framework import serializers
from marketing.models import Lead


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