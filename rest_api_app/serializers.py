from rest_framework import serializers
from .models import*


class user_serializer(serializers.Serializer):
    id=serializers.IntegerField(required=False)
    name=serializers.CharField(max_length=40)
    age=serializers.CharField(max_length=40)
    subject=serializers.CharField(max_length=40)
    
    
    class Meta:
        model=user
        fields="__all__"    
        exclude=('id',)
        
        
    def create(self, validated_data):
        return user.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get("name",instance.name)
        instance.age=validated_data.get("age",instance.age)
        instance.subject=validated_data.get("subject",instance.subject)
        instance.save()
        return instance
    
    
    
    
    
    