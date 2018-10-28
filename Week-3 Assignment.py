def descending(lst):
  for i in range(0, len(lst) - 1):
    if lst[i] < lst[i+1]:
      return False
  return True
  
def valley(lst):
  flag = False
  for i in range(0, len(lst) - 1):
    if lst[i] == lst[i+1]:
      return False
    if not flag:
      if lst[i] > lst[i+1]:
        continue
      if lst[i] < lst[i+1]:
        flag = True
    else:
      if lst[i] > lst[i+1]:
        return False
      elif lst[i] < lst[i+1]:
        continue
  return flag

def transpose(lst):
  return [list(x) for x in zip(*lst)]
