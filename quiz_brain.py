class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def has_next(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, actual_answer):
        if user_answer.lower()[0] == actual_answer.lower()[0]:
            self.score += 1
            print(f"Correct! Score: {self.score}/{len(self.questions_list)}")
        else:
            self.score += 0
            print(f"The answer was {actual_answer}! Score: {self.score}/{len(self.questions_list)}")

    def next_question(self):
        if self.has_next():
            question = self.questions_list[self.question_number]
            self.question_number += 1
            answer = input(f"\nQ{self.question_number}. {question.text} (True/False): ")
            self.check_answer(answer, question.answer)
