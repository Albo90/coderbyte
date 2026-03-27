def FindIntersection(strArr):
  first_item = list(map(int, strArr[0].split(", ")))
  second_item = list(map(int, strArr[1].split(", ")))
  intersection = [item for item in first_item if item in second_item]
  intersection.sort()
  res = ",".join(map(str,intersection)) if len(intersection) > 0 else "false"
  return res 
  

# keep this function call here 
print(FindIntersection(input()))