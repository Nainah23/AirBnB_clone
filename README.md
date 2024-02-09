# README.md

## AirBnB Clone Project

This repository contains the implementation of an AirBnB clone, a project focused on building a command-line interpreter and various classes representing entities in the AirBnB ecosystem.

### Project Overview

The project is structured as follows:

1. **pycodestyle Compliance**
   - Ensure all code is written in compliance with pycodestyle checks.

2. **Unit Tests**
   - All files, classes, and functions must be thoroughly tested using unit tests.

3. **BaseModel Class**
   - Implement a `BaseModel` class with the following features:
     - Public instance attributes: `id`, `created_at`, `updated_at`.
     - Public instance methods: `save(self)` and `to_dict(self)`.
     - Define the serialization/deserialization process.

4. **Create BaseModel from Dictionary**
   - Enhance the `BaseModel` class to recreate an instance from a dictionary representation.

5. **Store First Object**
   - Introduce a class `FileStorage` to serialize instances to a JSON file and deserialize JSON files to instances.

6. **Console 0.0.1**
   - Develop a command-line interface (`console.py`) using the `cmd` module with basic functionalities:
     - `quit` and `EOF` to exit the program.
     - `help` for documentation.
     - Custom prompt: `(hbnb)`.

7. **Console 0.1**
   - Update the command interpreter to include commands for creating, showing, destroying, updating, and listing instances.

8. **First User**
   - Create a class `User` that inherits from `BaseModel` with attributes: `email`, `password`, `first_name`, and `last_name`.

9. **More Classes**
   - Implement additional classes that inherit from `BaseModel`: `State`, `City`, `Amenity`, `Place`, and `Review`.

10. **Console 1.0**
    - Update `FileStorage` to handle serialization and deserialization for all new classes.
    - Enhance the command interpreter to support actions for all created classes.

11. **All Instances by Class Name**
    - Advanced: Allow retrieving all instances of a class using `<class name>.all()`.

12. **Count Instances**
    - Advanced: Retrieve the number of instances of a class using `<class name>.count()`.

13. **Show Instance by ID**
    - Advanced: Retrieve an instance based on its ID using `<class name>.show(<id>)`.

14. **Destroy Instance by ID**
    - Advanced: Destroy an instance based on its ID using `<class name>.destroy(<id>)`.

15. **Update Instance by ID**
    - Advanced: Update an instance based on its ID using `<class name>.update(<id>, <attribute name>, <attribute value>)`.

16. **Update from Dictionary**
    - Advanced: Update an instance based on its ID with a dictionary using `<class name>.update(<id>, <dictionary representation>)`.

17. **Unittests for the Console!**
    - Advanced: Write comprehensive unittests for `console.py` covering all features.

### Authors

This project is a collaborative effort, and contributions are acknowledged. The list of authors is maintained in the [AUTHORS](AUTHORS) file.
