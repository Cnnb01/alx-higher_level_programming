## Python - Classes and Objects

### Classes

A class is a blueprint or template for creating objects. It defines the attributes and methods that an object will have. Classes can be thought of as user-defined data types that encapsulate data and behavior. Classes can also inherit attributes and methods from other classes, a concept known as inheritance.

### Objects

An object is an instance of a class, created from a class. Objects inherit the attributes and methods defined by the class. Objects are the actual entities that we interact with in a program, and they represent the data and behavior defined by their class.

### Instance vs. Object

While the terms "instance" and "object" are often used interchangeably, they do have slightly different connotations:

- An instance is a specific occurrence of a class, like a house built from a blueprint.
- An object is a more general concept that can refer to anything in Python, including classes, functions, and modules.

### Properties vs. Getters and Setters

In Python, properties and getters/setters are used to manage attributes of an object:

- **Properties**:
  - Properties are a built-in feature of Python that allow for controlled access to attributes using methods, called getters and setters.
  - They are the Pythonic way to add behavior to attributes while avoiding breaking changes in APIs.
  - They provide a more flexible and integrated approach to managing attribute access and mutation.

- **Getters and Setters**:
  - Getters and setters are traditional methods used to access and modify the attributes of an object.
  - They make it explicit that accessing or mutating an attribute happens through a method call.
  - They allow for more complicated data access than simple attribute access.
  - They can be preferred over properties in situations where you need to run extra arguments and flags, use inheritance, or raise exceptions related to attribute access and mutation.

### Methods

Methods are functions that are defined inside a class and operate on an object of that class. They can access and modify the attributes of the object. Methods are called on objects and can access and modify their attributes.

### Attributes

Attributes are pieces of data that belong to an object. They can be accessed and modified using dot notation. Attributes can be instance attributes or class attributes. Instance attributes are specific to an object and are initialized in the constructor. Class attributes are shared by all instances of the class and are initialized in the class.

### Inheritance and Polymorphism

Inheritance is a concept in object-oriented programming where a class inherits attributes and methods from another class. In Python, a class can inherit from another class using the `inherit` keyword. Polymorphism is a concept where a single interface can be used by different classes to implement different functions. In Python, a class can implement a polymorphic interface using the `__abc__.ABC` class.

### Docstrings

Docstrings are docstrings are string literals that are used to document Python modules, classes, functions, and methods. They are accessed using the `__doc__` attribute. Docstrings should provide a brief summary of the purpose and behavior of the module, class, function, or method, along with any required or optional arguments, and side effects.

### Error Handling

Error handling in Python is crucial for writing robust and reliable software. Exceptions are objects that represent errors or unexpected situations. Python provides several built-in exception classes, and you can define your own custom exception classes as well. To handle errors, you can use `try` and `except` blocks to catch and handle exceptions.

### Dynamic Dispatch

Dynamic dispatch is a concept in object-oriented programming where the method to be called is determined at runtime, rather than at compile time. In Python, this is achieved using the `virtualmethod` table, which is a table that contains pointers to the method implementations for each method defined in a class. When a method is called on an object, the method lookup in the virtual method table returns the correct method implementation to be executed.

### Summary

In summary, Python classes and objects are the building blocks of object-oriented programming in Python. Classes are blueprints for creating objects, while objects are specific occurrences of those classes. Attributes and methods are used to store data and behavior, respectively. Properties, getters, and setters are used to manage access to object attributes. Methods are functions that operate on objects and can access and modify their attributes. Inheritance and polymorphism are key concepts in object-oriented programming, and error handling is essential for writing robust software.
