from catboost import CatBoostRegressor
import pandas as pd
from flask import Flask, request, jsonify
import json


def preproc_data(df_input):
    '''includes several functions to pre-process the predictor data.'''

    df_output = df_input.copy()

    # ################### Предобработка ##############################################################
    # убираем не нужные для модели признаки
    df_output.drop(['Таможня', 'Состояние', 'id'], axis=1, inplace=True, )

    # ################### fix ##############################################################
    # Переводим признаки из float в int (иначе catboost выдает ошибку)
    for feature in ['modelDate', 'numberOfDoors', 'mileage', 'productionDate']:
        df_output[feature] = df_output[feature].astype('int32')

    # ################### Feature Engineering ####################################################
    # тут ваш код на генерацию новых фитчей

    # ################### Clean ####################################################
    # убираем признаки которые еще не успели обработать,
    df_output.drop(['Комплектация', 'description', 'Владение'], axis=1, inplace=True)

    return df_output

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    X_json = request.get_json()
    X = pd.DataFrame(json.loads(X_json), index=[0])
    X = preproc_data(X)
    return jsonify({'prediction': model.predict(X)[0]})

if __name__ == '__main__':
    model = CatBoostRegressor()
    model.load_model('catboost_single_model_baseline.model')
    app.run('0.0.0.0')