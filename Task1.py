# Take trainee data using input commands
first_name = input("Please enter your first name: ")
middle_name = input("Please enter your middle name: ")
last_name = input("Please enter your last name: ")
# Now we have the seperate inputs, we can concatenate.
# We then use the capitalize method to ensure each name begins with a capital letter.
# Use casting to ensure the data type is a string. This is optional as the inputs will always be strings unless we exlicitly convert to another format.
full_name = str(first_name.capitalize() + " " + middle_name.capitalize() + " " + last_name.capitalize())
# We repeat this process for the address
house_number = int(input("Please enter your house number: ")) # house number will always be an integer.
street = input("Please enter your street name: ")
postcode = input("Please enter your postcode: ")
address = str(house_number) + " " + street.capitalize() + ", " + postcode.upper()

# The following parameters require simple inputs
# Both NI and DOB have non-numeric characters therefore remain as string types.
ni_number = input("Please enter your national insurance number with no spaces: ")
dob = input("Please enter your date of birth in the following format dd-mm-yyyy: ")
age = int(input("Please enter your age: ")) # Age is restricted to integer inputs.
course_applied = input("Please type the course you wish to apply for: ")
background = input("Please enter your most recent education: ")


# We now have all the user data so we can print to the console.
print("Thank you for entering your details. Please confirm:")
print("Full Name:" + " " + full_name)
print("Address:" + " "+ address)
print("NI Number:" + " "+ ni_number.upper())
print("DOB and age" + " " + dob + ", " + str(age) + " " +"years old")
print("Course Applied for:" + " " + course_applied.capitalize())
print("Education Background:" + " " + background.capitalize())
