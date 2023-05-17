from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(element["text"], element["answer"]) for element in question_data]

quiz_brain = QuizBrain(question_bank)

keep_playing = True

while keep_playing:
    keep_playing = quiz_brain.next_question()

