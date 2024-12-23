# Patient Information Management Application

This is a Flask web application for managing patient information. It allows users to enter, view, and manage patient data efficiently.

## Project Structure

```
patient-info-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   └── templates
│       ├── base.html
│       ├── index.html
│       └── patient.html
├── migrations
├── static
│   ├── css
│   │   └── styles.css
│   ├── js
│   │   └── scripts.js
│   └── images
├── tests
│   ├── __init__.py
│   └── test_app.py
├── .flaskenv
├── config.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd patient-info-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   - Configure your database settings in `config.py`.
   - Run migrations to set up the database schema.

5. **Run the application:**
   ```
   flask run
   ```

## Usage

- Navigate to the home page to enter patient information.
- View patient details by selecting a patient from the list.

## Testing

To run the tests, use the following command:
```
pytest
```

## License

This project is licensed under the MIT License.