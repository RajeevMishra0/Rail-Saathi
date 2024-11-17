from app.app import app, db
from flask_migrate import Migrate
# from flask_script import Manager

migrate = Migrate(app, db)

# Add migrate command to the manager
# app.add_command('db',)

if __name__ == "__main__":
    app.run(debug=True)
