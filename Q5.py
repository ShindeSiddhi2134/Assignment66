def main():

    Input = 2

    Weight = 0.5

    Bias = 0.1

    Target = 1

    LearningRate = 0.1

    Prediction = (Input * Weight) + Bias

    print("Prediction:", Prediction)

    Error = Target - Prediction

    print("Error:", Error)

    OldWeight = Weight

    Weight = Weight + LearningRate * Error * Input

    print("Old Weight:", OldWeight)

    print("Updated Weight:", Weight)


if __name__ == "__main__":
    main()