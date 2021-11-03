#!/usr/bin/python3
"""
Write a class called BaseModel.
"""
import uuid
import datetime
import time


Class BaseModel:
	"""
	class BaseModel defines all common
	attributes/methods for other classes.
	Methods:
		save(self)
		to_dict(self)
		__str__(self)
	"""
	def __init__(self, id = None, methodcreated_at=None, updated_at=None):
        """
        Initialization function.
        If id is not None, 
        Attributes:
            id: string - assign with an uuid when an instance is created.
			created_at: datetime - assign with the current datetime
			when an instance is created.
			updated_at: datetime - assign with the current datetime when
			an instance is created and it will be updated every time you
			change your object.
        """
		self.id = str(uuid.uuid4())
		self.created_at = datetime.datetime.now()
		self.updated_at = datetime.datetime.now()

	def __str__(self):
        """
        Function that prints [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{:s}] ({:d}) {:d}".format(
            self.__class__.__name__, self.id, self.__dict__)
	
	def save(self):
		"""
		Updates the public instance attribute updated_at with the current
		datetime.
        """
		self.updated_at = datetime.datetime.now()
	
	def to_dict(self):
		"""
		xxxxxxxx
        """
		convert_dict = self.__dict__
		
		return {'__class__': self.__class__.__name__, self.updated_at.__dict__}

		# return {'__class__': self.__class__.__name__, 'updated_at' : created_at.isoformat(), 'created_at' : created_at.isoformat()}



