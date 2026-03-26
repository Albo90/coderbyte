def BracketMatcher(strParam):
  bracket_start = "("
  bracket_end = ")"
  res = 1
  while bracket_start in strParam or bracket_end in strParam  :
    index_start = strParam.find(bracket_start) 
    strParam = strParam.replace(bracket_start, "", 1)
    index_end = strParam.find(bracket_end) 
    strParam = strParam.replace(bracket_end, "", 1)
    if index_start == -1 or index_end == -1 or index_start > index_end:
      return 0
  return res


# keep this function call here 
print(BracketMatcher(input()))