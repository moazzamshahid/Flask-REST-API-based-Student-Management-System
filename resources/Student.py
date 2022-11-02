from flask import Flask, request
from flask_smorest import Blueprint,abort
from flask.views import MethodView
from Schema import StudentSchema,StudentUpdateSchema
from sqlalchemy.exc import SQLAlchemyError ,IntegrityError
from models import StudentModel
from db import db
import uuid


blp =Blueprint("Student",__name__,description="Operation on Student")


@blp.route("/student")
class Studentlist(MethodView): # MethodView is a class within the flask.views module of the Flask project. MethodView is a Python Metaclass that determines the methods, such as GET, POST, PUT, etc, that a view defines.
    @blp.response(200,StudentSchema(many=True))
    def get(self):
        student=StudentModel.query.all()
        return student
    @blp.arguments(StudentSchema)
    @blp.response(200,StudentSchema)
    def post(self,request_data):
        new_student=StudentModel(**request_data)  
        try:
            db.session.add(new_student)
            db.session.commit()
        except IntegrityError:
            abort(400,message="Student already exists")
        except SQLAlchemyError:
            abort(500,message="an error occured while creating the student")
        return new_student


@blp.route("/student/<string:id>")
class student_(MethodView):
    @blp.response(200,StudentSchema)
    def get(self,id):
        student=StudentModel.query.get_or_404(id)
        return student
    
    @blp.arguments(StudentUpdateSchema)
    @blp.response(200,StudentSchema)
    def put(self,request_data,id):
        student=StudentModel.query.get(id)
        if student:
            student.name=request_data["name"]
            student.roll_no=request_data["roll_no"]
            student.dept=request_data["dept"]
            student.batch=request_data["batch"]
        else:
            student=StudentModel(id=id,**request_data)
        db.session.add(student)
        db.session.commit()
        return student

    def delete(self,id):
        student=StudentModel.query.get_or_404(id)
        try:
            db.session.delete(student)
            db.session.commit()
        except IntegrityError:
            return {"message":"delete enrollement firsts..."}

        return {"message": "Student romoved"}


            

                




        


    

