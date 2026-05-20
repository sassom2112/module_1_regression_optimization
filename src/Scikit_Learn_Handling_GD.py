import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def load_data(file_path):
    data = pd.read_excel(file_path)
    X = data['X'].values.reshape(-1, 1)
    Y = data['Y'].values.reshape(-1, 1)
    return X, Y


def main():
    file_path = './data/Module_1_Assignment_Spreadsheet.xlsx'
    X, Y = load_data(file_path)

    model = LinearRegression()
    model.fit(X, Y)
    Y_pred = model.predict(X)

    mse = mean_squared_error(Y, Y_pred)
    r2 = r2_score(Y, Y_pred)

    print('scikit-learn Linear Regression Results')
    print('--------------------------------------')
    print(f'Coefficient (theta): {model.coef_[0, 0]:.6f}')
    print(f'Intercept (bias): {model.intercept_[0]:.6f}')
    print(f'Mean squared error: {mse:.6f}')
    print(f'R^2 score: {r2:.6f}')


if __name__ == '__main__':
    main()

