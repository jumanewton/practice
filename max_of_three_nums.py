def max_of_two(x,y):
  if x>y:
    return x
  return y

def max_of_three(x, y, z):
  return max(z, max_of_two(x,y))

res = max_of_three(20, 4, 13)
print(res)

