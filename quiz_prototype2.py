animals_questions = 'Animals Questions'
capitals_questions = 'Capitals Questions'
math_questions = 'Math Questions'

questions = [animals_questions, capitals_questions, math_questions]

quiz = {animals_questions: [("Cub is lions baby", True),
                        ("Another animals question", False),
                        ("Last animals question", False)],

        capitals_questions: [("Delhi is the capital city of India", True),
                         ("Another capitals question", True),
                         ("Last capitals question", False)],

        math_questions: [("20 is log 100 for base 10", False),
                     ("Another math question", True),
                     ("Last math question", False)]
}

result = {"Correct": 0, "Incorrect": 0}

def get_quiz_choice():
    while True:
        try:
            quiz_number = int(input('Choose the quiz you like\n1 for Animal Questions \n2 for Capital Questions \n3 for Math Questions \nYour choice:'))
        except ValueError:
            print ("Not a number, please try again\n")
        else:
            if 0 >= quiz_number or quiz_number > len(quiz):
                print ("Invalid value, please try again\n")
            else:
                return quiz_number


def get_answer(question, correct_answer):
    while True:
        try:
            print ("Q: {}".format(question))
            answer = int(input("1 for True\n0 for False\nThe answer: "))
        except ValueError:
            print ("Not a number, please try again\n")
        else:
            if answer is not 0 and answer is not 1:
                print( "Invalid value, please try again\n")
            elif bool(answer) is correct_answer:
                result["Correct"] += 1
                return True
            else:
                result["Incorrect"] += 1
                return False


choice = get_quiz_choice()
quiz_name = questions[choice - 1]
print ("\nYou chose the {}\n".format(quiz_name))
quiz_questions = quiz[quiz_name]
for q in (quiz_questions):
    print ("The answer is: {}\n".format(str(get_answer(q[0], q[1]))))
if user_answer in correct_answer:
            print("Correct")
            score += 1
else : print("Incorrect", answer)

print(score, "out of", len(questions), "that is", float(score / len(questions)) * 100, "%")

