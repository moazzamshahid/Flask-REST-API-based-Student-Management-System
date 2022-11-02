from flask import Flask,request
from flask_smorest import Blueprint,abort
from flask.views import MethodView
from models import StudentModel,CourseModel
from Schema import CourseSchema, EnrollementSchema, StudentSchema
from sqlalchemy.exc import SQLAlchemyError
from db import db
import uuid

from resources.courses import course_

blp=Blueprint("Enrollement",__name__,description="Operation on Enrollements")

@blp.route("/Student/<string:student_id>/Course/<string:Course_id>")
class Student_Course_Enrollement(MethodView):
    def delete(self,student_id,Course_id):
        student=StudentModel.query.get_or_404(student_id)
        course=CourseModel.query.get_or_404(Course_id)
        student.Courses.remove(course)
        try:
            db.session.add(student)
            db.session.commit()
        except SQLAlchemyError:
            abort(500,message="an error occured while deletting tag")
        return {"message":"enrollement removed"}


    @blp.response(200,CourseSchema)
    def post(self,student_id,Course_id):
        student=StudentModel.query.get_or_404(student_id)
        course=CourseModel.query.get_or_404(Course_id)
        student.Courses.append(course)
        try:
            db.session.add(student)
            db.session.commit()
        except SQLAlchemyError:
            abort(500,message="an error occured while inserting tag")
        return course
        


@blp.route("/student/<string:student_id>/Enrollement")  
class Enrollement_(MethodView):
#need to change accoring to tags
    @blp.response(200,StudentSchema)
    def get(self,student_id):
       student=StudentModel.query.get_or_404(student_id)
       return student





