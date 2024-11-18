from app import create_app, db

# Initialize the Flask app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
