from db import db


class CourseModel(db.Model):
    __tablename__="Courses"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),unique=True,nullable=False)
    code=db.Column(db.Integer,unique=True,nullable=False)
    semes_type=db.Column(db.String(80),unique=False,nullable=False)
    
    Student=db.relationship("StudentModel",back_populates="Courses",secondary="Enrollements")
    teacher=db.relationship("TeacherModel", back_populates="Course" ,uselist=False)
    quizes=db.relationship("QuizModel", back_populates="Courses", lazy="dynamic")