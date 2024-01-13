# 0x0A. Python - Inheritance

## Superclass, Baseclass, or Parentclass
- A superclass, baseclass, or parentclass is a class that is extended or inherited by another class. It provides common attributes and methods to its subclasses.

## Subclass
- A subclass is a class that inherits attributes and methods from another class, known as its superclass. It can also have its own attributes and methods.

## Listing Attributes and Methods
- To list all attributes and methods of a class or instance, you can use the built-in `dir()` function. Example:
    ```python
    print(dir(MyClass))
    ```

## Adding New Attributes
- An instance can have new attributes at any time. Simply assign a value to a new attribute, and it becomes part of the instance.

## Inheriting from Another Class
- To inherit from another class, include the parent class in parentheses when defining the subclass. Example:
    ```python
    class SubClass(ParentClass):
        # subclass attributes and methods
    ```

## Defining a Class with Multiple Base Classes
- To define a class with multiple base classes, list them in the parentheses separated by commas. Example:
    ```python
    class SubClass(BaseClass1, BaseClass2):
        # subclass attributes and methods
    ```

## Default Class Inheritance
- Every class in Python inherits from the built-in `object` class by default.

## Method or Attribute Override
- To override a method or attribute inherited from the base class, define a method or attribute with the same name in the subclass.

## Inherited Attributes and Methods
- Subclasses inherit attributes and methods from their superclass. They can access and use them as if they were defined in the subclass.

## Purpose of Inheritance
- Inheritance allows code reuse, promotes code organization, and supports the creation of specialized classes based on existing ones.

## Using `isinstance`, `issubclass`, `type`, and `super`
- `isinstance(obj, class)` checks if `obj` is an instance of `class`.
- `issubclass(subclass, superclass)` checks if `subclass` is a subclass of `superclass`.
- `type(obj)` returns the type of `obj`.
- `super()` is used to call methods from the superclass.