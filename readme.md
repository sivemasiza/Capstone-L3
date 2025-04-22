# Garden App

Welcome to the **Garden App**! This is a Django-based web application where users can sign up, log in, and interact with various features, including a blog and polls. The app allows users to vote on polls related to gardening and view blog posts.

## Features

- **User Authentication**: Users can create an account, log in, and manage their profiles.
- **Blog**: A blog section where users can post, read, and interact with gardening-related articles.
- **Polls**: Users can participate in polls related to gardening topics, such as favorite plants, gardening techniques, and more.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS (Bootstrap for styling)
- **Database**: SQLite (for development) or PostgreSQL (recommended for production)
- **Authentication**: Django's built-in authentication system

## Requirements

To run the app locally, you need to have Python 3.x and Django installed. You can use `pip` to install the necessary dependencies.

### Python and Django Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/garden-app.git
   cd garden-app
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Setting Up the Database

Before running the application, you need to set up the database and apply the migrations.

1. Run migrations:

   ```bash
   python manage.py migrate
   ```

2. Create a superuser to access the Django admin panel (optional but recommended):

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up an admin user.

## Running the Application

To start the development server, run the following command:

```bash
python manage.py runserver
```

You can now access the application at `http://127.0.0.1:8000/`.