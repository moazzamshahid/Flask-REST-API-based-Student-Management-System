from db import db


class TeacherUserModel(db.Model):
    __tablename__="TeacherUsers"

    id= db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),nullable=False, unique=True)
    password=db.Column(db.String(80),nullable=False, unique=True)
    Teacher_id=db.Column(db.Integer, db.ForeignKey("teachers.id"), nullable=True,unique=True)
    teacher = db.relationship("TeacherModel", back_populates="teacher_user")

class StudentUserModel(db.Model):
    __tablename__="StudentUsers"
    
    id= db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),nullable=False, unique=True)
    password=db.Column(db.String(80),nullable=False, unique=True)
    Student_id=db.Column(db.Integer,db.ForeignKey("Students.id"),nullable=False, unique=True)
    student=db.relationship("StudentModel", back_populates="student_user")


class AdminUserModel(db.Model):
    __tablename__="AdminUsers"
    
    id= db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),nullable=False, unique=True)
    password=db.Column(db.String(80),nullable=False, unique=True)









