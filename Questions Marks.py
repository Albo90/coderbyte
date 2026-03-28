def QuestionsMarks(strParam):
  questions_count = 0
  first = -1
  second = -1
  ok_count = 0

  for item in strParam:
    if item.isdigit():
      if first == -1:
        first = int(item)
        questions_count = 0
      else: 
        second = int(item)
    if item == "?":
      questions_count+=1
    if first != -1 and second != -1:
          pair_sum = first + second
          first = second
          second = -1  
          if pair_sum == 10:
            if questions_count != 3:
              return "false"  
            questions_count = 0
            ok_count+=1
  
  return "true" if ok_count > 0 else "false"            



  # code goes here
  return strParam

# keep this function call here 
print(QuestionsMarks(input()))