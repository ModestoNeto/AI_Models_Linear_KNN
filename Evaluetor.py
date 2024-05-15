from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

class Evaluator:
    @staticmethod
    def evalue(Y_true, Y_pred):
        r2 = r2_score(Y_true, Y_pred)
        mse = mean_squared_error(Y_true, Y_pred)
        mae = mean_absolute_error(Y_true, Y_pred)
        
        print(f"Resultados - R² score: {r2}, MSE: {mse}, MAE: {mae}")
        
        return r2, mse, mae