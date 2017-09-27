import random

# choice(seq)------- A random item from a list, tuple, or string.
print "choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9])
print "choice('A String') : ", random.choice('A String')

# randrange([start],stop,[step]) ---------- A randomly selected element from range(start, stop, step)
# Select an even number in 100 <= number < 1000
print "randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2)

# Select another number in 100 <= number < 1000
print "randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3)

# random() ------- A random float r, such that 0 is less than or equal to r and r is less than 1
# First random number
print "random() : ", random.random()

# Second random number
print "random() : ", random.random()

# seed([x]) ------ Sets the integer starting value used in generating random numbers.
# Call this function before calling any other random module function.
# Returns None.
random.seed( 10 )
print "Random number with seed 10 : ", random.random()

# It will generate same random number
random.seed( 10 )
print "Random number with seed 10 : ", random.random()

# It will generate same random number
random.seed( 10 )
print "Random number with seed 10 : ", random.random()

# shuffle(lst) ------- Randomizes the items of a list in place. Returns None.
list = [20, 16, 10, 5];
random.shuffle(list)
print "Reshuffled list : ",  list

random.shuffle(list)
print "Reshuffled list : ",  list

# uniform(x,y) --------- A random float r, such that x is less than or equal to r and r is less than y 
print "Random Float uniform(5, 10) : ",  random.uniform(5, 10)

print "Random Float uniform(7, 14) : ",  random.uniform(7, 14)