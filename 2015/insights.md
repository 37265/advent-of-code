## Day 1
Use variables in strings by using f-strings à la: `f'Some text with some {variable}'`.

---
Ternary-ish operators can be done with the structure below, but that doesn't add much that a normal
if-else block doesn't do, IMO. For more complex logic, this structure seems less appropriate.
```python
some_value if some_condition else other_value
```

---
You can `map()` an array of elements to another type with `map(type, list)`. To convert that back to
an array again, you can call `list()` on that `map()` call.

---
Python lets you unpack an array (kinda like in JavaScript I guess) with 
`[element1, element2, element3] = [array name]` as long as the amount of elements matches(?)

---
Kinda obvious but you can return dictionaries from functions and access values with 
`dictionary["value"]`.