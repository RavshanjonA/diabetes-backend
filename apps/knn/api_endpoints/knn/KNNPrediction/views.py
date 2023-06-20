from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import InputSerializer
import numpy as np

from ...service.models import KNNModel


class KNNPredictionView(APIView):
    def post(self, request):
        serializer = InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        input_data = serializer.validated_data
        data_array = np.array([list(input_data.values())])

        knn_model = KNNModel()
        prediction = knn_model.predict(data_array)

        return Response({'prediction': prediction})
