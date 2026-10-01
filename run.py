from app import create_app

app = create_app()

if __name__ == '__main__':
    # In production, use a WSGI server like gunicorn
    # e.g., gunicorn -w 4 run:app
    app.run()
