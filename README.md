 📝 To-Do List (Beginner Friendly)

A simple command-line To-Do List Manager built with Python.
I started this project as part of my **100 Days Python Logic Challenge** (from Day 47 onwards) and kept adding features step by step until it became a more polished version.

This project is **perfect for beginners** who want to learn about:

* Functions
* File handling (`open`, read, write)
* Dictionaries & lists
* Error handling (`try-except`)
* Modular coding (splitting logic into functions)

---

## 🚀 Features

✅ Add a task with a category
✅ View all tasks (grouped by category)
✅ Remove a task by number
✅ Mark a task as **completed**
✅ Save tasks to a file (`tasks.txt`) so they don’t disappear after closing
✅ Load tasks back from the file on restart

---

## 📂 Project Structure

```
todo.py       # Main program
tasks.txt     # File where all tasks are saved (auto-created)
```

---

 🖥️ How to Run

1. Make sure you have **Python 3.x** installed.
2. Save the code as `todo.py`.
3. Open a terminal/command prompt in the same folder and run:

   ```bash
   python todo.py
   ```
4. Follow the menu to manage your tasks.

---

## 🧑‍💻 Example Usage

```
 ----TO DO LIST-----
A. Add a task
B. View all tasks
C. Remove task by number
D. Mark task as completed
E. Exit
```

* Add a new task:

  ```
  Enter new task: Buy groceries
  Enter category for the task: Personal
  Task added: Buy groceries in category 'Personal'
  ```

* Mark it completed:

  ```
  Task 'Buy groceries' marked as completed.
  ```

* Exit:

  ```
  Goodbye!
  ```

---

## 📘 What I Learned

* How to use **dictionaries with lists** (`setdefault`)
* How to **persist data** using files (`tasks.txt`)
* How to **map menu numbers to tasks** using a dictionary
* How to structure a **modular Python program**

---

## 🔮 Future Improvements

* Add **due dates** for tasks
* Add **priority levels** (High/Medium/Low)
* Option to **edit a task** instead of only removing
* GUI version (Tkinter or web app)

---

## 🌟 Why Share This?

I built this as a **practice project**, but I’m sharing it so that other **new learners** can:

* Read clean, beginner-friendly code
* Learn step by step how small projects evolve
* Get inspired to build their own versions 🚀

---

✨ Feel free to fork this project, suggest improvements, or use it as your starting point!

---

Do you want me to also **add commit history style notes** in the README (like “Day 47 → Added file saving, Day 48 → Added categories…”), so new learners can see the growth journey? That would make it extra inspiring for beginners.
