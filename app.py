from flask import Flask
from flask_cors import CORS
from resources.Student import blp as Student_blp
from resources.courses import blp as course_blp
from resources.Enrollement import blp as Enrollement_blp
from resources.Teacher import blp as Teacher_blp
from resources.Quiz import blp as Quiz_blp
from resources.User import blp as User_blp
from db import db
from flask_smorest import Api
from flask_jwt_extended import JWTManager
import os
import secrets



app=Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"]=True
app.config["API_TITLE"]="STORES REST API"
app.config["API_VERSION"]="v1"
app.config["OPENAPI_VERSION"]= "3.0.3"
app.config["OPENAPI_URL_PREFIX"]="/"
app.config["OPENAPI_SWAGGER_UI_PATH"]="/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"]="https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL","sqlite:///data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATOIN"]=False

db.init_app(app)
CORS(app)

@app.before_first_request
def create_table():
    db.create_all()

app.config["JWT_SECRET_KEY"] = str(secrets.SystemRandom().getrandbits(128))
jwt=JWTManager(app)

@jwt.additional_claims_loader
def add_claim_to_jwt(identity):
    if "student" in identity:
        return {"is_user":"student"}
    elif "teacher" in identity :
        return {"is_user":"teacher"}
    elif "admin" in identity:
        return {"is_user":"admin"}

api=Api(app)
api.register_blueprint(Student_blp)
api.register_blueprint(course_blp)
api.register_blueprint(Enrollement_blp)
api.register_blueprint(Teacher_blp)
api.register_blueprint(Quiz_blp)
api.register_blueprint(User_blp)



