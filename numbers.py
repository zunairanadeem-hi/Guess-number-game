print("------------guess secret number game-----------")
secret_number=10
while True:
    userchoices=int(input("enter the guess number:"))
    if(userchoices<secret_number):
        print("too low!try the higher number")
    elif(userchoices>secret_number):
        print("too high! try the smaller number")
    elif(userchoices==secret_number):
        print("congraulation! you guess the correct number")
        break
print("----------game over--------------")