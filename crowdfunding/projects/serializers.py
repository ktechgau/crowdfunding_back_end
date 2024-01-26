from rest_framework import serializers
from .models import Project, Pledge, Category
from django.db.models import Sum



class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    class Meta:
        model = Pledge
        fields = '__all__'

class PledgeDetailSerializer(PledgeSerializer):   
    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.project = validated_data.get('project', instance.project)
        instance.supporter = validated_data.get('supporter', instance.supporter)
        instance.save()
        return instance
    
   
class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())    #One category can be chosen for one project

    class Meta:
        model = Project
        fields = '__all__'  
    

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField(source='category.category')    #Category can be seen in project details

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',
    instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created',
    instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

    def amount_to_raise(self, instance):
        sum_of_pledges = instance.pledges.aggregate(Sum('amount'))['amount__sum']
        amount_to_go = instance.goal - sum_of_pledges
        return amount_to_go