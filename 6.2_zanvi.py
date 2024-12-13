from tkinter import *

# Question Data
questions = [

    {"q": "What is 5+5?", "a": "10"},
    {"q": "What is the square root of 100?", "a": "10"},
    {"q": "Is 5i+3j a complex number?", "a": "Yes"},
    {"q": "What is the smallest prime number?", "a": "2"},
    {"q": "Calculate x+y=7 where y=5", "a": "2"}
]

# Initialize global variables
current_question = 0
score = 0
def check_answer():
    global current_question, score

    # Get user answer
    user_answer = answer_entry.get().strip()
    correct_answer = questions[current_question]['a']

    # Check correctness
    if user_answer.lower() == correct_answer.lower():
        feedback_label.config(text="Correct! :>", fg="green")
        score += 5
    else:
        feedback_label.config(text=f"Incorrect! :< The correct answer was {correct_answer}", fg="red")
        score -= 2

    # Clear entry box
    answer_entry.delete(0, END)

    # Move to next question or end quiz
    current_question += 1
    if current_question < len(questions):
        load_question()
    else:
        end_quiz()


def load_question():
    """Load the next question."""
    question_label.config(text=f"Question {current_question + 1}: {questions[current_question]['q']}")
    feedback_label.config(text="")


def end_quiz():
    """Display the final score and end the quiz."""
    total_marks_possible = len(questions) * 5
    passing_scope = total_marks_possible * 0.6

    # Clear the screen
    question_label.config(text="")
    feedback_label.config(text="")
    answer_entry.destroy()
    submit_button.destroy()

    # Display final score and result
    result_label = Label(root, text=f"Your final score is: {score}/{total_marks_possible}", font=("Arial", 14),
                         bg="bisque")
    result_label.pack(pady=20)

    if score >= passing_scope:
        pass_label = Label(root, text="Well done! You have passed the quiz!", font=("Arial", 14), fg="black",
                           bg="bisque")
        pass_label.pack()
    else:
        fail_label = Label(root, text="Sorry! You didn't pass the quiz, better luck next time!", font=("Arial", 14),
                           fg="black", bg="bisque")
        fail_label.pack()


# Initialize main window
root = Tk()
root.title("Simple Quiz")
root.geometry("500x350")
root.configure(bg="darkseagreen1")

# Question Label
question_label = Label(root, text="", font=("Arial", 14), bg="darkseagreen1", wraplength=450, justify="center")
question_label.pack(pady=20)

# Answer Entry
answer_entry = Entry(root, font=("Arial", 14))
answer_entry.pack(pady=10)

# Submit Button
submit_button = Button(root, text="Submit Answer", font=("Arial", 14), command=check_answer)
submit_button.pack(pady=10)

# Feedback Label
feedback_label = Label(root, text="", font=("Arial", 12), bg="darkseagreen1")
feedback_label.pack(pady=10)

# Load the first question
load_question()

# Run the quiz
root.mainloop()