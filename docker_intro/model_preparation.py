from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
import pickle

X, y = load_diabetes(return_X_y=True)
regressor = LinearRegression()
regressor.fit(X,y)

model = pickle.dumps(regressor)
type(model), type(regressor)
regressor_from_bytes = pickle.loads(model)
regressor_from_bytes
with open('myfile.pkl', 'wb') as output:
       pickle.dump(regressor, output)