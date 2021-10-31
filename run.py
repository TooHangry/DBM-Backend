from app import start_app

if __name__ == '__main__':
    start_app = start_app()
    start_app.run()
else:
    gunicorn_app = start_app()