# Phoxia 💻


It's a  wallpaper app which  is  made  HTML,CSS,Javascript,Bootstrap-4 ,and as a backend Django framework.


## Steps to Run the Project

1. **Clone the repository**
    ```bash
    $ git clone <repository-url>
    $ cd Phoxia
    ```

2. **Create and activate a virtual environment**
    ```bash
    $ python -m venv venv
    $ venv\Scripts\activate    # on Mac: source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    $ pip install -r requirements.txt
    ```

4. **Apply migrations**
    ```bash
    $ python manage.py makemigrations
    $  python manage.py migrate
    ```
5. **Create a superuser**
    ```bash
    $ python manage.py createsuperuser
    ```


6. **Run the development server**
    ```bash
    $  python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/login` to view the app.