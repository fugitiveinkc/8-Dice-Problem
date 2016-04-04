'''

Title: Adventures in Probability

Objective: To address the question of expected value with 8 dice and rerolls on blanks (from game played at olive game night)

'''
import matplotlib.pyplot as plt
from Dice import dice

#1) Set up dice: elements
#2) Set up number of dice: dice objects
#3) Set up number of rolls and collect data
#4) Perform probability analysis

elements = [int(x) for x in raw_input('What are the faces of the dice? ').split(' ')]
number_of_dice = int(raw_input('How many dice do you want? '))
number_of_rolls = int(raw_input('How many rolls would you like to perform? '))

#Set up dice

Dice = [dice(elements) for x in range(0, number_of_dice)]
	
#How should I store data?  Dictionary is fast. 

data = {x: 0 for x in range(number_of_dice*min(elements), number_of_dice*max(elements)+1)}
data1 = {x: 0 for x in range(number_of_dice*min(elements), number_of_dice*max(elements)+1)}

#Rolling time! (2 experiments: One with no reroll, the other with blank rerolls) 

#Experiment 1
for n in range(0, number_of_rolls):
	die_sum = 0
	for die in Dice:
		die.roll()
		die_sum += die.face
	data[die_sum] += 1

#Experiment 2
for n in range(0, number_of_rolls):
	die_sum = 0
	for die in Dice:
		die.roll()
		if die.face == 0:
			die.roll()
		die_sum += die.face
	data1[die_sum] += 1

plt.plot(data.keys(), [data[x] for x in data.keys()], 'g^', data1.keys(), [data1[x] for x in data1.keys()], 'ro')
plt.xlabel('Possible dice sums')
plt.ylabel('Frequency')
plt.title('Frequency distribution of 8 dice')
plt.show()
print "This is the data with no reroll: " + str(data)
print "This is the data with a reroll for blanks: " + str(data1)

#Probabilistic analysis
#1) Plot Histogram (What libraries to use?)
#2) Expected Value
#3) Variance and Standard Deviation

p = {x: float(data[x])/number_of_rolls for x in data} #Probabilities for data
p1 = {x: float(data1[x])/number_of_rolls for x in data1} #Probabilities for data1
ex = sum(x*p[x] for x in data) #Expected for data
ex1 = sum(x*p1[x] for x in data1) #Expected for data1
print "The probabilities with no reroll: " + str(p)
print "The expected value with no reroll: " + str(ex)
print "The probabilities with a reroll on blanks: " + str(p1)
print "The expected value with a reroll on blanks: " + str(ex1)
