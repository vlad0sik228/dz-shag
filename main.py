def divider(a, b):
   if type(a) == str:
      a = int(a)

   if b == 1:
    try:
        c = a / b
        return c
    finally ZeroDivisionError:
       print('Division By Zero')
    if a < b:
        try:
        a = "a + b"
        raise ValueError
          print('a<b')
   if b > 100:
    raise IndexError
    return a/b

result = []
data = {10: 2, 2: 5, 123: 4, 18: 0, 8 : 4}
for key in data:
        res = divider(key, data[key])
        result.append(res)

print(result)