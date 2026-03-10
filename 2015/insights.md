## Day 1 
![Python](https://img.shields.io/badge/Python-3.12.3-ffd23f)

Use variables in strings by using f-strings à la: `f'Some text with some {variable}'`.

---
Ternary-ish operators can be done with the structure below, but that doesn't add much that a normal
if-else block doesn't do, IMO. For more complex logic, this structure seems less appropriate.
```python
some_value if some_condition else other_value
```

## Day 2
![Python](https://img.shields.io/badge/Python-3.12.3-ffd23f)

You can `map()` an array of elements to another type with `map(type, list)`. To convert that back to
an array again, you can call `list()` on that `map()` call.

---
Python lets you unpack an array (kinda like in JavaScript I guess) with 
`[element1, element2, element3] = [array name]` as long as the amount of elements matches(?)

---
Kinda obvious but you can return dictionaries from functions and access values with 
`dictionary["value"]`.

## Day 3
![Python](https://img.shields.io/badge/Python-3.12.3-ffd23f)

In Python, you can just instantiate an array/list of **anything** by doing `list = []` without 
needing to put anything inside of the brackets to determine what will be stored in there.
Not knowing this was kinda screwing up my solution for Day 3 - part 1.

---
In Python, you can use a set `{}` to avoid having to check for element uniqueness in a list (with `if x not in list`). That's especially useful when keeping track of a number of coordinates (i.e. tuples) like in the solution for Day 3 - part 1. I was using a list of dictionaries first, because I didn't know I could just store the coordinates in a tuple.

---
Python exposes an operator for unions of sets with `|` (single pipe). I was calling `.union` before on the sets of Santa and Robo-Santa's coordinates, but `|` looks a bit cleaner. 

Furthermore, it was a good idea to print the cardinality of the union of the two sets rather than conditionally adding coordinates to each set based on exclusivity. The union approach also makes both sets' contents more true to their purpose.

---
Python supports multi-line expressions by either putting `\` at the end of a line, or wrapping the entire expression in parentheses.

## Day 4
![Python](https://img.shields.io/badge/Python-3.12.3-ffd23f)

I can `import` libraries at the top of a Python script, but I knew that.

---
For portability (and convenience when running code in VSCode), I should use this:

```py
from pathlib import Path

f = Path(__file__).with_name("input.txt")
data = f.read_text()[other operations]
```
Rather than just doing:

```py
with open("input.txt") as f:
``` 
Otherwise, VScode looks for the input file relative to where the `python3` command lives.

## Day 5
![Go](https://img.shields.io/badge/Go-1.25.0-007d9c)

Strings in Go are actually arrays of bytes. This means that you can't always just iterate over a string and expect to be able to compare characters. 

---
Go has some quirks with loops. You can make several different types of loops with `for`, such as:

```go
for _, var := range vars {
    // Some code using var | 'for each' style
}
```
> Normally, the first parameter would be the index, but naming that `_` actually ignores the index.

And: 
```go
for i := range vars {
    // Some code using i | classic 'for loop' style
}
```
> In this case, only the index is accessible in the loop body.

---
When you want to get a 'subslice' of a slice in Go, the 'end' (if specified) is exclusive. That means that, e.g., `slice[3 : len(slice)-1]` actually excludes the last `[whatever]` contained in the slice. I was unaware of this and it kept me from completing part 2 of Day 5.

## Day 6
