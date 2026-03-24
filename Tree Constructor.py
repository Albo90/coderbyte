import ast
from collections import defaultdict
def TreeConstructor(strArr):
  dic = defaultdict(list)
  s = set()
  no_radix = list()
  for item in strArr:
    pair = ast.literal_eval(item)
    l,r = pair
    dic[r].append(l)
    s.add(r)
    no_radix.append(l)
    if len(dic[r]) > 2:
      return "false"
  for item in no_radix:
    s.discard(item)    
  if len(s) > 1:
    return "false"    
  return "true"    


# keep this function call here 
print(TreeConstructor(input()))