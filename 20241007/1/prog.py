def Pareto(*pairs):
  res = []
  for pair1 in pairs:
    is_dominated = False
    for pair2 in pairs:
      if pair1 != pair2 and pair1[0] <= pair2[0] and pair1[1] <= pair2[1] and (pair1[0] < pair2[0] or pair1[1] < pair2[1]):
        is_dominated = True
        break
    if not is_dominated:
      res.append(pair1)

  return tuple(res)

data = eval(input())
print(Pareto(*data))
