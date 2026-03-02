import tkinter as tk

root = tk.Tk()
root.title("Game")
root.geometry("800x500")
root.configure(bg="#6A0DAD")  # Deep purple
# Label
label = tk.Label(
    root,
    text="Current Number: 24000",
    bg="#6A0DAD",
    fg="white",
    font=("Arial", 14, "bold")
)
label.pack(pady=20)
# Button
btn2 = tk.Button(root, text="Divide by 2", bg="white", fg="black", font=("Arial", 12, "bold"), width=15, height=2)
btn3 = tk.Button(root, text="Divide by 3", bg="white", fg="black", font=("Arial", 12, "bold"), width=15, height=2)
btn4 = tk.Button(root, text="Divide by 4", bg="white", fg="black", font=("Arial", 12, "bold"), width=15, height=2)

btn2.pack(pady=10)
btn3.pack(pady=10)
btn4.pack(pady=10)

root.mainloop()