def insertion_sort(ll):
  rr = [ll[0]]

  for l in ll[1:]:
    for i, r in enumerate(rr):
      if l < r:
        rr.insert(i, l)
        break

      if i == len(rr) - 1:
        rr.append(l)
        break

  return rr
