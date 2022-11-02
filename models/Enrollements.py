from db import db


class EnrollementsModel(db.Model):
    __tablename__="Enrollements"
    id=db.Column(db.Integer,primary_key=True)
    student_id=db.Column(db.Integer,db.ForeignKey("Students.id"),nullable=False,unique=False)
    course_id=db.Column(db.Integer,db.ForeignKey("Courses.id"),nullable=False,unique=False)





