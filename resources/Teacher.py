from flask import Flask
from flask_smorest import Blueprint,abort
from flask.views import MethodView
from Schema import TeacherSchema
from sqlalchemy.exc import SQLAlchemyError ,IntegrityError
from models import TeacherModel
from db import db
import uuid

blp =Blueprint("Teacher",__name__,description="Operation on Teacher")

@blp.route("/Teacher")
class Teacher(MethodView):
    @blp.arguments(TeacherSchema)
    @blp.response(200,TeacherSchema)
    def post(self,request_data):
        Teacher=TeacherModel(**request_data)
        try:
            db.session.add(Teacher)
            db.session.commit()
        except IntegrityError:
            abort(400,message="Teacher already exists")
        except SQLAlchemyError:
            abort(500,message="an error occured while creating the Teacher")
        return Teacher
    @blp.response(200,TeacherSchema(many=True))
    def get(self):
        teacher=TeacherModel.query.all()
        return teacher


@blp.route("/Teacher/<int:id>")
class UpdateorDelete(MethodView):
    @blp.response(200,TeacherSchema)
    def get(self,id):
        Teacher=TeacherModel.query.get_or_404(id)
        return Teacher

    @blp.arguments(TeacherSchema)
    @blp.response(200,TeacherSchema)
    def put(self,request_data,id):
        
        Teacher=TeacherModel.query.get_or_404(id)
        Teacher.name=request_data["name"]
        Teacher.Course_id=request_data["Course_id"] 
        db.session.add(Teacher)
        db.session.commit()
        return Teacher  

    def delete(self,id):
        Teacher=TeacherModel.query.get_or_404(id)
        db.session.delete(Teacher)
        db.session.commit()
        return {"message":"Teacher Deleted"}
