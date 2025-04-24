# 🛒 Grocery Shop App — Flask + REST API + PostgreSQL

A modern, scalable, and RESTful web application for managing a grocery store. Built using **Flask**, **PostgreSQL/SQLite**, **Flask-RESTful**, and **Bootstrap 5**, this app provides a full-featured shopping and inventory system — complete with admin management, product CRUD operations, order handling, transaction reports, and API endpoints ready for frontend or mobile app integration.

---

## 🚀 Introduction

This Grocery Shop App is a production-ready web application that simulates an e-commerce-style shopping experience tailored for grocery store operations. It supports complete CRUD functionality, robust REST APIs, and interactive frontend features using modern tools and best practices.

This project demonstrates:
- Clean architecture with separation of concerns
- RESTful API design
- Use of relational database and models
- Professional UI and functionality

---

1. **Admin** can manage products and categories Add, Update/edit, Delete products and categories, while 

2. **Users** can register, log in, view products, add items to cart, and order/buy products. Users can also print out all trasaction history and 
export all odered product into csv file.

---

## ✅ Key Features

- 🔐 **Authentication System** (Login/Logout)
- 📦 **Product Management** (CRUD)
- 🗂️ **Category Management**
- 🛒 **Cart & Orders Handling**
- 💸 **Transactions & Billing**
- 🧾 **Export Reports as CSV**
- 🔄 **API Endpoints for Frontend & Mobile App**
- 📅 **Product Manufacturing Date Support**
- 🔍 **Search, Sort & Filter**
- 🌙 **Dark Mode Toggle**
- 📤 **Print-Friendly Transaction Page**
- 📈 **Pagination & Performance Optimization**

---

## 🧩 Additional Features

- 🖨️ **Print All Transactions Page** for invoice and reports.
- 📂 **Export All Orders to CSV** for admin.
- 🔄 **RESTful API for Products, Categories, and Orders**.
- ✅ **Full CRUD via APIs** (Tested with Postman).
- ⚙️ **Pagination**, **Filtering**, and **Sorting** supported.
- 🔌 **API Integration Ready** for mobile or frontend frameworks like Vue.js or React.
- 🔐 CSRF Protection & Form Validation using Flask-WTF.

---

## 🧰 Tech Stack

- **Backend**: Flask (Python)
- **Templating**: Jinja2
- **Frontend**: HTML, CSS, Bootstrap5, Font Awesome
- **Database**: SQLite with SOLALchemy
- **Charting**: Chart.js

---

## 📂 Folder Structure

grocery-shop/ │ ├── app.py # Main Flask app entry point 
├── models.py # SQLAlchemy database models 
├── config.py # Configurations (DB URI, Secret key) 
├── requirements.txt # Python package dependencies 
├── .gitignore # Files/folders to ignore in git 
├── README.md # Project overview 
│ ├── templates/ # Jinja2 templates (HTML views) 
  │ ├── layout.html │ ├── login.html │ ├── register.html │ ├── profile.html │ ├── cart.html │ ├── admin_dashboard.html │ ├── ... 
│ ├── static/ # Static assets │ ├── css/ │ ├── js/ │ └── images/ 
│ |── instance/ # (Optional) for SQLite DB or config


---

## 🧪 Setup & Run Locally

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/grocery-shop.git
cd grocery-shop
```
2. **Create virtual environment**
```
python -m venv venv
source venv/bin/activate      
Windows: venv\Scripts\activate
```
3. **Install dependencies**
```
pip install -r requirements.txt
```
4. **🛠️ Initialize the database**
```
from app import db
db.create_all()
```
5. **▶️ Run the app**
```
▶️ Run the app
```
Visit: http://127.0.0.1:5000

---

## 🔗 API Endpoints Overview

Method | Endpoint | Description
GET | /api/products | List all products
POST | /api/products | Create new product
GET | /api/products/<id> | Retrieve product by ID
PUT | /api/products/<id> | Update a product
DELETE | /api/products/<id> | Delete a product
GET | /api/category | Get all categories
GET | /api/orders | List all orders
POST | /api/orders | Create new order

## 👨‍💻 Author
**Sanish Kumar**

Aspiring Backend Developer | Python | Flask | REST APIs

📧 sanishbux42@gmail.com
