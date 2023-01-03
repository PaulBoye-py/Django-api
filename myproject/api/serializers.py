# We need to serialize the models because response object in views.py cannot
# natively handle complex datatypes such as Django model instances

from rest_framework import serializers
from base.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'