from db import db

class TeacherModel(db.Model):

    __tablename__="teachers"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80),unique=True,nullable=False)
    Course_id=db.Column(db.Integer,db.ForeignKey("Courses.id"),nullable=True)

    Course=db.relationship("CourseModel", back_populates="teacher")
    teacher_user=db.relationship("TeacherUserModel", back_populates="teacher",uselist=False)




