import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1], [2], [3]])
y = np.array([3, 5, 7])

model = LinearRegression()
model.fit(x, y)

print(model.predict([[4]]))
