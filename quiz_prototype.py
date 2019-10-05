import sys,time,random

typing_speed = 25 
def rint(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ("")

questions = ["What is 1 + 1",
             "What is the currency of India?",
             "True or False... Delhi is capital of India?",
             "What was the last year India won Cricket World cup?",
             "True or False... The current Prime Minister of India is Modi?"]
answer_choices = ["a)1\nb)2\nc)3\nd)4\n:",
                  "a)Dollar\nb)Euro\nc)Ruppee\nd)Brady\n:",
                  ":",
                  "a)1998\nb)2018\nc)2202\nd)2011\n:",
                  ":"]
correct_choices = [{"b", "2"},
                   {"c", "Ruppee"},
                   {"true", "t"},
                   {"d", "2011"},
                   {"true", "t"}]
answers = ["1 + 1 is 2",
           "Ruppee is the only currency of India",
           "",
           "The last time India won the Cricket World cup was 2011",
           "The current Prime Minster of India is Modi"]


def quiz():
    print("\n")
    print("Welcome to the Quiz\n")
    print("Let's begin the Quiz\n")
    print("\n")


    score = 0
    for question, choices, correct_choice, answer in zip(questions, answer_choices, correct_choices, answers):
        print(question)
        user_answer = input(choices).lower()
        if user_answer in correct_choice:
            rint("Correct\n")
            score += 1
        else:
            print("Incorrect", answer,"\n")
    print(score, "out of", len(questions), "that is", float(score / len(questions)) * 100, "%\n")
    rint("END OF QUIZ\n")
if __name__ == "__main__":
    quiz()