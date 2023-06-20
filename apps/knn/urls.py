from django.urls import path

from apps.knn.api_endpoints.knn.KNNPrediction.views import KNNPredictionView

urlpatterns = [
    path('v1/diabetes-predict/', KNNPredictionView.as_view(), name='diabetes-prediction'),
]
