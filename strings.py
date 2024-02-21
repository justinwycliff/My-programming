name =input( "enter your namre")
message = f" hello , {name}"
print(message)
 
 #string concenation (normal way)
first_name = "justin"
second_name = "wycliff"

full_name = first_name + second_name
print(full_name)

# second normal way
full_name = first_name + " " + second_name
print(full_name)


#concatenation using f strings
part1 = "stay hungry"
part2 = "you die"

print(f" {part1} {part2} ")

print( "you will die if you " + part1)

print(f" you will die if you ") , {part1} "
