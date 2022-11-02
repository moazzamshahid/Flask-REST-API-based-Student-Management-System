from db import db

class QuizModel(db.Model):
    __tablename__="Quizes"
    id= db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),unique=False,nullable=False)
    Total_Marks=db.Column(db.Float(precision=2), nullable=False)
    Marks_Obtained=db.Column(db.Float(precision=2), nullable=False)
    student_id=db.Column(db.Integer, db.ForeignKey("Students.id"),unique=False, nullable=False)
    course_id=db.Column(db.Integer, db.ForeignKey("Courses.id"), unique=False,nullable=False)

    student=db.relationship("StudentModel", back_populates="quizes")
    Courses=db.relationship("CourseModel", back_populates="quizes")

    
