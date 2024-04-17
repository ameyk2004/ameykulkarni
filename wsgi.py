from app import create_app
app = create_app()


if __name__ == "__main__":
    # waitress-serve --listen=127.0.0.1:8000 wsgi:app
    app.run(port=5001)

# Build Command : pip install -r requirements.txt
# Run Command waitress-serve --listen=127.0.0.1:8000 wsgi:app