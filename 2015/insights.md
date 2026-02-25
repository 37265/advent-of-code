## Day 1
Use variables in strings by using f-strings à la: `f'Some text with some {variable}'`.

---
Ternary-ish operators can be done with the structure below, but that doesn't add much that a normal
if-else block doesn't do, IMO. For more complex logic, this structure seems less appropriate.
```python
some_value if some_condition else other_value
```

## Day 2
You can `map()` an array of elements to another type with `map(type, list)`. To convert that back to
an array again, you can call `list()` on that `map()` call.

---
Python lets you unpack an array (kinda like in JavaScript I guess) with 
`[element1, element2, element3] = [array name]` as long as the amount of elements matches(?)

---
Kinda obvious but you can return dictionaries from functions and access values with 
`dictionary["value"]`.

## Day 3
In Python, you can just instantiate an array/list of **anything** by doing `list = []` without 
needing to put anything inside of the brackets to determine what will be stored in there.
Not knowing this was kinda screwing up my solution for Day 3 - part 1.

---
In Python, you can use a set `{}` to avoid having to check for element uniqueness in a list (with `if x not in list`). That's especially useful when keeping track of a number of coordinates (i.e. tuples) like in the solution for Day 3 - part 1. I was using a list of dictionaries first, because I didn't know I could just store the coordinates in a tuple.

---
Python exposes an operator for unions of sets with `|` (single pipe). I was calling `.union` before on the sets of Santa and Robo-Santa's coordinates, but `|` looks a bit cleaner. 

Furthermore, it was a good idea to print the cardinality of the union of the two sets rather than conditionally adding coordinates to each set based on exclusivity. The union approach also makes both sets' contents more true to their purpose.

## Day 4