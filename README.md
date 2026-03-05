# 🎯 Event Countdown Timer Django

A Django-based countdown application that helps users track and manage countdown timers for various events and deadlines.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/BALADURGAG24/django-event-countdown-website)

## 📁 Project Structure 
  
```
Directory structure:
└── baladurgag24-django-event-countdown-website/
    ├── README.md
    ├── db.sqlite3
    ├── LICENSE
    ├── manage.py
    ├── countdown/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── __pycache__/
    └── home/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── views.py
        ├── __pycache__/
        ├── migrations/
        │   ├── 0001_initial.py
        │   ├── __init__.py
        │   └── __pycache__/
        └── templates/
            └── myapp.html
```

## ⚙️ How Does It Work? (Flow)

👉 You do these steps:

1️⃣ You create an Event (via admin panel).
2️⃣ You open the main web page (http://127.0.0.1:8000/).
3️⃣ Django fetches the Event and calculates how much time is left.
4️⃣ The HTML page shows:
   - Event Name
   - Countdown timer (hours, minutes, seconds)
5️⃣ JavaScript updates the countdown every second to show the real-time countdown.

## 📚 Key Technologies Used

| Technology | Purpose |
|------------|---------|
| Django | Main web framework (Python) |
| Django ORM | Database access |
| Django Admin | Managing Events easily |
| HTML | Webpage structure |
| CSS | Styling the page |
| JavaScript | Real-time countdown timer animation |
| SQLite | Default database used by Django |

## ✅ Use Cases

👉 This project can be used to build:

- 🚀 A countdown for product launches
- 🎤 A countdown for conferences
- 🎉 A countdown for personal events (birthdays, parties)
- ⏱️ A timer for hackathons or competitions
- 🏠 A homepage "coming soon" countdown

## 🚀 Features

- ⏰ Create and manage countdown timers
- 📅 Track important events and deadlines
- 🎨 Clean and intuitive user interface
- 🔄 Real-time countdown updates
- 📱 Responsive design for all devices

## 🛠️ Technology Stack

- **Backend Framework**: Django
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Template Engine**: Django Templates

## 🏗️ Project Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/BALADURGAG24/django-event-countdown-website.git
   cd django-event-countdown-website
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## 📝 Key Components

### 🏠 Home App
- Handles the main countdown functionality
- Contains views for displaying and managing countdowns
- Includes templates for the user interface

### ⚙️ Project Configuration
- Django settings and URL routing
- Database configuration
- Static and media file handling

## 🔧 Development

- The project uses Django's built-in development server
- SQLite database for development
- Django admin interface for data management

## 📚 API Documentation

The project includes the following main endpoints:
- `/` - Home page with countdown display
- `/admin/` - Django admin interface
- `/api/` - API endpoints for countdown management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- [BALADURGAG24](https://github.com/BALADURGAG24) - Initial work

## 🙏 Acknowledgments

- Django Documentation
- Django Community
- All contributors who have helped shape this project
