# 🔐 Password Strength Checker

A **Python GUI application** that evaluates the strength of user-entered passwords using **regular expressions (Regex)** and a **score-based system**. Built with Tkinter, the tool provides real-time feedback, a visual strength bar, and helpful suggestions to create stronger, more secure passwords.

---

## 🚀 Features

- ✅ Real-time password evaluation
- 🎯 Score-based strength rating (0 to 5)
- 🌈 Color-coded strength bar (Very Weak to Ultra Secure)
- 💬 Feedback to help improve weak passwords
- 🖥 Simple and intuitive Tkinter GUI
- 🛠 No external dependencies – runs on standard Python

---

## 📊 Password Strength Criteria

The password is evaluated based on the following rules:

| Criteria                            | Score |
|-------------------------------------|-------|
| At least **8 characters**           | +1    |
| Contains **uppercase letters**      | +1    |
| Contains **lowercase letters**      | +1    |
| Contains **numbers**                | +1    |
| Contains **special characters**     | +1    |

### 💡 Final strength levels:
- **0** – Very Weak 😞
- **1** – Weak 😟
- **2** – Medium 😐
- **3** – Strong 🙂
- **4** – Very Strong 💪
- **5** – Ultra Secure 🚀

---

## 🧪 How to Run

1. Ensure you have **Python 3.x** installed.
2. Save the script as `password_checker.py`.
3. Run the script from your terminal or command prompt:

bash
python password_checker.py
`

> 💡 No additional libraries are required – it uses only Python’s built-in `tkinter` and `re` modules.

---

## 📁 File Structure


password-strength-checker/
├── LICENSE
├── README.md
└── password_checker.py


---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgments

This tool was developed as part of my **Skill Craft Cybersecurity Internship** to practice password validation, Regex, and secure user input handling.

---
