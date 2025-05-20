from sqlalchemy import Column,Integer,String,ForeignKey,Table 
from sqlalchemy.orm import relationship
from .database import Base

workout_routine_association = Table (
    'workout_routine', Base.metadata,
    Column('workout_id', Integer, ForeignKey('workouts.id')),
    Column('routine_id', Integer, ForeignKey('routines.id'))
)

