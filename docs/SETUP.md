# Installation Guide

Follow these steps to set up the CRM project on your local machine.

## Prerequisites
- Python 3.x installed
- Git installed

## Steps

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/crm-project.git](https://github.com/mostafa3ttar/Django-Build-CRM.git)
   cd crm-project

2. Create and activate a virtual environment:
# Windows:
python -m venv venv
venv\Scripts\activate

# Linux/macOS:
python -m venv venv
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Configure Environment Variables:
Create a .env file in the root directory and add:
SECRET_KEY=
DEBUG=

5. Run migrations and start the server:
python manage.py migrate
python manage.py runserver

