questions =[
    ["1.Who Developed C++ programming language." , "Graham Bell" , "Denis Ritchi" , "Alexander-II" , "Guido van Rossum" , "None" , 2],
    ["2.Who Developed python programming language." , "Guido van Rossum" , "Denis Ritchi" , "Alexander-II" , "Matz" , "None" , 1],
    ["3.Who Developed Java programming language." , "Graham Bell" , "Niklaus Wirth" , "James Gosling" , "Thomas Edison" , "None" , 3],
    ["4.Who Developed JavaScript programming language." , "Graham Bell" , "Denis Ritchi" , "Guido van Rossum" , "Brendan Eich" , "None" , 4],
    ["5.Who Developed Ruby programming language." , "Graham Bell" , "Denis Ritchi" , "Matz" , "Thomas Edison" , "None" , 3],
    ["6.Who Developed Pascal programming language." , "Matz" , "Niklaus Wirth" , "Alexander-II" , "Guido van Rossum" , "None", 2],
    ["7.Who Developed Pascal programming language." , "Matz" , "Niklaus Wirth" , "Alexander-II" , "Guido van Rossum" , "None", 2],
    ["8.Who Developed Pascal programming language." , "Matz" , "Niklaus Wirth" , "Alexander-II" , "Guido van Rossum" , "None", 2],
    ["9.Who Developed Pascal programming language." , "Matz" , "Niklaus Wirth" , "Alexander-II" , "Guido van Rossum" , "None", 2],
    ["10.Who Developed Pascal programming language." , "Matz" , "Niklaus Wirth" , "Alexander-II" , "Guido van Rossum" , "None", 2],
    ["11.Who Developed Pascal programming language." , "Matz" , "Niklaus Wirth" , "Alexander-II" , "Guido van Rossum" , "None", 2],
]
levels = [100000 , 200000 , 400000 , 500000 , 7000000 , 8500000 , 10000000 , 20000000 , 30000000 , 40000000 , 50000000]

money = 0
answer = 0

for answer in range(0 , len(questions)):
    question = questions[answer]
    print(f"Question for Rupees {levels[answer]} is here: ")
    print(question[0])
    print(f"a. {question[1]}            b. {question[2]}")
    print(f"c. {question[3]}            d. {question[4]}")
    reply = int(input("Enter your Answer(1-4) "))
    if reply == question[6]:
        print(f"You are correct , you won Rupees {levels[answer]}")
        money = levels[answer]
        if answer == 3:  # Question 4
            locked_money = 7000000  # Lock at 7,000,000
            print(f"Your money is now locked at Rupees {locked_money}")
        elif answer == 9:  # Question 10
            locked_money = 50000000  # Lock at 50,000,000
            print(f"Your money is now locked at Rupees {locked_money}")
        
    else:
        print(f"Sorry you are wrong , the correct answer is {question[6]} , you lost Rupees {levels[answer]}")
        if answer >= 3:
            money = locked_money
        else:
            money = 0
        break

        break
print(f"Your take home money is{money}")


 


