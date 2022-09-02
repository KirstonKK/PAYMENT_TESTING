def tailcall(f):
    def g(*args):
        while True:
            result = f(*args)
            if type(result) is tuple:
                args = result
            else:
                return result
    return g

def fact(n):
  if n == 0:
    return 1
  return fact(n-1, n* acc)
