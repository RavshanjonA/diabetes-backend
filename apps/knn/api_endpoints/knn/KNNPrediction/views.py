from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import KNNPredictionSerializer
import numpy as np

from ...service.models import KNNModel
from .schemas import prediction_request_body, prediction_response, bad_request_response

class KNNPredictionView(APIView):
    @swagger_auto_schema(
        request_body=prediction_request_body,
        responses={
            200: openapi.Response(
                description='Successful prediction',
                schema=prediction_response,
            ),
            400: openapi.Response(
                description='Bad Request',
                schema=bad_request_response,
            ),
        },
    )
    def post(self, request):
        serializer = KNNPredictionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        input_data = serializer.validated_data
        data_array = np.array([list(input_data.values())])

        knn_model = KNNModel()
        prediction = knn_model.predict(data_array)

        return Response({'prediction': prediction})
