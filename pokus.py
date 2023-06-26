


# ------------------------------------------------------------------
#
# P Y T H O N
# 
# ------------------------------------------------------------------
# Receiving Input
#   name = input ("What is your name: ")
#   
# ------------------------------------------------------------------
# Variables:
#   int ()
#   float ()
#   bool ()
#   str ()
#
# ------------------------------------------------------------------
# Conversion of variables>
#   int (birth_year)
#   str (sum)
#   temperature = float (input ("Insert temperature: "))
#
# ------------------------------------------------------------------
# Strings:
#   course = "Python for Begginners"
#   print (course.upper() 
#   print (course.find 
#   print (course.replace
#   print ("Python" in course)
#
# ------------------------------------------------------------------
# Arithmetic operators:
#   +
#   -
#   *       
#   **      exponent
#   /       float
#   //      int
#   %       remainder (zbytek)
#   +=      augmented assignment operator (x += 3)
#   -=
#   *=
#   /=
#
# ------------------------------------------------------------------
# Comparison operators:
#   is '>' '<' '=>' '<=' '=='
#   is not '!='
#   x = 3 <= 2
#   print (x)
#
# ------------------------------------------------------------------
# Logical operators:
#   and (both); or (at least one); not (invert)
#   x = 25
#   print (not x > 10 and x < 30)
#   print (x > 10 or x < 30)
#
# ------------------------------------------------------------------
# IF statements
#   if; elif (else if); else; : (then)
#   
#   Example 1:
# temperature = float (input ("Insert temperature: "))
# print ("")
# if temperature > 30: # teplota nad 30
#     print ("It's a hot day")
#     print ("Drink water")
# elif temperature > 20: # teplota 21 - 30 
#     print ("It's a nice day")
# elif temperature > 10: # teplota 11 - 20
#     print ("It's a bit cold")
# else:
#     print ("It's very cold")
# print ("")
# print ("Done")
#
#   Example 2:
# weight = float (input ("Your weight: "))
# unit = str (input ("(K)g or L(s): "))
# if unit.upper() == "K": # udaj je v kg
#     weight_lbs = weight / 0.45
#     print ("Weight in Kg is:", weight)
#     print ("Weight in Lbs is:", weight_lbs)
# elif unit.upper() == "L": # udaj je v lbs
#     weight_kg = weight * 0.45
#     print ("Weight in Kg is:", weight_kg)
#     print ("Weight in Lbs is:", weight)
# else:
#     print ("Weight cannot be determined, unit incorrectly entered (Kg/Lbs)")
# print ("")
# print ("Done")
#
# ------------------------------------------------------------------
# While loops
#
#   Example 1:
# i = 1
# while i <= 10:
#     print (i)
#     print (i * '*')
#     i = i + 1
#   
# ------------------------------------------------------------------
# Lists
# 
#   Example 1:
# names = ["Jan","Petr","Josef","Karel","Emil"]
# names[0] = "Honza"
# print (names)
# print (names [-1])
# print (names [1:4])
# 
#   Example 2:
# numbers = [1,2,3,4,5,6,7]
# numbers.append (8)
# numbers.insert (0,0)
# numbers.remove (3)
# numbers.clear ()
# print (numbers)#
# print (1 in numbers)   {vraci True nebo False}
# print (len (numbers))  {vraci pocet polozek v seznamu}
#
# ------------------------------------------------------------------
# FOR Loops
#   
#   Example 1:
# numbers = [1,2,3,4,5,6,7]
#
# for item in numbers:
#     print (item)
# 
# i = 0
# while i < len (numbers):
#     print (numbers[i])
#     i = i + 1
#
# ------------------------------------------------------------------
# RANGE Function
# range (from,to,step)
#
#   Example 1:
# for number in range(5,20,2):
#     print (number)        {5,7,9,...19}
# 
#
# ------------------------------------------------------------------
# TUPLES {like lists but inchangable}
# 
#   Example 1:
# names = ("Jan","Petr","Josef","Karel","Emil")
# print (names)
#

