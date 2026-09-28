import numpy as np
import matplotlib.pyplot as plt

def Sigmoid(x):

    return 1 / (1 + np.exp(-x))


def ReLU(x):

    return np.maximum(0, x)


def Tanh(x):

    return np.tanh(x)


def main():

    X = np.linspace(-10, 10, 100)
    Y1 = Sigmoid(X)
    Y2 = ReLU(X)
    Y3 = Tanh(X)
   
    plt.plot(X, Y1, label="Sigmoid")

    plt.plot(X, Y2, label="ReLU")
    
    plt.plot(X, Y3, label="Tanh")

    plt.xlabel("Input")
    plt.ylabel("Output")

    plt.title("Activation Functions")

    plt.legend()

    plt.grid()

    plt.show()


if __name__ == "__main__":
    main()