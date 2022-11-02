from marshmallow import Schema,fields

class StudentPlainSchema(Schema):
    id= fields.Int(dump_only=True)
    name=fields.Str(required=True)
    roll_no=fields.Int(required=True)
    dept=fields.Str(required=True)
    batch=fields.Str(required=True)

class QuizPlainSchema(Schema):
    id= fields.Int(dump_only=True)
    name=fields.Str(required=True)
    student_id=fields.Int()
    course_id=fields.Int()
    Total_Marks=fields.Float(required=True)
    Marks_Obtained=fields.Float(required=True)

class StudentUpdateSchema(Schema):
    id= fields.Int()
    name=fields.Str()
    roll_no=fields.Int()
    dept=fields.Str()
    batch=fields.Str()

class CoursePlainSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str(required=True)
    code=fields.Str(required=True)
    semes_type=fields.Str(required=True)

class TeacherPlainSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str(required=True)
    Course_id=fields.Int()

class CourseUpdateSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str()
    code=fields.Str()
    semes_type=fields.Str()


class TeacherSchema(TeacherPlainSchema):
    Course=fields.Nested(CoursePlainSchema(),dump_only=True)


class EnrollementSchema(Schema):
    id=fields.Str(dump_only=True)

class CourseSchema(CoursePlainSchema):
    Student=fields.List(fields.Nested(StudentPlainSchema()),dump_only=True)
    teacher=fields.Nested(TeacherPlainSchema(),dump_only=True)
    quizes=fields.List(fields.Nested(QuizPlainSchema(),dump_only=True))

class StudentSchema(StudentPlainSchema):
    Courses=fields.List(fields.Nested(CoursePlainSchema(),dump_only=True))
    quizes=fields.List(fields.Nested(QuizPlainSchema(),dump_only=True))

class QuizUpdateSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str()
    student_id=fields.Int(required=True)
    course_id=fields.Int(required=True)
    Total_Marks=fields.Float()
    Marks_Obtained=fields.Float()


class QuizSchema(QuizPlainSchema):
    student=fields.Nested(StudentPlainSchema(),dump_only=True)
    Courses=fields.Nested(CoursePlainSchema(),dump_only=True)

class UserSchema(Schema):
    id=fields.Int(dump_only=True)
    username=fields.Str(required=True)
    password=fields.Str(required=True)
    account_type=fields.Str()
    user_id=fields.Int()
    

