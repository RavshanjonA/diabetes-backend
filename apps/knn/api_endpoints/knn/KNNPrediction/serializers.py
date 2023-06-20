from rest_framework import serializers

class InputSerializer(serializers.Serializer):
    Pregnancies = serializers.IntegerField()
    Glucose = serializers.FloatField()
    BloodPressure = serializers.FloatField()
    SkinThickness = serializers.FloatField()
    Insulin = serializers.FloatField()
    BMI = serializers.FloatField()
    DiabetesPedigreeFunction = serializers.FloatField()
    Age = serializers.IntegerField()