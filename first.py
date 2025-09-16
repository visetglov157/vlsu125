
def m(x, a, b, k):
    result = (1000 * abs(x * k) / (a + b)) ** (1/3)
    return result
print('input x, a, b, k')
x = float(input())
a = float(input())
b = float(input())
k = float(input())
print('result', m(x, a, b, k))
