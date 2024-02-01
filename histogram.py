a = (0, 1, 1, 1, 2, 5)

def count_elements(seq) -> dict:
  hist = {}
  for i in seq:
    hist[i] = hist.get(i, 0) + 1
  return hist

counted = count_elements(a)
print(counted)

from collections import Counter

recounted = Counter(a)
print(recounted)

def ascii_histogram(seq) -> None:
  counted  = count_elements(seq)
  for k in sorted (counted):
    print("{0:5d} {1}".format(k "+" *counted[k]))
