import re
import tkinter as tk

def check_password_complexity(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("- Make the password at least 8 characters long")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("- Add at least one uppercase letter")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("- Add at least one lowercase letter")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("- Include at least one number")

    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        score += 1
    else:
        feedback.append("- Include at least one special character (!@#$%^&*...)")

    levels = {
        0: ("Very Weak 😞", "#d32f2f"),       # red
        1: ("Weak 😟", "#f57c00"),            # orange
        2: ("Medium 😐", "#fbc02d"),          # yellow
        3: ("Strong 🙂", "#388e3c"),          # green
        4: ("Very Strong 💪", "#1976d2"),     # blue
        5: ("Ultra Secure 🚀", "#7b1fa2")     # purple
    }

    strength, color = levels.get(score, ("Ultra Secure 🚀", "#7b1fa2"))
    return score, strength, color, feedback

def update_ui(event=None):
    password = password_var.get()
    score, strength, color, feedback = check_password_complexity(password)

    strength_label.config(text=f"Password Strength: {strength} (Score: {score}/5)", fg=color)

    for i in range(5):
        if i < score:
            blocks[i].config(bg=color, fg="white", text="█")
        else:
            blocks[i].config(bg="#ddd", text=" ")

    if feedback:
        feedback_text.config(state="normal")
        feedback_text.delete("1.0", "end")
        feedback_text.insert("end", "Suggestions to improve:\n" + "\n".join(feedback))
        feedback_text.config(state="disabled")
    else:
        feedback_text.config(state="normal")
        feedback_text.delete("1.0", "end")
        feedback_text.config(state="disabled")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("450x320")
root.resizable(False, False)

tk.Label(root, text="Enter your password:", font=("Arial", 12)).pack(pady=(15, 5))

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 14))
password_entry.pack(fill="x", padx=20)
password_entry.bind("<KeyRelease>", update_ui)

strength_label = tk.Label(root, text="Password Strength:", font=("Arial", 14, "bold"))
strength_label.pack(pady=(15, 5))

frame_blocks = tk.Frame(root)
frame_blocks.pack(pady=(0, 15))
blocks = []
for _ in range(5):
    block = tk.Label(frame_blocks, bg="#ddd", fg="white", width=3, height=2, bd=1, relief="solid", font=("Arial", 16, "bold"))
    block.pack(side="left", padx=4)
    blocks.append(block)

feedback_text = tk.Text(root, height=7, width=55, bg="#fff0f0", fg="#c0392b", font=("Arial", 11))
feedback_text.pack(padx=20, pady=(0, 15))
feedback_text.config(state="disabled")

update_ui()

root.mainloop()
