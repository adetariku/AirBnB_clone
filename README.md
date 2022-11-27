This repository is the first part of ALX project to implement a cloned vesion of AirBnB website.The complete version will have the following.
  	A command interpreter to manipulate data without a visual interface, like a shell (for development and debugging)

	A website (front-end) with static and dynamic functionalities

	A comprehensive database to manage the backend functionalities
	An API that provides a communication interface between the front and backend of the system.



Files and Directories
models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
tests directory will contain all unit tests.
console.py file is the entry point of our command interpreter.
models/base_model.py file is the base class of all our models. It contains common elements:
attributes: id, created_at and updated_at
methods: save() and to_json()
models/engine directory will contain all storage classes (using the same prototype). For the moment I will have only one: file_storage.py.
The project's implementation will happen in the following phases:



REMAZRKS:

