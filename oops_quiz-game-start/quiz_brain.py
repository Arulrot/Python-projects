
class Quizbrain:
    def __init__(self,q_list):
     self.question_number=0
     self.score=0
     self.question_list=q_list
    
    def still_question(self):
       if self.question_number <len(self.question_list):
          return True
       else:
          return  False
       

    def next_question(self):
       current_question=self.question_list[self.question_number]
       self.question_number+=1
       choice=input(f" \nQ.{self.question_number}: {current_question.text} (True/False) :").lower()
       self.check_answer(choice,current_question.answer)

    def check_answer(self,usr_ans,correct_ans):
        if usr_ans.lower()==correct_ans.lower():
            self.score+=1
            print("You got it Right!")
        else:
            print("That's a wrong Answer !")
        print(f"the correct answer is {correct_ans} .")
        print(f"Your current score is :{self.score}/{self.question_number}")