from DataLoader import DataLoader
from ModeloLinear import ModeloLinear
from ModeloKNN import ModeloKNN
from Evaluetor import Evaluator
from Results import Results
from Menu import Menu

class Main:
    def __init__(self, filepath, features, target):
        self.filepath = filepath
        self.features = features
        self.target = target
        
        self.data_load = DataLoader(self.filepath)
        
        escolha_modelo = Menu()
        
        modelo, n_neighbors = escolha_modelo.escolha_modelo()
        
        if modelo == 'Linear':
            self.model = ModeloLinear()
        else:
            self.model = ModeloKNN(n_neighbors=n_neighbors)
            
        self.evaluetor = Evaluator()
        self.display = Results()
        
    def run(self):
        self.data_load.loader()
        self.data_load.preprocess(self.features, self.target)
        
        self.model.train(self.data_load.X_train, self.data_load.Y_train)
        predictions = self.model.predict(self.data_load.X_test)
        r2, mse, mae = self.evaluetor.evalue(self.data_load.Y_test, predictions)
        
        if isinstance(self.model, ModeloLinear):
            coefficeints, intercept = self.model.coefficients()
            self.display.display_results(self.model, self.data_load.Y_test, predictions, self.features, r2, mse, mae, coefficeints, intercept)
        else:
            self.display.display_results(self.model, self.data_load.Y_test, predictions,self.features, r2, mse, mae)

if __name__ == "__main__":
    filepath = r"C:\Users\modes\Documents\VScode\Python\IA\Trabalho_1_Modesto_Pereira_Lima_Verde_Neto\ConsumoCo2.csv"
    features = ['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB']
    target = 'CO2EMISSIONS'
    
    main_process = Main(filepath, features, target)
    
    main_process.run()