questions = [
    ["which language is used to create fb?", "python",
     "java", "c", "none", 4],
    ["which is the national animal of india?", "peacock",
     "cat", "dog", "tiger", 4],
    ["which app is used to listen songs?", "github",
     "snapchat", "linkedin", "spotify", 4],
    ["which is the favourite food of hyderabadis?", "pizza",
     "sandwich", "burger", "biryani", 4],
    ["which app helps to get an internship?", "instagram",
     "youtube", "snapchat", "linkedin", 4],
    ["which is the national bird of india?", "duck",
     "eagle", "bat", "peacock", 4],
    ["which colour indicates to stop in the signal lights?", "green",
     "blue", "yellow", "red", 4],
    ["which colour indicates to go in the signal lights?", "green",
     "blue", "yellow", "red", 1],
    ["which app is famous for social media?", "snapchat",
     "linkedin", "instagram", "youtube", 3],
    ["which language is used by the computers?", "python",
     "java", "c", "none", 4]
]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 320000, 1000000, 10000000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}       b. {question[2]}")
    print(f"c. {question[3]}       d. {question[4]}")
    reply = int(input("enter your answer (1-4) "))
    if reply == question[-1]:
        print(f"correct answer, you have won {levels[i]}")
        if i == 4:
            money = 1000
        elif i == 8:
            money = 320000
        elif i == 9:
            money = 10000000
    else:
        print("wrong answer")
        break

print(f"Your take home money is {money}")