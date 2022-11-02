from db import db


class StudentModel(db.Model):
    __tablename__="Students"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),unique=True,nullable=False)
    roll_no=db.Column(db.Integer,unique=True,nullable=False)
    dept=db.Column(db.String(80),unique=False,nullable=False)
    batch=db.Column(db.String(80),unique=False,nullable=False)

    Courses=db.relationship("CourseModel",back_populates="Student",secondary="Enrollements")
    quizes=db.relationship("QuizModel",back_populates="student", lazy="dynamic")
    student_user=db.relationship("StudentUserModel", back_populates="student")


