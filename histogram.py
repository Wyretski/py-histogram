a = (0, 1, 1, 1, 2, 5)

def count_elements(seq) -> dict:
  hist = {}
  for i in seq:
    hist[i] = hist.get(i, 0) + 1
  return hist

counted = count_elements(a)
print(counted)

##def ascii_histogram(seq) -> None:
  ##counted  = count_elements(seq)
