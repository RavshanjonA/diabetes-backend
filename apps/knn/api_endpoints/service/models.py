from sklearn.neighbors import KNeighborsClassifier
from joblib import load

class KNNModel:
    def __init__(self):
        self.knn_model = load('apps/knn/api_endpoints/service/lregression_model.joblib')

    def predict(self, input_data):
        prediction = self.knn_model.predict(input_data)
        return prediction.item()