import random

questions = {
    # Original 15
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
    "If a list has 5 elements, what is its last index number?": "4",

    # Additional 15
    "Which keyword is used to create a class in Python?": "class",
    "What function is used to display output on the screen?": "print",
    "Which data type is used to store True or False values?": "bool",
    "What keyword is used to handle exceptions in Python?": "try",
    "If x = [1,2,3], what does len(x) return?": "3",
    "What is the result of 15 % 4?": "3",
    "What function converts text to uppercase?": "upper",
    "Which built-in function gives the largest value in a list?": "max",
    "Which operator is used for exponentiation in Python?": "**",
    "What is the output of 3 + 2 * 2?": "7",
    "What is used to store multiple items in a single variable?": "list",
    "Which keyword is used to skip the rest of the current loop iteration?": "continue",
    "What keyword is used to exit a function and optionally return a value?": "return",
    "If x = 5, what is the value of x += 3?": "8",
    "What will print(type('Hello')) display?": "<class 'str'>"
}

def python_Quiz_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    select_questions = random.sample(questions_list, total_questions)

    for idx, question in enumerate(select_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong the correct answer is: {correct_answer}.\n")
            if score >= 1:
                score -= 1
        
    print("!Game Over!")
    print(f"Score: {score} \ {total_questions}\n{(score / total_questions) * 100}%")

python_Quiz_game()