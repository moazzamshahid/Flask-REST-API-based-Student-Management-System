from flask import Flask, request
from flask_smorest import Blueprint,abort
from flask.views import MethodView
from Schema import QuizSchema,QuizUpdateSchema
from sqlalchemy.exc import SQLAlchemyError ,IntegrityError
from models import QuizModel,EnrollementsModel
from db import  db

blp=Blueprint("Quiz",__name__,description="Operation on Quiz")

@blp.route("/Student/<int:student_id>/Course/<int:course_id>/Quiz")
class CreateQuiz(MethodView):
    @blp.arguments(QuizSchema)
    @blp.response(200,QuizSchema)
    def post(self,request_data,student_id,course_id):
        enrollement=EnrollementsModel.query.filter(EnrollementsModel.course_id==course_id,EnrollementsModel.student_id==student_id).first()
        if enrollement:
            
            quiz=QuizModel.query.filter(QuizModel.course_id==course_id,QuizModel.student_id==student_id).first()

            if quiz:
                print("hello from inside quiz")  
                abort(400,message="quiz already exists...")
            else:
                #student_id=student_id,course_id=course_id,name=request_data["name"],Total_Marks=request_data["Total_Marks"],Marks_Obtained=request_data["Marks_Obtained"]
                print(request_data)
                quiz=QuizModel(student_id=student_id,course_id=course_id,name=request_data["name"],Total_Marks=request_data["Total_Marks"],Marks_Obtained=request_data["Marks_Obtained"])
                try:
                    db.session.add(quiz)
                    db.session.commit()
                except SQLAlchemyError:
                    abort(400,message="an error occured while creating the quiz")
        else:
            abort(400,message="student not enrolled in this course...")
        return quiz
    @blp.arguments(QuizUpdateSchema)
    @blp.response(200,QuizSchema)
    def put(self,request_data,student_id,course_id):
        
        quiz=QuizModel.query.filter(QuizModel.course_id==course_id,QuizModel.student_id==student_id).first()   
        if quiz:
            quiz.name=request_data["name"]
            quiz.Total_Marks=request_data["Total_Marks"]
            quiz.Marks_Obtained=request_data["Marks_Obtained"]
        db.session.add(quiz)
        db.session.commit()
        return quiz


@blp.route("/Quiz")
class Quiz(MethodView):
    @blp.response(200,QuizSchema(many=True))
    def get(self):
       quiz= QuizModel.query.all()
       return quiz

@blp.route("/Quiz/<string:name>")
class Delete_quiz(MethodView):

    def delete(self,name):
        quiz= QuizModel.query.filter(QuizModel.name==name)
        if quiz:
            db.session.delete(quiz)
            db.session.commit()
        else:
            return {"message":"Quiz does not exist"}

        return {"message":"Quiz Deleted"}



        

        


        

        
        