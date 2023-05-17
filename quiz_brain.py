class QuizBrain:

    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def next_question(self):

        current_question = self.question_list[self.question_number]

        guess = input(f"Q.{self.question_number +1}: {current_question.text} (True/False)?: ").title()
        if guess == "End":
            return False
        elif guess == current_question.answer:
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {current_question.answer}.")
        print(f"Your current score is {self.score}/{self.question_number + 1}.\n\n")
        if self.question_number < len(self.question_list) - 1:
            self.question_number += 1
            return True
        else:
            print("That was the last question!")
            return False
