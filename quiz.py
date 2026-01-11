import threading
import time

# ---------------- TIMER INPUT FUNCTION ----------------
def timed_input(prompt, timeout):
    answer = [None]

    def get_input():
        answer[0] = input(prompt)

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        print("\nTime's up!")
        return None
    return answer[0]

# ---------------- QUIZ QUESTIONS ----------------
questions = [
    {
        "questions": "Which country hosted the FIFA World Cup 2022?",
        "options": ["Qatar","Brazil","Germany","France"],
        "answer": "Qatar"
    },
    {
        "question": "Python was created by which developer?",
        "options": ["James Gosling", "Bjarne Stroustrup", "Dennis Ritchie", "Guido van Rossum"],
        "answer": "4"
    },
    {
        "question": "Who is the current President of India?",
        "options": ["Ram Nath Kovind", "Droupadi Murmu", "Pratibha Patil", "Narendra Modi"],
        "answer": "2"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["List", "Set", "Dictionary", "Tuple"],
        "answer": "4"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "2"
    }
]

# ---------------- MAIN QUIZ LOGIC ----------------
score = 0
TIME_LIMIT = 10  # seconds per question

print("\nWelcome to the Python Quiz Game!")
print("You have", TIME_LIMIT, "seconds for each question.\n")

for index, q in enumerate(questions, start=1):
    print(f"\nQuestion {index}: {q['question']}")

    for i, option in enumerate(q["options"], start=1):
        print(f"{i}. {option}")

    user_answer = timed_input("Enter your answer (1-4): ", TIME_LIMIT)

    if user_answer is None:
        print("Skipped (Timeout)")
    elif user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

# ---------------- FINAL SCORE ----------------
print("\nQuiz Finished!")
print("Your Score: score/len(questions)")

if score == len(questions):
    print("Excellent! Perfect score!")
elif score >= len(questions) // 2:
    print("Good job!")
else:
    print("Keep practicing!")
