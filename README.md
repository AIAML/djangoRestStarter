# Django REST Starter

یک پروژه نمونه **Django + Django REST Framework + JWT** برای مدیریت کاربران و API.  
این پروژه با هدف یادگیری و تمرین پیاده‌سازی **RESTful API با احراز هویت JWT** طراحی شده است.

---

## ویژگی‌ها
- ثبت‌نام کاربران (Register)
- ورود و دریافت JWT Token (Login)
- مشاهده و ویرایش پروفایل کاربر (Profile)
- احراز هویت با JWT
- Refresh Token برای تمدید دسترسی
- ساختار ماژولار با apps (users, core, ...)
- آماده برای توسعه و افزودن ماژول‌های دیگر

---

## پیش‌نیازها
- Python >= 3.10
- pip
- virtualenv یا venv
- SQLite (به طور پیش‌فرض) یا SQL Server / PostgreSQL (قابل تغییر در settings)

---

## نصب و راه‌اندازی

### مرحله 1: کلون کردن پروژه
```bash
git clone https://github.com/AIAML/djangoRestStarter.git
cd djangoRestStarter
