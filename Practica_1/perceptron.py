import random

class Perceptron:
    def _init_(self, num_inputs):
        self.weights = [random.uniform(-1,1) for _ in range(num_inputs)]
        self.bias = random.uniform(-1,1)
    
    def predict(self, inputs):
        activation = self.bias
        for i in range(len(inputs)):
            activation += inputs[i] * self.weights[i]
        return i if activation >= 0 else 0
    
    def train(self, inputs, target):
        output = self.predict(inputs)
        error = target - output
        self.bias += error
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i]

    def get_weights(self):
        return self.weights

    def save_weights(self, filename):
        with open(filename, "w") as f:
            f.write(f"(self.bias)\n")
            for w in self.weights:
                f.write(f"(w)\n")

    def load_weights(self, filename):
        with open(filename, "r") as f:
            self.bias = float(f.readline())        
            self.weights = [float(line) for line in f.readlines()]
            
    def get_weights(self):
         return self.weights
    
    def save_weights(self, filename):
         with open(filename, "w") as f:
            f.write(f"{self.bias}\n")
            for w in self.weights:
                f.write(f"{w}\n")
    
    def load_weights(self, filename):
        with open(filename, "r") as f:
            self.bias = float(f.readline())
            self.weights = [float(line) for line in f.readlines()]

                                  
try:
        Perceptron.load_weights("weights.txt")
except:
        print("No se pudieron cargar los pesos")
        print("Entrenando")
        for _ in range(1000):
            inputs = [0,0]
            Perceptron.train(inputs,0)
            inputs = [0,1]
            Perceptron.train(inputs,0)
            inputs = [1,0]
            Perceptron.train(inputs,0)
            inputs = [1,1]
            Perceptron.train(inputs,0) 
    
        Perceptron.save_weights("weights.txt")
        print("Este es el modelo entrenado:")
        print(Perceptron.get_weights())


print("Predicciones")
print([0,0], "*", Perceptron.predict([0,0]))
print([0,0], "*", Perceptron.predict([0,1]))
print([0,0], "*", Perceptron.predict([1,0]))
print([0,0], "*", Perceptron.predict([1,1]))