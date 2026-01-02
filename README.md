# Real-Time Inventory Dashboard

A full-stack web application featuring an Admin Portal for data management and a User Portal for real-time data visualization. [cite_start]Built with Django (Backend) and Vue.js (Frontend)[cite: 8, 36, 37].

## 🚀 Live Demo URLs
- **Admin Portal (Login):** [https://tan-11.github.io/real-time_dashboard/frontend/login.html](https://tan-11.github.io/real-time_dashboard/frontend/login.html)
- **User Portal (View Only):** [https://tan-11.github.io/real-time_dashboard/frontend/user.html](https://tan-11.github.io/real-time_dashboard/frontend/user.html)
- **Backend API:** [https://real-time-dashboard-t5gv.onrender.com/api/items/](https://real-time-dashboard-t5gv.onrender.com/api/items/)

> **Test Credentials:**
> - **Username:** `admin`
> - **Password:** `admin123`

---

## 🛠️ Tech Stack
* [cite_start]**Frontend:** Vue.js 3 (CDN), Bootstrap 5 [cite: 36]
* [cite_start]**Backend:** Python Django 5, Django Rest Framework (DRF) [cite: 37]
* [cite_start]**Database:** SQLite (Dev), Render Ephemeral (Prod) [cite: 40]
* [cite_start]**Deployment:** Docker (Backend), GitHub Pages (Frontend) 

---

## ✨ Features Implemented
### [cite_start]1. Admin Portal [cite: 11]
* **CRUD Operations:** Add, Edit, and Delete items.
* [cite_start]**Input Validation:** Prevents duplicate names and ensures valid colors/shapes[cite: 13].
* **Search & Filter:** Filter by Shape/Color and Search by Name.
* [cite_start]**Authentication:** Secure Login/Logout using Token-based Auth.

### [cite_start]2. User Portal [cite: 18]
* [cite_start]**Real-Time Data:** Displays items in a grid format[cite: 21].
* [cite_start]**Timestamps:** Shows creation and update times[cite: 20].
* **Read-Only:** Users can view and search but cannot modify data.

### [cite_start]3. Bonus Features 
* ✅ **Authentication:** Users must log in to access the Admin interface.
* ✅ **Input Validation:** Backend enforces data integrity; Frontend provides immediate feedback.
* ✅ **Deployment:** Fully deployed to the cloud (Render + GitHub Pages).
* ✅ **Docker:** Containerized backend for consistent deployment.

---

## 💻 How to Run Locally

### Prerequisites
* Python 3.10+
* Git

### 1. Clone the Repository
```bash
git clone [https://github.com/tan-11/real-time_dashboard.git](https://github.com/tan-11/real-time_dashboard.git)
cd real-time_dashboard
