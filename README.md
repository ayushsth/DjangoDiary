# DjangoDiary

DjangoDiary is a personal diary web application built with Django that allows users to securely create, manage, and organize diary entries. The application also includes an integrated news section powered by the NewsAPI.

## Live Link
https://djangodiary.onrender.com/

## Features

- User Authentication System
  - Register
  - Login
  - Logout

- Personal Diary Management
  - Create diary entries
  - Update existing entries
  - Delete entries
  - View individual diary entries

- News Feed Integration
  - Fetches latest headlines using NewsAPI
  - Pagination support

- Secure User-Based Access
  - Users can manage only their own diary entries

- Responsive UI using Django Templates

## Tech Stack

### Backend
- Django
- Python

### Database
- SQLite

### Deployment
- Render

## Installation & Setup

### Clone the repository

```bash
git clone https://github.com/ayushsth/DjangoDiary.git
cd DjangoDiary
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate virtual environment

#### Windows

```bash
.venv\\Scripts\\activate
```

#### Linux/Mac

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create `.env` file

Create a `.env` file in the root directory and add:

```env
SECRET_KEY=your_secret_key
DEBUG=True
NEWS_API_KEY=your_news_api_key
```

### Run migrations

```bash
python manage.py migrate
```

### Start development server

```bash
python manage.py runserver
```
