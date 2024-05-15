class Results:
    
    @staticmethod
    def display_results(model, Y_test, predictions, features, r2, mse, mae, coefficients=None, intercept=None):
        print("\nResultados do Modelo:")
        if coefficients is not None and intercept is not None:
            Results.display_coefficients(coefficients, intercept, features)
        Results.display_predictions(Y_test, predictions)
        Results.display_metrics(r2, mse, mae)
    
    @staticmethod
    def display_coefficients(coefficients, intercept, features):
        print("\nCoenfficientes")
        for features, coef in zip(features,coefficients):
            print(f"{features}: {coef: .4f}")
        print(f"Interceptador: {intercept: .4f}")
    
    @staticmethod
    def display_predictions(Y_test, predictions, num_display=10):
        print("Valores atuais X Previstos")
        for actual, pred in zip(Y_test[:num_display], predictions[:num_display]):
            print(f"Atual: {actual: .2f}, Previsto: {pred: .2f}")
    
    @staticmethod
    def display_metrics(r2, mse, mae):
        print("\nMetricas de Avaliação")
        print(f"R²: {r2: .4f}")
        print(f"Mean Square Error: {mse: .2f}")
        print(f"Mean Absolute Error: {mae: .2f}")