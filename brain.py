class QB:
    def __init__(self,qlist):
        self.qno=0
        self.queslist=qlist
        self.score=0
    def still_has_questions(self):
        return self.qno < len(self.queslist)
    def nextq(self):
        current=self.queslist[self.qno]
        self.qno+=1
        answer=input(f"Q.{self.qno}. {current.text} (True/False): ")
        self.check(answer, current.ans)
    def check(self,answer,correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.qno}")
        print("\n")