# ✨ BeautyVerse API

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.0%2B-092E20?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

**The ultimate backend solution for hybrid beauty e-commerce and professional booking platforms.**

[View Live Demo](#) | [Read Documentation](#)

</div>

---

## 🌟 Overview

**BeautyVerse API** is a robust, RESTful backend system designed to power the next generation of beauty platforms. It bridges the gap between searching for beauty products and booking professional services, offering a seamless experience for both customers and creators.

Whether you're browsing for the latest skincare products or booking a home-service makeup artist, BeautyVerse handles the logic securely and efficiently.

## 🚀 Key Features

### 🛍️ E-Commerce & Shopping
-   **Dynamic Product Catalog**: Browse products with advanced filtering by category, price, and location.
-   **Smart Pricing**: Automatic calculation of `final_price` based on creator-defined `discount_percent`.
-   **Cart Management**: Persistent shopping carts for users.
-   **Shop Logic**: Support for delivery options and physical shop locations.

### 🎨 Artists & Appointments
-   **Rich Artist Profiles**:
    -   📍 **Location & Service Mode**: Filter artists by location and `offers_home_service`.
    -   📸 **Portfolio**: Integrated generic links for Instagram/TikTok and portfolio galleries.
    -   ⭐ **Professional Details**: Categories, descriptions, and experience levels.
-   **Booking System**:
    -   📅 **Real-time Availability**: `/artists/<id>/available-slots/` endpoint prevents double-booking.
    -   🕒 **Scheduling**: Flexible booking, rescheduling, and cancellation policies.

### 🔐 Security & Role Management
-   **JWT Authentication**: Secure stateless authentication using `Simple JWT`.
-   **Role-Based Access**:
    -   **Customers**: Browse, shop, book.
    -   **Artists/Creators**: Manage their own profiles, services, and appointment slots.
    -   **Admins**: Full platform oversight.
-   **Ownership**: Strict permissions ensuring users can only edit objects they created.

## 🛠️ Tech Stack

-   **Framework**: [Django](https://www.djangoproject.com/) & [Django REST Framework](https://www.django-rest-framework.org/)
-   **Database**: MySQL (Aiven Cloud)
-   **Authentication**: JWT (JSON Web Tokens)
-   **Documentation**: Swagger / OpenAPI (via `drf-yasg`)
-   **Storage**: Cloudinary / S3 (Planned for media files)
-   **Deployment**: Ready for PythonAnywhere / Render / Railway

## 📋 API Documentation

Once running locally, full interactive API documentation is available at:
-   **Swagger UI**: `http://localhost:8000/swagger/`
-   **Redoc**: `http://localhost:8000/redoc/`

## 🔧 Installation & Setup

### Prerequisites
-   Python 3.8+
-   MySQL Database URL

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/beautyverse-api.git
cd beautyverse-api
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
Create a `.env` file in the root directory:
```env
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=defaultdb
DB_USER=avnadmin
DB_PASSWORD=your_password
DB_HOST=mysql-id.aivencloud.com
DB_PORT=your_port
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Run Migrations & Server
```bash
python manage.py migrate
python manage.py runserver
```

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
    <sub>Built by Bonane NIYIGENA</sub>
</div>
