# Electronic Health Records (EHR) System

## Overview
The **5G Emergency Smart Ambulance EHR System** is a web-based application designed to manage patient records efficiently and intuitively. Built using the Django framework, this application allows users to add, search, and manage patient information, making it a valuable tool for emergency healthcare environments.

---

## Features
1. **User Authentication:**
   - Login and logout functionality for secure access.

2. **Patient Management:**
   - Add new patient records.
   - Search and view patient details.
   - Update or delete patient records as required.

3. **Dashboard Overview:**
   - Provides statistics, including total patients, recent additions, and patients flagged as at risk.
   - Quick links for ease of navigation.

4. **Responsive Design:**
   - Optimized for various devices using custom CSS.

---

## Technologies Used
- **Backend:** Python (Django Framework)
- **Frontend:** HTML, CSS
- **Database:** SQLite (default Django database)
- **Version Control:** Git
- **Static File Handling:** Django’s `static` module

---

## File Structure
```
project_root/
|— ehr_app/
|   |— migrations/        # Django migrations
|   |— static/
|   |   |— css/
|   |       |— style.css   # Custom styles for the app
|   |— templates/
|       |— ehr_app/
|           |— base.html   # Base template with shared layout
|           |— dashboard.html  # Dashboard view template
|           |— add_patient.html  # Add patient form
|           |— search_patient.html # Search patient form
|   |— views.py            # Application views
|   |— models.py           # Database models for patient data
|   |— urls.py             # URL routing for the app
|   |— forms.py            # Django forms for patient management
|— project_root/
    |— settings.py         # Django project settings
    |— urls.py             # Project-level URL configurations
    |— wsgi.py             # WSGI application
```

### Key Files and Their Purpose
- **models.py:** Defines the database schema, including the `Patient` model.
- **views.py:** Contains the logic for rendering pages and handling user requests.
- **forms.py:** Defines forms for adding and updating patient records.
- **base.html:** Base template that contains the shared header and footer layout.
- **style.css:** Provides custom styling for the application.
- **urls.py:** Maps URL paths to their corresponding views.

---

## Installation and Setup
1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate   # For Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
   Access the app at `http://127.0.0.1:8000/`.

---

## Usage Instructions
1. **Login:** Use the provided credentials to log in.
2. **Dashboard:** Access an overview of the patient data.
3. **Add Patient:** Navigate to "Add Patient" and fill in the required details.
4. **Search Patient:** Use the search functionality to find specific patient records.

---

## Deployment
### Using Gunicorn and Nginx (Production Example)
1. **Collect Static Files:**
   ```bash
   python manage.py collectstatic
   ```

2. **Install Gunicorn:**
   ```bash
   pip install gunicorn
   ```

3. **Start Gunicorn:**
   ```bash
   gunicorn project_root.wsgi:application
   ```

4. **Configure Nginx:** Point your Nginx configuration to the Gunicorn socket.

---

## Troubleshooting
- **Static Files Not Loading:**
   Ensure `STATICFILES_DIRS` is correctly set in `settings.py` and run `collectstatic` if in production.
- **Database Issues:**
   Check the database file permissions and ensure migrations are applied correctly.

---

## Future Enhancements
- Integration with IoT devices for real-time patient data updates.
- Advanced analytics to predict patient risks.
- Multi-language support for international deployment.

---

## Contributing
Feel free to contribute by submitting pull requests or reporting issues. For major changes, please open an issue to discuss proposed modifications.

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---

## Contact
**Developer:** Tadiwanashe Mabhudhu  
**Email:** mabhudhutt@gmail.com

