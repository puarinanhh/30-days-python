first_name = input('Enter your first name: ')
age = input('Enter your age: ')
print('first name: ' + first_name + ' age : ' + age)
print(age)
print(type(age))
person_info = {
      'first_name': 'John',
      'last_name': 'Doe',
      'age': 30
}

print(person_info)

print('type(10) :', type(10))
print('type(10.1) :', type(10.1))
print('type("Hello") :', type("Hello"))
print('type(10+1j) :', type(10+1j))
print('type(person_info) :', type(person_info))
print('type(1,2,3) :', type((1,2,3)))
print('type(zip([1,2], [3,4])) :', type(zip([1,2], [3,4])))

# int to float
num_int = 10
print('num_int :', num_int)
num_float = float(num_int)
print('float of num int :', num_float)
# float to int
gravity = 10.6
print('gravity :', gravity, ', ' 'int of float: ',int(gravity))

# string to int
num_str = '10'
print('num_str :', num_str)
num_int = int(num_str)
print('int of num_str :', num_int)

# int to string
num_int = 10
print('num_int :', num_int)
num_str = str(num_int)
print('str of num_int :', num_str)

# str to float
num_str = '10.6'
print('num_str :', num_str)
num_float = float(num_str)
print('float of num_str :', num_float)

# str to list
num_str = '10,20,30'
print('num_str :', num_str)
num_list = list(num_str)
print('list of num_str :', num_list)


# exercise lv1
# Declare a first name variable and assign a value to it
first_name_1 = 'Puarin'

# Declare a last name variable and assign a value to it
last_name_1 = 'Dara'

# Declare a full name variable and assign a value to it
full_name_1 = first_name_1 + ' ' + last_name_1
print(full_name_1)

# Declare a country variable and assign a value to it
country = 'VietNam'
print('Country :', country)

# Declare a city variable and assign a value to it
city = 'Hanoi'
print('City :', city)

# Declare an age variable and assign a value to it
age = 20
print('Age :', age)

# Declare a year variable and assign a value to it
year = 2022
print('Year :', year)

# Declare a is_married variable and assign a value to it
is_married = False
print('Is Married :', is_married)

# Declare a is_true variable and assign a value to it
is_true = True
print('Is True :', is_true)

# Declare a is_light_on variable and assign a value to it
is_light_on = True
print('Is Light On :', is_light_on)

# Declare multiple variables on one line
x, y, z = 1, 2, 3
print(x, y, z)

# Exercise lv2

# Check the data type of all your variables using type() built-in function
print(type(first_name_1))
print(type(last_name_1))
print(type(full_name_1))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Using the len() built-in function, find the length of your first name
print(len(first_name_1))

# Compare the length of your first name and your last name
print(len(first_name_1) == len(last_name_1))

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one
print(diff)

# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
print(product)

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(remainder)

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area


radius = 30
area_of_circle = 3.14 * radius * radius
circum_of_circle = 2 * 3.14 * radius
print(area_of_circle)
print(circum_of_circle)

radius2 = input('Enter radius: ')
area_of_circle2 = 3.14 * int(radius2) * int(radius2)
print(area_of_circle2)


# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
test_name = input('Enter your name: ')
print('Your name is: ', test_name)
test_age = input('Enter your age: ')
print('Your age is: ', test_age)


