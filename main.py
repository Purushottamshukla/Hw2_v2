# Author: Purushottam Shukla pps5338@psu.edu
def getGradePoint(letter):
  table={"A":4.0,"A-":3.67,"B+":3.33,"B":3.0,"B-":2.67,"C+":2.33,"C":2.0,"D":1.0,"F":0.0}
  try:
    score = table[letter]
  except KeyError: 
      score = 0.0
  else:
      score = table[letter]
  return score

def run():
  gpa = 0
  totalcred = 0
  for i in range(3):
    letter = input(f"Enter your course {i+1} letter grade: ")
    letter = letter.upper()
    Credit = input(f"Enter your course {i+1} credit: ")
    print(f"Grade point for course {i+1} is: {getGradePoint(letter)}")
    try:
      float(Credit)
    except ValueError:
      print('Credit must be represented as a number.')
      quit()
    else:
      gpa+=(float(Credit)*getGradePoint(letter))
      totalcred+=float(Credit)
  print(f"Your GPA is: {gpa/totalcred}")

if __name__ == '__main__':
  run()