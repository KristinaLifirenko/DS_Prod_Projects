import requests
import time

if __name__ == '__main__':
    r = requests.post('http://solution:5000/predict', json={'params': [1, 2, 1, 0.661212487096872]})
    print(r.status_code)

    if r.status_code == 200:
        print(r.json()['prediction'])
    else:
        print(r.text)
    time.sleep(2)