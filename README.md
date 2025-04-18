# Grocery Shopping Application

# 🛒 Grocery Shop - Flask Web Application

A simple, full-featured grocery shopping web app built using **Flask**. Admins can manage products and categories, while users can register, log in, view products, add items to cart, and checkout.

---

## 🚀 Features

### 🔐 Authentication
- User registration & login
- Profile update with password change
- Secure session management

### 🛍️ User Functionalities
- Browse categorized products
- Search products by name and filter by price
- Add items to cart
- View cart summary and checkout

### 🛠️ Admin Dashboard
- Add / Edit / Delete product categories
- Manage products under categories
- View summary and analytics via charts

---

## 📸 Screenshots

> Add screenshots of homepage, product list, admin dashboard, and cart here.

---

## 🧰 Tech Stack

- **Backend**: Flask (Python)
- **Templating**: Jinja2
- **Frontend**: HTML, CSS, Bootstrap5, Font Awesome
- **Database**: SQLite with SOLALchemy
- **Charting**: Chart.js

---

## 📁 Project Structure

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
## Create virtual environment
python -m venv venv
source venv/bin/activate      
Windows: venv\Scripts\activate
