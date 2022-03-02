from rest_framework import serializers
from .models import book   #import model
 
# Create a class
class booksSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = book
        fields = '__all__'
