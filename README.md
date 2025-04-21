# 📚 PSC MCQ Helper

A web-based platform designed to streamline MCQ-based practice for Public Service Commission (PSC) exams. Features categorized question banks, instant scoring, and easy access to correct answers to help users learn efficiently.

---

## 🚀 Features

- 📂 Category-Based Questions — Filter and attempt MCQs by subject or exam category.  
- 🧠 Instant Evaluation — Automatically checks answers and provides scores.  
- 📊 Scoreboard — Tracks and displays performance after each quiz session.  
- 🔍 Correct Answer Highlighting — Shows the correct options for better understanding.  
- 🧾 Easy-to-Use Interface — Clean layout using W3.CSS, designed with responsiveness in mind.  
- 🌐 WebSocket Integration — Enables real-time communication for future enhancements.

---

## ⚙️ Installation

Follow these steps to set up and run the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/psc-mcq-helper.git
cd psc-mcq-helper

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the development server
python manage.py runserver
