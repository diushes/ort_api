from rest_framework import serializers

from theory.models import Category
from .models import Test, Question, Option


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    category_title = serializers.CharField(source='category.title', read_only=True)

    class Meta:
        model = Test
        fields = "__all__"
