from rest_framework.serializers import FloatField, IntegerField, Serializer


class KNNPredictionSerializer(Serializer):
    Pregnancies = IntegerField(label="Number of Pregnancies")
    Glucose = IntegerField(label="Glucose level")
    BloodPressure = IntegerField(label="Blood Pressure")
    SkinThickness = IntegerField(label="Skin Thickness")
    Insulin = IntegerField(label="Insulin level")
    BMI = FloatField(label="Body Mass Index")
    DiabetesPedigreeFunction = FloatField(label="Diabetes Pedigree Function")
    Age = IntegerField(label="Age")