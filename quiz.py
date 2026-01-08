import random

quiz={"Who is the current President of India?":"Droupadi Murmu",
           "Which country hosted the FIFA World Cup 2022?":"Qatar",
           "Which country launched the James Webb Space Telescope?":"United States",
           "Which country won the ICC Cricket World Cup 2019?":"England",
           "In which sport is the term 'love' used for scoring?":"Tennis",
           "Which programming language is known as the language of the web?":"JavaScript",
           "Python was created by which developer?":"Guido van Rossum"}

options=[
    ["Ram Nath Kovind","Droupadi Murmu","Pranab Mukherjee","Manmohan Singh"],
    ["Qatar","Brazil","Germany","France"],
    ["England","Australia","United States","China"],
    ["India","Australia","New Zealand","England"],
    ["Cricket","Tennis","Football","Hockey"],
    ["Python","Java","C++","JavaScript"],
    ["Guido van Rossum","James Gosling","Dennis Ritchie","Bjarne Stroustrup"]
]


index=list(range(len(quiz)))
random.shuffle(index)

score=0

questions=list(quiz.keys())
answers=list(quiz.values())

for i in index:
    print("\n"+questions[i])
    opts=options[i].copy()
    random.shuffle(opts)

    print("1. ",opts[0])
    print("2. ",opts[1])
    print("3. ",opts[2])
    print("4. ",opts[3])

    while True:
        your_answer=input("Enter your answer (1-4): ")
        if your_answer in ["1","2","3","4"]:
            your_answer=int(your_answer)
            if(opts[your_answer-1]==answers[i]):
                print("Correct!")
                score+=1
            else:
                print("Wrong! The correct answer is",answers[i])
            break;
        else:
            print("Please eneter a valid number between 1 to 4.")
print("\n Your final score is",score,"out of",len(quiz))
