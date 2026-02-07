import random
questions = {
    "What function is used to output text in Python?": "print()",
    
    "Which keyword defines a function in Python?": "def",
    
    "What is the data type of True and False?": "boolean",
    
    "Which character is used to start a single-line comment?": "#",
    
    "What method removes whitespace from the start/end of a string?": "strip()",
}


def quiz_game():
    question_list = list(questions.keys())
    total_questions = 5
    score = 0
    selected_question = random.sample(question_list,total_questions)
 
    for idx , question in enumerate(selected_question):
        print(f"{idx+1}.{question}")
        user_answer = input("Enter your answer : ").lower().strip()
        correct_answers = questions[question]
        if user_answer == correct_answers.lower():
            print("Correct Answer ! \n")
            score += 1
        else:
            print(f"Wrong ! The correct answer is: {correct_answers}.\n")
    
    print(f"Your score is: {score}/{total_questions}") 


quiz_game()




