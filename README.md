<img width="914" height="297" alt="Group 5" src="https://github.com/user-attachments/assets/44b191f0-d1fb-455a-98fb-0411bd4314ab" />

This project is a Django-based web application for creating, managing, and exporting CVs (resumes)

## Technology Stack:

* **Django**
  A high-level Python web framework used for backend development, authentication, access control, and form handling

* **PostgreSQL**
  A powerful relational database system used for storing user data, CV information, and file metadata

* **Python**
  The core programming language of the project, used for business logic, data processing, and document generation

* **python-docx**
  A library used to dynamically generate professional CV documents in DOCX format based on user-submitted data

## Getting Started:

### 1. Clone the repository

```bash
git clone https://github.com/Marchello-Projects/PyPortfolio
```

### 2. Create and activate virtual environment (optional but recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate  
# On Windows: python -m venv .venv
# .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
### 4. Set up environment variables

Create a `.env` file in the root directory with the following content:

```env
SECRET_KEY=Your_django_secret_key
DB_NAME=Database_Name
DB_USER=Database_user
DB_PASSWORD=Database_password
```

> [!NOTE]
> **Generate a Secret Key**:
> Run the following command in your terminal to generate a new secure key:
> ```bash
> python3 -c 'import secrets; print(secrets.token_urlsafe(50))'
> # On Windows: python -c "import secrets; print(secrets.token_urlsafe(50))"
> ```

### 5. Apply database migrations

Initialize the database schema:

```bash
python3 manage.py migrate
# On Windows: python manage.py migrate
```

### 6. Create a superuser

Create an administrative user to access the Django Admin interface:

```bash
python3 manage.py createsuperuser
# On Windows: python manage.py createsuperuser
```

### 7. Run the development server

Start the server to access the application:

```bash
python3 manage.py runserver
# On Windows: python manage.py runserver
```

### 8. Configure Skills via Admin Panel

Before using the CV builder, you need to populate the database with the skills that will be available for selection

1. Open **[http://127.0.0.1:8000/admin/](https://www.google.com/search?q=http://127.0.0.1:8000/admin/)** in your browser
2. Log in using the **superuser credentials** you created in Step 6
3. Navigate to the **Skills** section
4. **Add your skills**: You can create and manage the list of skills available for users

The system supports various skill categories, including:

* **Web Development:** HTML, CSS, JavaScript, PHP
* **Backend & Data:** Python, SQL, Rust, C++

Once added, these skills will appear in the CV creation form
