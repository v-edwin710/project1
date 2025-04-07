# 🛠 Project Setup Instructions

Follow these steps to get your project up and running:

---

## 🔧 1. Install Required Packages

Use `pip` to install all dependencies listed in `requirements.txt`:

`pip install -r requirements.txt`

---

## 🚀 2. Configure Your API Route

Open `main.py` and **modify or add your desired API route** to handle requests as needed.

---

## ▶️ 3. Run the API Server

Start your Flask API by running:

`python main.py`

This will launch the server, typically on `http://127.0.0.1:5000/`.

---

## 🖥 4. Split the Terminal (Optional but Recommended)

Open a new terminal tab or split the terminal so you can run another script without stopping the server.

---

## 🗄 5. Configure the Database Connection

In `test.py`, update the database connection settings:

- DRIVER_NAME = ''        # e.g., 'ODBC Driver 17 for SQL Server'
- SERVER_NAME = ''        # e.g., 'localhost' or '192.168.1.100\SQLEXPRESS'
- DATABASE_NAME = ''      # e.g., 'my_database'
- USERNAME = 'your_username'
- PASSWORD = 'your_password'

---

## 🧪 6. Run the Database Test Script

Once you've configured the connection in `test.py`, run:

`python test.py`

This will execute your database-related functionality.