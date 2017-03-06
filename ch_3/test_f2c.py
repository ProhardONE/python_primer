def C(f):
  return 5/float(9)* (f - 32)

def F(c):
  return 9/float(5)*c + 32

def test_Converter():
  functions = [C,F]
  value = 10
  tol = 1E-14
  i = 0
  for function in functions:
    exact = value
    approx = functions[i](functions[i-1](value))
    i += 1
    success = abs(exact - approx) < tol
    msg = 'Convert: %g   Exact: %g' % (approx, exact)
    assert success, msg
  
test_Converter()
