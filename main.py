try:
    import math
    import pandas as pd
except:
    print("Erro na importação de bibliotecas")

# Entendendo a regressão linear multipla #

"""
- Projetar o valor de uma variável (dependente), através de outras variáveis (independentes VIs);
- Investigar que varáveis se relacionam com uma variável de desfecho; 
- Investigar qual conjunto de variáveis traz melhor explicação para a variável de resultado
- Entender a relação entre o resultado e as variáveis de predição

Fórmula da reta: y = β0 + β1X + e
y -> valores de resultado
β0  -> é o valor do intercepto, que nos informa o valor de “y” quando “x” é zero
β1 -> determina a inclinação da tera
X -> são os valores da nossa variável preditora

Coef Angular: B = nE xi yi - Exi Eyi
               ---------------------
                   nE x²i - (Exi)²

Intercepto: A = Ey - BEx
           --------------
                 n 

"""

class estatistics:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        if not isinstance(y, pd.Series):
            raise TypeError("A variável não é do tipo 'DataFrame'.")
        
        if not isinstance(x, pd.Series):
            raise TypeError("A variável não é do tipo 'DataFrame'.")
        

    def sum(self, x, y, x2, y2, xy):
        self.sum_x = x.sum()
        self.sum_y = y.sum()
        self.sum_x2 = x2.sum()
        self.sum_y2 = y2.sum() 
        self.sum_xy = xy.sum()

        self.angular_coeficient(self.sum_x, self.sum_y, self.sum_x2, self.sum_y2, self.sum_xy, x, y)
        self.intercept(self.sum_y, self.sum_x, x)

    def mmq(self):
        x = self.x
        y = self.y
        
        # Calculo do x2, y2 e xy
        try:
            self.x2 = x ** 2
            self.y2 = y ** 2
            self.xy = x * y
        except:
            raise TypeError("Valores inválidos para o calculo do x², y², xy")
            
        self.sum(x, y, self.x2, self.y2, self.xy)


    def angular_coeficient(self, sum_x, sum_y, sum_x2, sum_y2, sum_xy, x, y):
        # Coef Angular: B = nE xi yi - Exi Eyi
        #               ---------------------
        #                  nE x²i - (Exi)²
        self.B = ((len(x) * sum_xy) - (sum_x * sum_y)) / ((len(x) * sum_x2) - (sum_x ** 2))

    
    def intercept(self, sum_y, sum_x, x):
        # Intercepto: A = Ey - BEx
        #            --------------
        #                   n 
        self.A = (sum_y - (self.B * sum_x)) / len(x)

    def simple_linear_regression(self):
        self.mmq()
        valor = input("Informe o valor a ser predito: ")


        try:
            self.x1 = int(valor)
        except ValueError:
            try:
                self.x1 = float(valor)
            except ValueError:
                self.x1 = None

        if not isinstance(self.x1, (int, float)):
            raise TypeError("O valor deve ser um número inteiro ou float.")
        else:
            self.y_regression = self.A + (self.B + self.x1)
            print(self.y_regression)

    def multiple_linear_regression(self):
        # Formula
        # y = B0 + B1 x1 + ... + Bn xn
        pass

valores = {
    'x': [1, 2, 3, 4, 5],
    'y': [3, 7, 5, 11, 14]
}

base = pd.DataFrame(valores)

estatistica = estatistics(base['x'], base['y'])
estatistica.simple_linear_regression()