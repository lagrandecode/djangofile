from rest_framework import serializers
from .models import Question, Responses, Result



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        models = Responses
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        models = Result
        fields = '__all__'
