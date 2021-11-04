def is_prime(n):
    """"pre-condition: n is a nonnegative integer
    post-condition: return True if n is prime and False otherwise."""
    if n < 2: 
         return False;
    if n % 2 == 0:             
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True


n=55
while n < 100:
  pot_prime = 2**n-1
  print(n,':',pot_prime,'is', is_prime(pot_prime))
  n+=1
#endwhile

