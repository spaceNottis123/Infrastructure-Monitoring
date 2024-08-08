from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

#init the flask app
app = Flask(__name__)
app.config.from_object(Config)

#init SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)


#init the routes
from routes import *

#error
@app.errorhandler(404)
def not_found_error(error):
    return {"message": "Not Found"}, 404

@app.errorhandler(500)
def internal_erro(error):
    return {"message": "Internal Server Error"}, 500

if __name__ == "__main__":
    app.run(debug=True)
