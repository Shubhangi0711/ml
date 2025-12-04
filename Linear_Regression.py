x = [1, 2, 3]
y = [3, 5, 7]

n = len(x)
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum([x[i] * y[i] for i in range(n)])
sum_x2 = sum([value * value for value in x])

m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
c = (sum_y - m * sum_x) / n

test_x = 4
pred_y = m * test_x + c

print(m)
print(c)
print(pred_y)
