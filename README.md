# 🛒 CRUD-Project: Flipkart Clone (Django)

A Django-based CRUD (Create, Read, Update, Delete) web application inspired by Flipkart, demonstrating essential backend operations, user authentication, and product management.

---

## 🚀 Features

- ✅ User Authentication (Login/Register/Logout)
- 🧾 Add, View, Edit, and Delete Products
- 📦 Category-wise product listing
- 🔍 Product detail view
- 🛠️ Admin dashboard for managing inventory
- 🎨 Simple and responsive UI (can be integrated with Bootstrap or Tailwind CSS)

---

## 📂 Project Structure
Flipkart/ ├── Electronics/ # Django app for managing products ├── Flipkart/ # Main Django project ├── db.sqlite3 # Default SQLite database ├── manage.py # Django management script └── templates/ # HTML templates (if used)


---

## ⚙️ Setup Instructions

1. Clone the repository:-
git clone https://github.com/DivyamOswal/CRUD-Project.git
cd CRUD-Project

2. Create & activate a virtual environment:-
python -m venv venv
venv\Scripts\activate  # On Windows

3. Install dependencies:-
pip install -r requirements.txt

4. Run migrations:-
python manage.py makemigrations
python manage.py migrate

5. Create a superuser (admin):-
python manage.py createsuperuser

6. Run the server:-
python manage.py runserver

🧪Tech Stack:-
  (1) Backend: Python, Django

  (2)Database: SQLite (can be swapped with PostgreSQL/MySQL)
  
  (3) Frontend: HTML, CSS, Bootstrap (optional)
  
  (4) Version Control: Git + GitHub


  






