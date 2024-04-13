# Python - More Data Structures: Set, Dictionary, Lambda, Filter, Reduce, Map

This repository covers various concepts related to advanced data structures and functional programming in Python. The topics covered include Sets, Dictionaries, Lambda functions, Filter, Reduce, and Map.

## Sets

### Overview
- A set is an unordered collection of unique elements.
- It is defined using curly braces {} or the set() constructor.
- Sets automatically eliminate duplicate elements.

### Common Set Operations
1. *Adding Elements:*
   python
   my_set = {1, 2, 3}
   my_set.add(4)
   

2. *Removing Elements:*
   python
   my_set = {1, 2, 3}
   my_set.remove(2)
   

3. *Union, Intersection, and Difference:*
   python
   set1 = {1, 2, 3}
   set2 = {3, 4, 5}
   union_set = set1 | set2
   intersection_set = set1 & set2
   difference_set = set1 - set2
   

## Dictionaries

### Overview
- A dictionary is a collection of key-value pairs.
- Keys are unique and used for fast data retrieval.

### Common Dictionary Operations
1. *Creating a Dictionary:*
   python
   my_dict = {'key1': 'value1', 'key2': 'value2'}
   

2. *Accessing Values:*
   python
   value = my_dict['key1']
   

3. *Adding or Modifying Entries:*
   python
   my_dict['new_key'] = 'new_value'
   

4. *Removing Entries:*
   python
   del my_dict['key1']
   

## Lambda Functions

### Overview
- Lambda functions, or anonymous functions, are defined using the lambda keyword.
- They are often used for short, one-time operations.

### Example
   python
   add = lambda x, y: x + y
   result = add(3, 4)
   

## Filter

### Overview
- The filter() function is used to filter elements from a sequence based on a given function.
- It returns an iterator.

### Example
   python
   numbers = [1, 2, 3, 4, 5, 6]
   even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
   

## Reduce

### Overview
- The reduce() function, from the functools module, applies a rolling computation to sequential pairs of values.
- It is useful for aggregating elements in a sequence.

### Example
   python
   from functools import reduce
   numbers = [1, 2, 3, 4, 5]
   sum_all = reduce(lambda x, y: x + y, numbers)
   

## Map

### Overview
- The map() function applies a given function to all items in a sequence and returns an iterator.

### Example
   python
   numbers = [1, 2, 3, 4, 5]
   squared_numbers = list(map(lambda x: x**2, numbers))
