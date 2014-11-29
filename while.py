number = 23
running = True

while running:
    guess = int(raw_input('Enter an integer : '))
    if guess == number:
        print 'Congratulations, you guessed it.'
        # This causes the while loop to stop
        running = False
    elif guess < number:
        # Another block
        print 'No, it is a little higher than that.'
        # You can do whatever you want in a block ...
    else:
        print 'No, it is a little lower than that.'
        # you must have guessed > number to reach here
else:
    print 'The while loop is over.'

print 'Done'
# This last statement is always executed,
# after the if statement is executed.
