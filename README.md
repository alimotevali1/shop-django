# 🛍️ Django Shop

A simple e-commerce web application built with **Django 5**.  
This project demonstrates product management, cart functionality, and order processing using Django’s ORM and admin panel.

---

## 🚀 Features
- Product listing and detail pages  
- Shopping cart with session handling  
- Order creation and management  
- Django Admin integration for managing products and users  
- Simple, extendable structure for scaling up  

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Create a superuser
```bash
python manage.py createsuperuser
```

### 6. Run the server
```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser 🎉

---

## 📂 Project Structure
```
your_project/
├── shop/                  # Main e-commerce app
├── cart/                  # Shopping cart logic
├── orders/                # Order handling
├── static/                # CSS, JS, images
├── templates/             # HTML templates
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Built With
- [Django](https://www.djangoproject.com/) – Python web framework  
- [asgiref](https://pypi.org/project/asgiref/) – ASGI utilities for Django  
- [sqlparse](https://pypi.org/project/sqlparse/) – SQL parsing library used by Django  
- [tzdata](https://pypi.org/project/tzdata/) – Time zone database for Python  

---

## 💡 Future Improvements
- Product categories and filters  
- Payment gateway integration  
- User profiles and order history  
- REST API (Django REST Framework)  
- Frontend with React or Vue  

---

## 📄 License
This project is open source and available under the [MIT License](LICENSE).

---

Made with ❤️ using **Django**

---

### 📦 requirements.txt

```txt
asgiref==3.9.2
Django==5.2.6
sqlparse==0.5.3
tzdata==2025.2
```
