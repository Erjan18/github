def a_n(a,n):
      if n == 0:
            return 1
      elif n > 0: return a*a_n(a,n-1)
      else: return 1/a*a_n(a,n+1)
a, n = int(input()), int(input())
print (a_n(a,n))