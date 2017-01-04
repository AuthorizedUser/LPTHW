print "I will now count my chickens:"

print "Hens", 25 + 30 / 6 #Hens 30
print "Roosters", 100 - 25 * 3 % 4 #Roosters 97 #multiplication occurred before remainder divide.

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4 + 6 #7 # division first, then remainder, which is zero; then additive. The -.75 does not make a difference since it is a floating point. EDIT: Added one floating point number to test if it will carry over to the rest of the line.

print "Is it true that 3 + 2 < 5 - 7?" #Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7 #False, the less than symbol is evaluated last

print "What is 3 + 2?", 3 + 2 #What is 3 + 2? 5
print "What is 5 - 7?", 5 - 7 #What is 5 - 7? -2

print "Oh, that's why it's False." #Oh, that's why it's False."

print "How about some more." #How about some more."

print "Is it greater?", 5 > -2 #Is it greater? True
print "Is it greater or equal?", 5 >= -2 #Is it greater or equal? True
print "Is it less or equal?", 5 <= -2 #Is it less or equal? False