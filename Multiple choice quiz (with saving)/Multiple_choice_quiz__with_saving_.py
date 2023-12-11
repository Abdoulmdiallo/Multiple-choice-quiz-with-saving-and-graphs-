import matplotlib.pyplot as plt
score = 0
user_name = input("Your name: ")#asks the players name

def open_file(file, mode):
    with open(file, mode, encoding="utf8") as my_file:
        return my_file.read().splitlines()#this function will open a file in whatever mode you choose

questions_file = "quiz_questions2.txt" # you can choose 4 diffrent quizes just put 2,3 or 4 at the end to use the others
answers_file = "quiz_answers2.txt"# match the number 

questions = open_file(questions_file, "r")#opens the files with the answers and questions
answers = open_file(answers_file, "r")

if len(questions) != len(answers):#makes sure there are the same amount of questions as answers
    print("The number of questions and answers do not match.")
else:
    for question in range(len(questions)):
        print(questions[question])# prints each line of the question
        user_input = input("Your answer: ").lower()
        if user_input == answers[question]:# checks if the users answers to the line in the question is the same as what is on the answers file
            print("Correct!")   
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answers[question]}")
print(f"Your score is: {score}/{len(questions)}")# prints the amount of questions got right out of how many questionms there are

#this creates a file that stores all the players scores
Filename = "players"
MyFile = open(Filename+".txt","a") 
MyFile.write(f"\n{user_name} {score}") 
MyFile.close()
#the file might have some scores from my testing so delete them if you want a new bar chart
# Reading player names and scores from the file
playerNames = []
playerScores = []
#this will open the players file where the names and scores are and iterate through
with open("players.txt", "r") as score_file:
    for line in score_file:
        data = line.split()#this splits the name and the number so you can use their index to select them
#this will put the first part of the list in the list playernames and the second part in playerscores
        playerNames.append(data[0]) #selects the name
        playerScores.append(int(data[1])) #selects the number/score

# this will be Plotting the players names and scores using the list on line 40-41
plt.bar(playerNames, playerScores)
plt.xlabel('Players')#name of the x and y and title
plt.ylabel('Scores')
plt.title('Player Scores')
plt.show()