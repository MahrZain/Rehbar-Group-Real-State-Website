

```markdown
# Rehbar Group – Real Estate & Construction Platform

> “From dream homes to smart investments, we guide you every step of the way.”

**Rehbar Group** is a Pakistan-based real estate company offering complete solutions in development, marketing, construction, and investment consultancy.  
This repository contains the **entire source code** for [rehbargroup.com](https://rehbargroup.com) — a fully responsive, animated, and admin-manageable website built using **Django 5**, **Tailwind CSS**, **Jazzmin**, and **Swiper JS**.


---




---


## ✨ Features

- ✅ Modern UI with Tailwind CSS utility classes
- 📱 Fully responsive and mobile-friendly
- 🎯 Dynamic content: Home, About, Services, Projects, Contact Info
- 📊 Animated elements using GSAP + ScrollTrigger
- 🧭 Carousel for Featured Projects using Swiper.js
- 💬 WhatsApp floating button
- 🧑‍💼 Admin dashboard powered by Jazzmin
- 📬 Contact form with CSRF protection
- 🧩 Newsletter section
- ⚡ Scroll to top button + sticky navbar

---

## 🛠️ Tech Stack

- **Backend:** Django 5.0 (Python 3.11)
- **Frontend Styling:** Tailwind CSS v3 (CDN / CLI supported)
- **Animations:** GSAP + ScrollTrigger
- **Carousel:** Swiper JS v11
- **Icons:** Font Awesome 6
- **Admin Panel:** Django Jazzmin (AdminLTE 3 UI with dark/light modes)

---

---

## ⚙️ Quick Start Guide

### 🚀 Install & Run Locally

```bash
# Step 1: Clone the repo
git clone https://github.com/yourusername/rehbargroup.git
cd rehbargroup

# Step 2: Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Apply migrations
python manage.py migrate

# Step 5: Create a superuser
python manage.py createsuperuser

# Step 6: Run the server
python manage.py runserver

# Visit: http://127.0.0.1:8000
# Admin: http://127.0.0.1:8000/admin
````

### 🌀 Tailwind CLI (Optional for Custom Build)

```bash
# If you want to use Tailwind locally instead of CDN
npx tailwindcss -i website/static/css/input.css \
                -o website/static/css/tailwind.css --watch
```

---

## 🎨 Jazzmin Admin Panel

Jazzmin replaces the default Django admin with a beautiful, customizable dashboard.

### ✅ Setup Jazzmin

1. Installed already via `requirements.txt`
2. Add to your `INSTALLED_APPS` in `settings.py` **before** `django.contrib.admin`:

```python
INSTALLED_APPS = [
    "jazzmin",                  # ← this line first
    "django.contrib.admin",
    ...
]
```

3. (Optional) Add custom Jazzmin settings:

```python
JAZZMIN_SETTINGS = {
    "site_title": "Rehbar Admin",
    "site_brand": "Rehbar Group",
    "welcome_sign": "Welcome to Rehbar Dashboard",
    "show_ui_builder": True,
    "changeform_format": "horizontal_tabs",
    "navigation_expanded": True,
}
```

4. Start the dev server and go to `/admin` to enjoy the styled panel!

---

## 🧪 Deployment Tips

* Use `python manage.py collectstatic` in production
* Setup **Gunicorn** or **uWSGI** for WSGI server
* Use **Nginx** as a reverse proxy
* Optional: Add `Dockerfile` and `docker-compose.yml` for containerization

---

## 🧾 Example `.env`

```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your@email.com
EMAIL_HOST_PASSWORD=yourpassword
```

---

## 💻 Admin Credentials (for testing)

```bash
Username: admin
Password: (your set password)
```

Visit: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 📬 Contact

```
Rehbar Group
📍 Islamabad, Pakistan
📞 +92 300 1234567
📧 info@rehbargroup.com
🌐 https://rehbargroup.com
```



---

## 🙌 Credits

Developed with ❤️ by  [NullxCoder](https://linktr.ee/nullxco)

---

