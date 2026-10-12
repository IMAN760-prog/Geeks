
data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

def ask_questions():
    correct = 0
    incorrect = 0
    wrong_answers = []

    for item in data:
        answer = input(item["question"] + " ")

        if answer.strip().lower() == item["answer"].lower():
            print("Correct!")
            correct += 1
        else:
            print("Incorrect!")
            incorrect += 1
            wrong_answers.append({
                "question": item["question"],
                "your_answer": answer,
                "correct_answer": item["answer"]
            })

    return correct, incorrect, wrong_answers


def show_results(correct, incorrect, wrong_answers):
    print("\nQuiz Results")
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)

    if wrong_answers:
        print("\nQuestions you answered incorrectly:")
        for item in wrong_answers:
            print("Question:", item["question"])
            print("Your answer:", item["your_answer"])
            print("Correct answer:", item["correct_answer"])
            print()

    if incorrect > 3:
        replay = input("You had more than 3 wrong answers. Play again? (yes/no): ")
        if replay.strip().lower() == "yes":
            main()


def main():
    correct, incorrect, wrong_answers = ask_questions()
    show_results(correct, incorrect, wrong_answers)


main()
