from sklearn.linear_model import LinearRegression

class ModeloLinear:
    def __init__(self):
        self.model = LinearRegression()
        self.predictions = None
        
    def train(self, X_train, Y_train):
        self.model.fit(X_train,Y_train)
        
        print("Treino concluido")
        
    def predict(self, X_test):
        self.predictions = self.model.predict(X_test)
        
        print("Predições realizadas")
        return self.predictions
    
    def coefficients(self):
        return self.model.coef_, self.model.intercept_