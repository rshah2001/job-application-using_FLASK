# Flask Form Submission App

This Flask application allows users to submit a form with personal details, which are then stored in a SQLite database. Upon submission, a confirmation email is sent to the user.

## Features

- Collects user information through a form (first name, last name, email, date, and occupation).
- Stores form data in a SQLite database.
- Sends a confirmation email to the user after form submission.
- Flash messages are used to provide feedback to the user.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.6+
- Flask
- Flask-SQLAlchemy
- Flask-Mail
- python-dotenv

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/flask-form-app.git
   cd flask-form-app
Create a Virtual Environment:
bash
Copy code
python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install Dependencies:
bash
Copy code
pip install -r requirements.txt
Create a .env.local File:
In the root directory of the project, create a .env.local file and add the following environment variables:

# .env.local
SECRET_KEY=myapp@13123

SQLALCHEMY_DATABASE_URI=sqlite:///data.db

MAIL_SERVER=smtp.gmail.com

MAIL_PORT=465

MAIL_USE_SSL=True

MAIL_USERNAME=your_email@gmail.com

MAIL_PASSWORD=your_email_password

Ensure .env.local is Ignored by Git:

Make sure .env.local is listed in your .gitignore file to avoid committing sensitive information:

gitignore
Copy code
.env.local
Run the Application:
Before running the application, ensure the database is created by running:

bash
Copy code
python main.py
This will start the Flask development server. Visit http://127.0.0.1:5001/ in your browser.

## Usage

Fill out the form on the main page with your first name, last name, email, date, and occupation.

Submit the form.

A confirmation email will be sent to the email address provided, and the form details will be stored in the SQLite database.

## Project Structure

main.py: The main Flask application file.

templates/: Directory containing the HTML template(s).

data.db: SQLite database file (created after running the application).

.env.local: File containing environment variables (should not be committed to version control).

## Troubleshooting

Ensure your .env.local file is properly formatted and includes all necessary environment variables. If the confirmation email is not sent, check that your email settings in .env.local are correct.
Make sure you have an active internet connection for the email functionality.
