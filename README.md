# Django Blog Dashboard

A feature-rich, responsive blog platform built with Django and Bootstrap 5.  
Includes user authentication, category subscriptions, admin dashboard, comments with moderation, REST API, and more.

---

## Features

- User registration, login, and logout
- Blocked user handling
- Category subscription/unsubscription with email confirmation
- Responsive Bootstrap 5 UI with modern dashboard layout
- Post creation, editing, deletion (admin and via web form)
- Categories and tags management
- Post likes/dislikes (auto-delete on >10 dislikes)
- Comments with forbidden word filtering and single-level replies
- Admin dashboard with user, post, category, and forbidden word management
- Highlighted admin users in user list
- Django REST Framework API endpoints
- Search by tag or post title
- Pagination for posts and category views

---

## Screenshots

*Add screenshots here to showcase your landing page, post detail, admin dashboard, etc.*

---

## Getting Started

### 1. Clone the Repository

git clone https://github.com/YOUR-USERNAME/django-blog-dashboard.git
cd django-blog-dashboard

text

### 2. Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

text

### 3. Install Dependencies

pip install -r requirements.txt

text

### 4. Apply Migrations

python manage.py migrate

text

### 5. Create a Superuser

python manage.py createsuperuser

text

### 6. Run the Development Server

python manage.py runserver

text

### 7. Access the Application

- Blog: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## API Endpoints

| Endpoint                        | Methods         | Description                         |
|----------------------------------|----------------|-------------------------------------|
| `/api/posts/`                    | GET, POST      | List & create posts                 |
| `/api/posts/<id>/`               | GET, PUT, DELETE | Retrieve, update, delete post     |
| `/api/posts/<id>/comments/`      | GET, POST      | Add/view comments for a post        |

---

## Project Structure

blog_dashboard/
├── blog/
│ ├── templates/
│ ├── static/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ └── ...
├── blog_dashboard/
│ ├── settings.py
│ └── urls.py
├── manage.py
└── requirements.txt

text

---

## Configuration Notes

- **Email:** Uses Django's console backend for development. To send real emails, configure SMTP in `settings.py`.
- **Media:** Ensure `MEDIA_URL` and `MEDIA_ROOT` are set for image uploads.
- **Forbidden Words:** Manage via the admin panel.
- **Category and Tag Management:** Use the admin or extend the UI as needed.

---

## Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the MIT License.
