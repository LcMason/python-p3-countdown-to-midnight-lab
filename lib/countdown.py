# your code goes here!
import time
def countdown(number):
    pass
    # uses a while loop to countdown from that integer to 1, outputting f'{number} SECOND(S)!' in each iteration of the loop. The function should print() "HAPPY NEW YEAR!" after the loop finishes:
    while number >= 1:
        print(f'{number} SECOND(S)!')
        number -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(number):
    pass
    while number >= 1:
        print (f'{number} SECOND(S)')
        time.sleep(1)
        number -=1
    print("HAPPY NEW YEAR!")

    