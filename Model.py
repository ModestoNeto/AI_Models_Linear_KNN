from abc import ABC, abstractclassmethod

class Model(ABC):
    @abstractclassmethod
    def train(self, x_train, y_train):
        pass
    
    @abstractclassmethod
    def predict (self, x_test):
        pass    