from datetime import datetime
from sqlalchemy import (Column, Integer, String, DateTime, CheckConstraint, UniqueConstraint, create_engine)
from sqlalchemy.ext.declarative import declarative_base

# Define database engine
engine = create_engine('sqlite:///migrations_test.db')

# Define base class
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'
    
    # Constraints
    __table_args__ = (
        UniqueConstraint('email', name='unique_email'),
        CheckConstraint('grade BETWEEN 1 AND 12', name='grade_between_1_and_12')
    )

    # Columns
    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"Student {self.id}: {self.name}, Grade {self.grade}"
