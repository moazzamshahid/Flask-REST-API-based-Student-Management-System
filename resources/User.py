from flask import Flask
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from Schema import UserSchema
from sqlalchemy.exc import SQLAlchemyError ,IntegrityError
from flask_jwt_extended import jwt_required,create_access_token,get_jwt
from db import db
from models import StudentUserModel,TeacherUserModel,AdminUserModel
from passlib.hash import pbkdf2_sha256
from blocklist import BLOCKLIST

blp=Blueprint("User",__name__,description="Operation on Users")


@blp.route("/register")
class RegisterUser(MethodView):
    @blp.arguments(UserSchema)
    def post(self,request_data):
        try:
            if request_data["account_type"]=="student":
                print(request_data)
                user=StudentUserModel.query.filter(StudentUserModel.username==request_data["username"]).first()
                if user:
                    abort(400,message="user already exists")
                else:
                    user=StudentUserModel(username=request_data["username"],password=pbkdf2_sha256.hash(request_data["password"]),Student_id=request_data["user_id"]) 
                    db.session.add(user)
                    db.session.commit()
                    return {"message":"user created successfully"}
            elif request_data["account_type"]=="teacher":
                user=TeacherUserModel.query.filter(TeacherUserModel.username==request_data["username"]).first()
                if user:
                    abort(400,message="User already exists")
                else:
                    user=TeacherUserModel(username=request_data["username"],password=pbkdf2_sha256.hash(request_data["password"]),Teacher_id=request_data["user_id"]) 
                    db.session.add(user)
                    db.session.commit()
                    return {"message":"User created successfully"}
            elif request_data["account_type"]=="admin":
                user=AdminUserModel.query.filter(AdminUserModel.username==request_data["username"]).first()
                if user:
                    abort(400,message="User already exists")
                else:
                    user=AdminUserModel(username=request_data["username"],password=pbkdf2_sha256.hash(request_data["password"])) 
                    db.session.add(user)
                    db.session.commit()
                    return {"message":"User created successfully"}
            else:
                    return{"message":"invalid account_type"}
        except IntegrityError:
            return{"message":"One User can have only one account"}



@blp.route("/register/student")
class Student_Users(MethodView):
    @blp.response(200,UserSchema(many=True))
    def get(self):
         user=StudentUserModel.query.all()
         return user

@blp.route("/register/teacher")
class teacher_Users(MethodView):
    @blp.response(200,UserSchema(many=True))
    def get(self):
         user=TeacherUserModel.query.all()
         return user

@blp.route("/register/admin")
class admin_Users(MethodView):
    @blp.response(200,UserSchema(many=True))
    def get(self):
         user=AdminUserModel.query.all()
         return user


@blp.route("/login")
class LoginUser(MethodView):
    @blp.arguments(UserSchema)
    def post(self,request_data):
        if request_data["account_type"]=="student":
            user=StudentUserModel.query.filter(StudentUserModel.username==request_data["username"]).first()
            if user and pbkdf2_sha256.verify(request_data["password"],user.password):
                access_token = create_access_token(identity=str(user.id) +" student",fresh=True)
                return {"access_token":access_token}
        elif request_data["account_type"]=="teacher":
            user=TeacherUserModel.query.filter(TeacherUserModel.username==request_data["username"]).first()
            if user and pbkdf2_sha256.verify(request_data["password"],user.password):
                access_token = create_access_token(identity=str(user.id) +" teacher",fresh=True)
                return {"access_token":access_token}
        elif request_data["account_type"]=="admin":
            user=AdminUserModel.query.filter(AdminUserModel.username==request_data["username"]).first()
            if user and pbkdf2_sha256.verify(request_data["password"],user.password):
                access_token = create_access_token(identity=str(user.id) +" admin",fresh=True)
                return {"access_token":access_token}
    
        abort(401,message="invalid user")

@blp.route("/logout")
class LogoutUser(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200
        
        


        
     
