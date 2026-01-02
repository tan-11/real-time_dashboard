# Real-Time Inventory Dashboard

A full-stack web application featuring an Admin Portal for data management and a User Portal for real-time data visualization. Built with Django (Backend) and Vue.js (Frontend).

## 🚀 Live Demo URLs
- **Admin Portal (Login):** [https://tan-11.github.io/real-time_dashboard/frontend/login.html](https://tan-11.github.io/real-time_dashboard/frontend/login.html)
- **User Portal (View Only):** [https://tan-11.github.io/real-time_dashboard/frontend/user.html](https://tan-11.github.io/real-time_dashboard/frontend/user.html)
- **Backend API:** [https://real-time-dashboard-t5gv.onrender.com/api/items/](https://real-time-dashboard-t5gv.onrender.com/api/items/)

> **Test admin Credentials:**
> - **Username:** `admin`
> - **Password:** `admin123`

---

## 🛠️ Tech Stack
* **Frontend:** Vue.js 3 (CDN), Bootstrap 5
* **Backend:** Python Django 5, Django Rest Framework (DRF)
* **Database:** SQLite (Dev), Render Ephemeral (Prod)
* **Deployment:** Docker (Backend), GitHub Pages

---

## Features Implemented
### 1. Admin Portal
* **CRUD Operations:** Add, View, Edit, and Delete items.
* **Input Validation:** Prevents duplicate names and ensures valid colors/shapes.
* **Search & Filter:** Filter by Shape/Color and Search by Name.
* **Authentication:** Secure Login/Logout using Token-based Auth.

### 2. User Portal
* **Real-Time Data:** Displays items in a grid format.
* **Timestamps:** Shows creation and latest update times.
* **Read-Only:** Users can view and filter but cannot modify data.

### 3. Bonus Features 
* ✅ **Authentication:** Users must log in to access the Admin/User interface.
* ✅ **Input Validation:** Backend enforces data integrity; Frontend provides immediate feedback.
* ✅ **Deployment:** Fully deployed to the cloud (Render + GitHub Pages).
* ✅ **Docker:** Containerized backend for consistent deployment.

---

## How to Run Locally

### Prerequisites
* Python 3.10+
* Git

### 1. Clone the Repository
```bash
git clone [https://github.com/tan-11/real-time_dashboard.git](https://github.com/tan-11/real-time_dashboard.git)
cd real-time_dashboard
```

### 2. backend setup
```bash
cd backend
# Create virtual environment (Optional)
python -m venv venv
venv\Scripts\activate  #(mac: source venv/bin/activate)

# Install dependencies
pip install -r requirements.txt

# Run Migrations & Start Server
python manage.py migrate
python manage.py createsuperuser # Create your local admin
python manage.py runserver
```

### 3. Frontend Setup
* Navigate to the `frontend/` folder.
* Open `admin.html` or `user.html` in your text editor.
* Update the API URL:
* Change const API_URL from the cloud URL to `http://127.0.0.1:8000/api`.
* Open `login.html` in your browser to start.
