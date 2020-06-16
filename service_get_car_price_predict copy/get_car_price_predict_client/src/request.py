import requests
import pandas as pd
import numpy as np
import time

if __name__ == '__main__':
    df = pd.read_csv('test.csv').dropna()
    max_rand = df.shape[0] - 1
    #while True:
    #    try:
    json_str = df.iloc[np.random.randint(0, max_rand)].to_json(force_ascii=False, orient='index')
    r = requests.post('http://car_price_predict:5000/predict', json=json_str)
    print("Request: {}\nResponse:{}".format(json_str, r.json()['prediction']))
    time.sleep(2)
     #   except:
     #       print('Не удалось подключиться к серверу')
