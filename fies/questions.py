import ipywidgets as widgets
from IPython.display import display

def display_question(question_text, options, correct_answer):
    display(widgets.Label(question_text))
    dropdown = widgets.Dropdown(
        options=options,
        description='Select:',
        disabled=False,
    )
    display(dropdown)
    
    def check_answer(change):
        if dropdown.value == correct_answer:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", correct_answer)

    dropdown.observe(check_answer, names='value')

def question_1():
    question_text = "What is the capital of France?"
    options = ["Paris", "London", "Berlin", "Rome"]
    correct_answer = "Paris"
    display_question(question_text, options, correct_answer)

def question_2():
    question_text = "Which of the following is not a programming language?"
    options = ["Python", "Java", "HTML", "C++"]
    correct_answer = "HTML"
    display_question(question_text, options, correct_answer)

def question_3():
    question_text = "What is the largest planet in our solar system?"
    options = ["Jupiter", "Mars", "Saturn", "Venus"]
    correct_answer = "Jupiter"
    display_question(question_text, options, correct_answer)

# Example usage:
question_1()
question_2()
question_3()
