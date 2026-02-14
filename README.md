# 📌 Flask CRUD Application

A simple CRUD (Create, Read, Update, Delete) web application built using Flask.
This project is created for learning and understanding how Flask works with routing, templates, forms, and database integration.

---

## 🚀 Features

* Create new records
* View all records
* Update existing records
* Delete records
* Basic HTML templates using Jinja2
* SQLite database integration
* Flask-SQLAlchemy ORM

---

## 🛠 Tech Stack

* Python 3.x
* Flask
* Flask-SQLAlchemy
* SQLite
* Gunicorn (for production server)

---

## 📂 Project Structure

```
flask-learning/
│
├── app.py
├── requirements.txt
├── instance/
├── static/
├── templates/
│   ├── index.html
│   ├── create.html
│   └── edit.html
└── env/   (virtual environment - not pushed to git)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd flask-learning
```

---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv env
```

Activate it:

```bash
source env/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application (Development)

```bash
python app.py
```

Or:

```bash
flask run
```

App will run at:

```
http://127.0.0.1:5000
```

---

### 5️⃣ Run with Gunicorn (Production Style)

```bash
gunicorn --workers 3 --bind 0.0.0.0:8000 app:app
```

---

## 🗄 Database

This project uses SQLite.

The database file is automatically created when the app runs for the first time.

If using Flask-SQLAlchemy, make sure:

```python
db.create_all()
```

is executed before running the app.

---

## 📚 What I Learned

* Flask routing and decorators
* Working with templates (Jinja2)
* Handling forms
* Connecting to SQLite
* Using Flask-SQLAlchemy
* Running app with Gunicorn
* Virtual environment management in Linux

---

## 🔮 Future Improvements

* Add authentication (Login/Register)
* Add REST API endpoints
* Add pagination
* Add Bootstrap styling
* Deploy with Nginx + Gunicorn
* Deploy on cloud (AWS / VPS / Vercel alternative)

---

## 🎯 Purpose

This project is built for learning Flask fundamentals and backend development concepts.
