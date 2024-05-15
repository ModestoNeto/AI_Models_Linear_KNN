from sklearn.neighbors import KNeighborsRegressor

class ModeloKNN:
    def __init__(self, n_neighbors=10):
        self.model = KNeighborsRegressor(n_neighbors=n_neighbors)
        self.predictions = None
        
    def train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)
        print(f"Modelo teinado com k={self.model.n_neighbors}")
    
    def predict(self, X_test):
        self.predictions = self.model.predict(X_test)
        print("Previsões realizadas")
        return self.predictions