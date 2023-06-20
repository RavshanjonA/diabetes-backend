from sklearn.neighbors import KNeighborsClassifier
from joblib import load

class KNNModel:
    def __init__(self):
        # Load the trained KNN model
        self.knn_model = load('knn_model.joblib')

    def predict(self, input_data):
        # Perform the prediction using the KNN model
        prediction = self.knn_model.predict(input_data)
        return prediction.item()