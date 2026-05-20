import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_data(file_path):
    data = pd.read_excel(file_path)
    X = data['X'].values.reshape(-1, 1)
    Y = data['Y'].values.reshape(-1, 1)
    return X, Y


def normalize_feature(X):
    return (X - np.mean(X)) / np.std(X)


def compute_cost(X, Y, theta, bias):
    m = len(Y)
    predictions = X.dot(theta) + bias
    error = predictions - Y
    return (1 / (2 * m)) * np.sum(error ** 2)


def gradient_descent(X, Y, learning_rate=0.01, iterations=1000):
    m = len(Y)
    theta = np.random.randn(1, 1)
    bias = 0.0
    cost_history = []

    for i in range(iterations):
        predictions = X.dot(theta) + bias
        error = predictions - Y

        d_theta = (1 / m) * X.T.dot(error)
        d_bias = np.mean(error)

        theta -= learning_rate * d_theta
        bias -= learning_rate * d_bias

        cost_history.append(compute_cost(X, Y, theta, bias))

    return theta, bias, cost_history


def plot_regression(X_raw, Y, X_norm, theta, bias, cost_history):
    predictions = X_norm.dot(theta) + bias

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.scatter(X_raw, Y, color='blue', label='Data')
    plt.plot(X_raw, predictions, color='red', label='Regression line')
    plt.title('Linear Regression Fit')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(range(1, len(cost_history) + 1), cost_history, color='green')
    plt.title('Cost over iterations')
    plt.xlabel('Iteration')
    plt.ylabel('Cost')

    plt.tight_layout()
    plt.show()


def main():
    file_path = './data/Module_1_Assignment_Spreadsheet.xlsx'
    X_raw, Y = load_data(file_path)
    X_norm = normalize_feature(X_raw)

    theta, bias, cost_history = gradient_descent(X_norm, Y, learning_rate=0.01, iterations=1000)

    print('Manual Gradient Descent Results')
    print('---------------------------------')
    print(f'Coefficient (theta): {theta.item():.6f}')
    print(f'Intercept (bias): {bias:.6f}')
    print(f'Final cost: {cost_history[-1]:.6f}')

    plot_regression(X_raw, Y, X_norm, theta, bias, cost_history)


if __name__ == '__main__':
    main()

