"""professor.py: create a table named professors in the marist database"""
from db.db import db

class Professor(db.Model):
    __tablename__ = 'Professors'
    ProfessorID = db.Column(db.Integer,primary_key=True, autoincrement=True)

    # create relationship with courses table. assoc table name = ProfessorCourse
    course = db.relationship('Courses', secondary = 'ProfessorCourse', back_populates = 'Professors')
    def __init__(self):
        # remove pass and then initialize attributes
        pass

    def __repr__(self):
        # add text to the f-string
        return f"""

        """
    
    def __repr__(self):
        return self.__repr__()