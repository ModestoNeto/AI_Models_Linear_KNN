import pandas as pd
from sklearn.model_selection import train_test_split

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None
        self.X_train = None
        self.X_test = None
        self.Y_train = None
        self.Y_test = None
        
    def loader(self):
        self.data = pd.read_csv(self.filepath)
        print("Leitura concluida")
        
    def preprocess(self, fetures, target, test_size=0.3, random_state=42):
        if self.data is None:
            raise ValueError("Dados não existentes, forneça os dados antes")
        
        X = self.data[fetures]
        Y = self.data[target]
        
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split( X, Y, train_size=test_size, random_state=random_state)
        
        print("Dados processados")
        
    