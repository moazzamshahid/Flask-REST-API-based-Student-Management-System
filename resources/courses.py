from flask import Flask, request
from flask_smorest import abort,Blueprint
from flask.views import MethodView
from Schema import CourseSchema,CourseUpdateSchema
from models import CourseModel
from sqlalchemy.exc import SQLAlchemyError ,IntegrityError
import uuid
from db import db

blp=Blueprint("Courses",__name__,description="operation on courses")

@blp.route("/course")
class Courselist(MethodView):
    @blp.response(200,CourseSchema(many=True))
    def get(self):
        Course=CourseModel.query.all()
        return Course
    @blp.arguments(CourseSchema)
    @blp.response(200,CourseSchema)
    def post(self,request_data):
        course=CourseModel(**request_data)  
        try:
            db.session.add(course)
            db.session.commit()
        except IntegrityError:
            return {"message":"Course already Exists"}
        except SQLAlchemyError:
            return {"message":"Error inserting data"}
        return course
@blp.route("/course/<string:id>")
class course_(MethodView):
    @blp.response(200,CourseSchema)
    def get(self,id):
        course=CourseModel.query.get_or_404(id)
        return course
    @blp.arguments(CourseUpdateSchema)
    @blp.response(200,CourseSchema)
    def put(self,request_data,id):
        course=CourseModel.query.get(id)
        if course:
            course.name=request_data["name"]
            course.code=request_data["code"]
            course.semes_type=request_data["semes_type"]
        else:
            course=CourseModel(id=id,**request_data)
        db.session.add(course)
        db.session.commit()

        return course
            

    def delete(self,id):
        course=CourseModel.query.get_or_404(id)
        db.session.delete(course)
        db.session.commit()
        return {"message":"course deleted..."}

