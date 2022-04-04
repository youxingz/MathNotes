# 1. size|3,5,7,...| = (p(n+1) - p(n))/2
#

def read_primes(MAX_L):
  with open("./primes.txt", "r") as pfile:
    data = pfile.readlines()
    result = []
    for i in range(len(data)):
      if i == MAX_L:
        break
      item = data[i]
      kv = item.replace("\n", "").split(",")
      # result.append([int(kv[0]), int(kv[1])])
      result.append(int(kv[1]))
    return result

PRIMES = read_primes(1000)

def is_prime(n):
  return n in PRIMES

RESULTS = {}
for n in range(4, 1000, 2):
  RESULTS[''+str(n)] = []
  for p in PRIMES:
    if p > n / 2:
      break
    if is_prime(n - p):
      RESULTS[''+str(n)].append([p, n-p]) # = RESULTS[''+str(n)] + 1

for k in RESULTS:
  print(k, '\t', len(RESULTS[k]), '\t', RESULTS[k])
# print(RESULTS)