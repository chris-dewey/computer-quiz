from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def play():
    question_bank = []
    for question in question_data:
        question_bank.append(Question(question["text"], question["answer"]))

    quiz = QuizBrain(question_bank)

    while quiz.has_next():
        quiz.next_question()

    print("You have reached the end of the list!")
    print(f"You scored: {quiz.score}!")

    if input("Play again?").lower()[0] == 'y':
        play()
    else:
        print("Thanks for playing!")


play()
