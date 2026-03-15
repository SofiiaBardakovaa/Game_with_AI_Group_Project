import tkinter as tk
import random

current_number = None

def generate_numbers():
    numbers = []
    while len(numbers) < 5:
        num = random.randint(20000, 30000)
        if num % 12 == 0:
            numbers.append(num)
    return numbers

def start_game():
    start_frame.pack_forget()
    numbers_frame.pack(pady=20)

def choose_number(num):
    global current_number
    current_number = num

    numbers_frame.pack_forget()
    game_frame.pack(pady=20)

    label.config(text=f"Current Number: {current_number}")

root = tk.Tk()
root.title("Game")

window_width = 1000
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="#6A0DAD")  # Deep purple

# START SCREEN

start_frame = tk.Frame(root, bg="#6A0DAD")
start_frame.pack(pady=20)

title = tk.Label(
    start_frame,
    text = "WELCOME",
    bg = "#6A0DAD",
    fg = "white",
    font = ("Arial", 40, "bold")
)
title.pack(pady=60)

start_btn = tk.Button(
    start_frame,
    text="Start the game!",
    bg="white",
    fg="black",
    font=("Arial", 17, "bold"),
    width=15,
    height=2,
    command=start_game
)
start_btn.pack(pady=40)

# 5 NUMBERS SCREEN

numbers_frame = tk.Frame(root, bg="#6A0DAD")

title = tk.Label(
    numbers_frame,
    text = "Choose a starting number",
    bg = "#6A0DAD",
    fg = "white",
    font = ("Arial", 20, "bold")
)
title.pack(pady=40)

numbers = generate_numbers()

button_frame = tk.Frame(numbers_frame, bg="#6A0DAD")
button_frame.pack(pady=20)

for i, num in enumerate(numbers):
    btn = tk.Button(
        button_frame,
        text=str(num),
        font=("Arial", 14, "bold"),
        width=13,
        height=4,
        command=lambda n=num: choose_number(n)
    )
    btn.grid(row=0, column=i, padx=10)

# GAME SCREEN

game_frame = tk.Frame(root, bg="#6A0DAD")

# Label
label = tk.Label(
    game_frame,
    text="Current Number: 0",
    bg="#6A0DAD",
    fg="white",
    font=("Arial", 17, "bold")
)
label.pack(pady=30)

# Button
btn2 = tk.Button(game_frame, text="Divide by 2", bg="white", fg="black", font=("Arial", 14, "bold"), width=15, height=2)
btn3 = tk.Button(game_frame, text="Divide by 3", bg="white", fg="black", font=("Arial", 14, "bold"), width=15, height=2)
btn4 = tk.Button(game_frame, text="Divide by 4", bg="white", fg="black", font=("Arial", 14, "bold"), width=15, height=2)

btn2.pack(pady=10)
btn3.pack(pady=10)
btn4.pack(pady=10)

root.mainloop()