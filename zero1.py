import random

questions = {
    "What keyword is used to start a loop that repeats while a condition is true?": "while",
    "What is the value of 5 * 0 + 10?": "10",
    "Which symbol is used for comments in Python?": "#",
    "What keyword is used to define a block of code that runs only if a condition is true?": "if",
    "What is the data type of text in Python?": "string",
    "What will print(2 ** 3) output?": "8",
    "Which Python keyword is used to stop a loop early?": "break",
    "If x = 10, what is x // 3 equal to?": "3",
    "Which function is used to get input from a user?": "input",
    "What is 9 + 1 * 0 + 3?": "12",
    "What keyword is used to define a reusable block of code in Python?": "def",
    "Which operator checks if two values are equal?": "==",
    "What does len('ChatGPT') return?": "7",
    "Which keyword is used to import modules in Python?": "import",
    "If a list has 5 elements, what is its last index number?": "4"
}

def Quiz():
    #  this is getting all the keys from the dictionary in a list formate  
    questions_list = list(questions.keys())
    total_question = 5
    score = 0

    # randomly selection questions using a sample method passing two arguments the list and
    # the total number   
    selected_question = random.sample(questions_list, total_question)

    # still do not know how it works so more attention will do, Look at the variables 
    # idx, and question one is a number and the other is a string
    for idx, question in enumerate(selected_question):
        print(f"\n{idx + 1}. {question}")
        choice = input("Ans: ").lower().strip()
        # here too looks bit crazy how did it get all the dictionary key values
        correct_answer = questions[question]

        # conditional statement to check if the user choice is correct, we will add a score += 1
        if choice == correct_answer:
            print("Correct")
            score += 1
        # same logic but in revers mode to see if he or she is wrong
        if choice != correct_answer:
            print(f"The correct answer is {correct_answer}")
            if score >= 1:
                score -= 1
            
    # printing a statement for the user to see his total score and also in percentage
    print(f"Score: {score} \nPercentage: {(score / total_question) * 100}")

Quiz()