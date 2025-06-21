# 💪 FitNova — Your AI-Powered Fitness Tracker 

FitNova is an AI-powered fitness tracker built with Streamlit and MySQL. It empowers users to set goals, log workouts, monitor progress, interact with an AI coach (Nova AI), and analyze nutrition plans via natural language or uploaded meal files.

---

## 🧩 Features

- 🔐 Secure user authentication
- 🧮 BMI calculation with health categories
- 🏋️ Workout logger with calories burned
- 🎯 Goal detection from user message & tracking
- 🤖 AI assistant powered by LLaMA3 model
- 🥗 Nutrition chat via PDF upload or questions
- 📊 Interactive dashboards with Plotly
- 📄 Personalized PDF report generation
- 🎨 Streamlit-based modern interface


### 🥗 Nutrition Chat Usage

- Upload your meal plan as a PDF or text file.
- Or type natural language queries like:
- “How many calories are in this meal plan?”
- “Does this diet provide enough protein for weight loss?”

### 📄 PDF Report

Click the 📄 Generate Report button to download a personalized summary of your:
- ✅ BMI
- ✅ Fitness Goals
- ✅ Workout History
- ✅ Chatbot Interactions

### 🔍 Chatbot Capabilities

The built-in chatbot "Nova AI" can:
- 💡 Provide personalized fitness and nutrition tips.
- 🎯 Automatically extract structured goals from messages like:
- 🥗 Analyze uploaded meal plans (PDF or text).
- 📊 Display chatbot interaction logs and active goals.
- 🧠 Respond contextually using your BMI, goals, and recent workout data.

---


## 🚀 Tech Stack

| Layer         | Technology     |
|---------------|----------------|
| Frontend      | Streamlit      |
| Backend       | Python          |
| Database      | MySQL          |
| AI Chat       | LLaMA3 |
| Visualization | Plotly         |
| File Parsing  | PyMuPDF        |

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fitnova.git
cd fitnova
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🛠 MySQL Setup

### Step 1: Create Database

```sql
CREATE DATABASE fitnova;
USE fitnova;
```

### Step 2: Create Tables

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    height FLOAT,
    weight FLOAT
);

CREATE TABLE workouts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    date DATE,
    exercise VARCHAR(100),
    duration INT,
    calories_burned FLOAT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE goals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    goal_type VARCHAR(100),
    target_value FLOAT,
    current_value FLOAT,
    start_date DATE,
    end_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE chat_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    user_message TEXT,
    bot_reply TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

---

## 📁 Project Structure

```
fitnova/
├── app.py
├── auth.py
├── db.py
├── bmi.py
├── dashboard.py
├── workouts.py
├── goals.py
├── chatbot.py
├── nutrition_chat.py
├── report_generator.py
├── pro.py
├── tips.py
├── requirements.txt
└── README.md
```

## 👤 Author

Made by [sharan kk]  
