questions=[
 {
 "question": "What is the capital of Australia?",
 "options":["a. sydney", "b. canberra", "c. melbourne", "d. adelaide"],
 "answer": "b"
 },
 {
 "question": "What is the capital of India?",
"options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
"answer": "b"
},
{
"question": "Which planet is known as the Red Planet?",
"options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
"answer": "c"
},
{
"question": "Who wrote the Ramayana?",
"options": ["A. Tulsidas", "B. Valmiki", "C. Kalidasa", "D. Ved Vyasa"],
"answer": "b"
},
{
"question": "What is the largest ocean on Earth?",
"options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
"answer": "c"
},
{
"question": "What is the largest planet in our solar system?",
"options": ["A. Earth", "B. Marsh","C. Jupitar","D. Venus"],
"answer": "c"

}

]

print(f"\nwelcome to KBC Game!")
levels=[1000,2000,3000,5000,10000,20000]
money=0
for i in range(len(questions)):
    question = questions[i]
    print(f"\nquestion for Rs. {levels[i]}:")
    print(question["question"])
    for option in question["options"]:
        print(option)

    reply = input("enter your answer (a/b/c/d): ")
    if reply.lower() == question["answer"]:
        print("correct answer!")
        money=levels[i]
    else:
        print("wrong answer!")
        break

print(f"\n your take home money is{money}")