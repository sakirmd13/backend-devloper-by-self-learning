# 🚀 Backend Developer Roadmap (Self Learning)

> A complete self-learning journey to become a Backend Developer from scratch — one night at a time! 🌙

![Progress](https://img.shields.io/badge/Progress-Day%207%20Complete-brightgreen)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Study](https://img.shields.io/badge/Study%20Time-10PM--1AM-orange)

---

## 👨‍💻 About This Repository

This repository contains my **daily notes, code practice, and projects** as I learn Backend Development from zero.

- 📅 **Started:** June 2026
- ⏰ **Study Time:** Every night 10 PM – 1 AM
- 🎯 **Goal:** Become a job-ready Backend Developer
- 🎓 **Education:** B.Tech (Computer Science & Engineering)
- 💪 **Motto:** *"Consistency beats talent when talent doesn't stay consistent."*

---

## 📚 Learning Progress

| Day | Topic | Folder | Status |
|-----|-------|--------|--------|
| 01 | Internet & Web Fundamentals | `Internet-and-Web` | ✅ Completed |
| 02 | Python Variables | `Variable` | ✅ Completed |
| 03 | Python Data Types | `DataType` | ✅ Completed |
| 04 | Python Conditions (if/elif/else) | `Condition` | ✅ Completed |
| 05 | User Input & f-Strings | `Input` | ✅ Completed |
| 06 | Python Loops (for, while) | `Loops` | ✅ Completed |
| 07 | Python Functions & Booleans | `Functions` | ✅ Completed |
| 08 | Lambda & String/List Methods | `Methods` | 🔄 In Progress |
| 09 | Python OOP Basics | `OOP` | ⏳ Coming Soon |
| 10 | File Handling | `FileHandling` | ⏳ Coming Soon |
| 11 | Exception Handling | `Exceptions` | ⏳ Coming Soon |
| 12 | Mini Project — Full App | `Projects` | ⏳ Coming Soon |

---

## 🗂️ Folder Structure

```
backend-devloper-by-self-learning/
│
├── 📁 Internet-and-Web/     # Day 01 - How internet works, HTTP, DNS, APIs
├── 📁 Variable/             # Day 02 - Variables, naming rules, scope
│   └── variable.py
├── 📁 DataType/             # Day 03 - All 14 Python data types
│   ├── datatype.py
│   ├── casting.py
│   └── number.py
├── 📁 Condition/            # Day 04 - if, elif, else, logical operators
│   └── if_else_if.py
├── 📁 Input/                # Day 05 - input(), f-strings, type conversion
│   └── input.py
├── 📁 Loops/                # Day 06 - for loop, while loop, games
│   ├── for_loop.py
│   ├── while_loop.py
│   ├── number_guessing_game.py
│   ├── number_adding_game.py
│   └── math_game.py
├── 📁 Functions/            # Day 07 - Functions, booleans
│   ├── functions.py
│   └── booleans.py
├── 📁 Hello/                # First Python program
│   └── hello.py
└── 📄 README.md             # This file
```

---

## 🎮 Projects Built So Far

| Project | Concepts Used | Status |
|---------|--------------|--------|
| 🎯 Number Guessing Game | random, while, if/elif/else, break | ✅ Built |
| ➕ Number Adding Game | random, while, break, .lower() | ✅ Built |
| 🧮 Math Challenge Game | random, try/except, score tracking, defensive programming | ✅ Built |
| 🏧 ATM Machine | Functions, while, if/elif/else | 🔄 Coming Soon |
| 📊 Grade Calculator | Functions, lists, loops | 🔄 Coming Soon |

---

## 📖 What I Have Learned So Far

### 🌐 Internet & Web (Day 01)
- How the internet works (DNS, HTTP, HTTPS)
- Recursive vs Iterative DNS resolution
- HTTP Status Codes (200, 404, 500...)
- Role of Backend Server & CRUD operations
- What is an API (REST, GraphQL, WebSocket)

### 🐍 Python Basics (Day 02–07)

**Variables (Day 02)**
- Variables, naming rules, dynamic typing
- Global vs Local scope, `global` keyword
- Multiple assignment & unpacking

**Data Types (Day 03)**
- All 14 data types (int, float, str, bool, list, tuple, dict, set, frozenset, range, complex, bytes, bytearray, memoryview)
- Type casting, type checking with `type()`
- Truthy & Falsy values

**Conditions (Day 04)**
- if / elif / else, nested conditions
- Logical operators (and, or, not) with Truth Tables
- Shorthand if, ternary operator, `pass` statement

**User Input & f-Strings (Day 05)**
- `input()` function & type conversion
- Multiple inputs with `.split()` and `map()`
- f-Strings formatting, alignment, decimal places

**Loops (Day 06)**
- `for` loop with `range(start, stop, step)`
- `while` loop with conditions and flags
- `break`, `continue`, `pass` statements
- `else` clause in loops
- Nested loops & pattern printing (stars, triangles, pyramids)
- 3 Games built from scratch! 🎮

**Functions & Booleans (Day 07)**
- Basic functions with `def`
- Parameters, arguments & `return` statement
- Default parameters
- `*args` & `**kwargs`
- Positional-only `/` & keyword-only `*` arguments
- Combining `/` and `*`
- Nested functions
- Returning different data types
- Boolean values, Truthy & Falsy
- `isinstance()` function

---

## 💡 Key Concepts & Code Snippets

```python
# *args — variable positional arguments
def print_numbers(*args):
    for number in args:
        print(number)

# **kwargs — variable keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Positional-only + Keyword-only combined
def print_info(name, age, /, *, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Nested functions
def outer(x):
    def inner(y):
        return x + y
    return inner

# Defensive programming
while num2 == 0:
    num2 = random.randint(1, 100)  # Never divide by zero!

# Exception handling
try:
    user_answer = float(input("Answer: "))
except ValueError:
    print("Numbers only!")
```

---

## 🛠 Tech Stack

### ✅ Currently Learning
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### 🔄 Coming Next
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![NodeJS](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)

### ⏳ Future Goals
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-316192?style=for-the-badge&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

---

## 📝 Resources I Am Using

| Resource | Link | Type |
|----------|------|------|
| W3Schools Python | [w3schools.com](https://www.w3schools.com/python) | Website |
| roadmap.sh | [roadmap.sh/backend](https://roadmap.sh/backend) | Roadmap |
| CodeWithHarry | YouTube 🇮🇳 | Hinglish Video |
| Apna College | YouTube 🇮🇳 | Hinglish Video |
| WsCube Tech | YouTube 🇮🇳 | Hinglish Video |

---

## 🏆 Challenges Completed

| Topic | Coding Questions | MCQ | Status |
|-------|-----------------|-----|--------|
| Variables | ~15 | ~15 | ✅ |
| Data Types | ~15 | ~15 | ✅ |
| Conditions | ~15 | ~15 | ✅ |
| Loops | ~15 | ~15 | ✅ |
| Functions | In Progress | In Progress | 🔄 |

**Total: 100+ Questions Solved! 💪**

---

## 📈 Daily Consistency Log

| Day | Topic | Status |
|-----|-------|--------|
| Day 1 | Internet & Web | ✅ |
| Day 2 | Python Variables | ✅ |
| Day 3 | Python Data Types | ✅ |
| Day 4 | Python Conditions | ✅ |
| Day 5 | User Input & f-Strings | ✅ |
| Day 6 | Python Loops + 3 Games 🎮 | ✅ |
| Day 7 | Functions & Booleans | ✅ |

---

## 🎯 Goals

- ✅ Learn Python from Beginner to Advanced
- 🔄 Build Real-World Projects
- 🔄 Learn Databases (MySQL, MongoDB)
- 🔄 Develop REST APIs
- 🔄 Learn Flask / Django / FastAPI
- 🔄 Become Job Ready
- 🔄 Crack Software Developer Interviews

---

> **"Consistency beats talent when talent doesn't stay consistent."**
>
> *Started from zero — showing up every single night 🔥*
> *Not just reading — building projects from scratch! 🚀*

---

*⭐ If you find these notes helpful, please give this repo a star!*

*Made with 💙 and consistency — one night at a time!*



**Author:** Md Sakir  
🎓 B.Tech (Computer Science & Engineering)  
💻 Aspiring Backend Developer
