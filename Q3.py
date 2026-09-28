import math

def MSE(Actual, Predicted):

    Sum = 0

    for i in range(len(Actual)):

        Error = Actual[i] - Predicted[i]

        Sum = Sum + (Error * Error)

    Loss = Sum / len(Actual)

    return Loss


def BCE(Actual, Predicted):

    Sum = 0

    for i in range(len(Actual)):

        Loss = -(Actual[i] * math.log(Predicted[i]) +(1 - Actual[i]) * math.log(1 - Predicted[i]))

        Sum = Sum + Loss

    Loss = Sum / len(Actual)

    return Loss


def main():

    Actual = [1, 0, 1, 1]

    Predicted = [0.9, 0.2, 0.8, 0.7]

    MSELoss = MSE(Actual, Predicted)

    BCELoss = BCE(Actual, Predicted)

    print("Mean Squared Error:", MSELoss)

    print("Binary Cross Entropy:", BCELoss)

    print("\nMSE is mainly used for Regression.")

    print("BCE is mainly used for Binary Classification.")


if __name__ == "__main__":
    main()