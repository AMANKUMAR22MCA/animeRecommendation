
# Anime Recommendation Web App 🎌

A full-stack anime recommendation web app with JWT-based authentication, anime search, genre filtering, and personalized recommendations.

## 🌐 Live Demo

Hosted on **Google Cloud Platform**: [View Demo](http://34.100.160.93:5501/login.html)

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/98977004-ba5f-4e27-896f-147ac69abcb7)
<br>
![image](https://github.com/user-attachments/assets/c57551f6-f410-47af-98c9-f0c984e531aa)
<br>
![image](https://github.com/user-attachments/assets/12f51d18-dd4e-41c1-8b2c-51dfa4f8e743)

## ✨ Features

- 🔐 User Registration & Login with JWT Authentication
- 🧠 Personalized Anime Recommendations
- 🔍 Search Anime by Title
- 🎨 Filter Anime by Genre
- 📦 Deployed using Docker & Google Cloud

---

## 🖥️ Local Development Setup (Without Docker)

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/anime-recommendation-app.git
    cd anime-recommendation-app
    ```

2. **Create Virtual Environment & Activate**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate   # Windows
    ```

3. **Install Requirements**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations & Start Server**

    ```bash
    python manage.py makemigrations anime
    python manage.py migrate
    python manage.py runserver
    ```
```
- Note : for loacl setup you need to change the urls frontend (login.html , register.html , dashboard.html ) to http://127.0.0.1:8000
  and dont forget to add db creds 
```
5. Open browser and visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🐳 Docker Setup (Recommended)

1. **Run with Docker Compose**

    ```bash
    docker-compose up -d
    ```

2. **Database Settings for PostgreSQL in Docker**

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'anime_db',
            'USER': 'anime_user',
            'PASSWORD': 'anime_pass_123',
            'HOST': 'db',
            'PORT': '5432',
        }
    }
    ```

> 🔐 _Note: Change the above database credentials in production._

---

## 🗃️ Tech Stack

- **Frontend**: HTML/CSS + JS 
- **Backend**: Django + Django REST Framework
- **Database**: PostgreSQL / MySQL (Optional)
- **Authentication**: JWT
- **Deployment**: Docker, Google Cloud Platform

---

## 🧠 Credits

Project created by Aman Kumar 🚀

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

