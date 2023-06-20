from drf_yasg import openapi

prediction_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'Pregnancies': openapi.Schema(type=openapi.TYPE_INTEGER, description='Number of Pregnancies'),
        'Glucose': openapi.Schema(type=openapi.TYPE_INTEGER, description='Glucose level'),
        'BloodPressure': openapi.Schema(type=openapi.TYPE_INTEGER, description='Blood Pressure'),
        'SkinThickness': openapi.Schema(type=openapi.TYPE_INTEGER, description='Skin Thickness'),
        'Insulin': openapi.Schema(type=openapi.TYPE_INTEGER, description='Insulin level'),
        'BMI': openapi.Schema(type=openapi.TYPE_NUMBER, description='Body Mass Index'),
        'DiabetesPedigreeFunction': openapi.Schema(type=openapi.TYPE_NUMBER, description='Diabetes Pedigree Function'),
        'Age': openapi.Schema(type=openapi.TYPE_INTEGER, description='Age'),
    }
)

prediction_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'prediction': openapi.Schema(type=openapi.TYPE_STRING, description='Prediction result'),
    },
)

bad_request_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'Pregnancies': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
        'Glucose': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
        'BloodPressure': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
        'SkinThickness': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
        'Insulin': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
        'BMI': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
        'DiabetesPedigreeFunction': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
        'Age': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
    },
)
