def primo(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

MAX = 100

for j in range(2,MAX + 1):
    if primo(j) == True :
        print(j)