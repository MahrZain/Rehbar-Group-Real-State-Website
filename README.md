# Rehbar Group – Real Estate & Construction Platform

> "From dream homes to smart investments, we guide you every step of the way."
> 
<img width="950" height="453" alt="home" src="https://github.com/user-attachments/assets/6e313acf-eba1-4e02-8b86-ad3ecb7c3e10" />
> Admin Panel
<img width="949" height="454" alt="Admin" src="https://github.com/user-attachments/assets/0db086cc-9b93-42a4-ba1f-444f94c6bfd9" />



## 📌 Overview
**Rehbar Group** is a Pakistan-based real estate company offering complete solutions in development, marketing, construction, and investment consultancy. This repository contains the source code for [rehbargroup.com](https://rehbargroup.com) - a responsive, animated website with admin management built with:

- **Backend**: Django 5.0 (Python 3.11)
- **Frontend**: Tailwind CSS v3
- **Admin**: Jazzmin (AdminLTE 3)
- **Animations**: GSAP + ScrollTrigger
- **Carousel**: Swiper JS v11

## ✨ Key Features
| Category       | Features                                                                 |
|----------------|--------------------------------------------------------------------------|
| **Frontend**   | Responsive design, GSAP animations, Swiper carousels, WhatsApp integration |
| **Backend**    | Django admin, Content management, Secure forms, Newsletter system        |
| **Admin**      | Jazzmin dashboard, Dark/light mode, Customizable UI                     |
| **Utilities**  | Scroll-to-top, Sticky navbar, Contact form with CSRF protection          |

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Django
- Node.js (for Tailwind)
- PostgreSQL (recommended for production)

### Installation
```bash
# Clone repository
https://github.com/MahrZain/Rehbar-Group-Real-State-Website.git
cd rehbargroup

# Setup virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure database
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run development server
python manage.py runserver


## 📌 Structure

rehbargroup/
├── website/          # Main application
│   ├── models/       # Database models
│   ├── templates/    # HTML templates
│   ├── static/       # CSS/JS/images
│   └── views/        # Business logic
├── config/           # Project settings
└── manage.py         # Django CLI

