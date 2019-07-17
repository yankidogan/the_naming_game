import random
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

class Agent:
    def __init__(self, Lexicon, Name):
        self.Lexicon = Lexicon
        self.Name = Name

def gen_name ():
    vowels = ['A', 'E', 'I', 'O', 'U']
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    word = ""
    length = random.randint(2, 10)
    isVowel = False
    for i in range(length):
        if(isVowel):
            word = word+vowels[random.randint(0, 4)]
            isVowel = False
        else:
            word = word+consonants[random.randint(0, 20)]
            isVowel = True
    return word

def lex_counter(agent):
    lexicon = agent.Lexicon
    total = 0
    for x in lexicon:
        total = total + len(lexicon[x])
    return total

def print_good(dictionary):
    print()
    for x in sorted(dictionary):
        print(x,' : ', sorted(dictionary[x]))
        print()

lex1 = defaultdict(list)
lex2 = defaultdict(list)
lex3 = defaultdict(list)
lex4 = defaultdict(list)
lex5 = defaultdict(list)
lex6 = defaultdict(list)
lex7 = defaultdict(list)
lex8 = defaultdict(list)
lex9 = defaultdict(list)
lex10 = defaultdict(list)
agent1 = Agent(lex1, "agent1")
agent2 = Agent(lex2, "agent2")
agent3 = Agent(lex3, "agent3")
agent4 = Agent(lex4, "agent4")
agent5 = Agent(lex5, "agent5")
agent6 = Agent(lex6, "agent6")
agent7 = Agent(lex7, "agent7")
agent8 = Agent(lex8, "agent8")
agent9 = Agent(lex9, "agent9")
agent10 = Agent(lex10, "agent10")
objects = ["object1", "object2", "object3", "object4", "object5"]
agents = [agent1, agent2, agent3, agent4, agent5, agent6, agent7, agent8, agent9, agent10]

countSuc = 0
countFail = 0
sucList = [0]
sucCount = []
counter = 0
lexTotal = []

#NGLoopStart
for i in range(5000):
    speakerIndex = random.randint(0, 9)
    hearerIndex = random.randint(0, 9)
    objectIndex = random.randint(0, 4)
    while hearerIndex == speakerIndex:
        hearerIndex = random.randint(0, 9)
    speaker = agents[speakerIndex]
    hearer = agents[hearerIndex]
    obj = objects[objectIndex]
    name = ""
    #Check if the speaker has a name for the object
    #Speaker has a name:
    if obj in speaker.Lexicon:
        name = speaker.Lexicon[obj][random.randint(0, len(speaker.Lexicon[obj])-1)]
        #Check if the hearer has a name for the object
        #Hearer has a name:
        if obj in hearer.Lexicon:
            #Check if the hearer uses the name differently
            #Hearer uses the same name:
            if name in hearer.Lexicon[obj]:
                countSuc = countSuc+1
                sucCount.append(1)
            #Hearer uses a different name:
            else:
                hearer.Lexicon[obj].append(name)
                countFail = countFail+1
                sucCount.append(0)
        #Hearer has no name:
        else:
            hearer.Lexicon[obj].append(name)
            countFail = countFail+1
            sucCount.append(0)
    #Speaker has no name:
    else:
        name = gen_name()
        speaker.Lexicon[obj].append(name)
        countFail = countFail+1
        sucCount.append(0)
    counter = counter + 1
    if counter == 50:
        sucList.append(countSuc/(countSuc+countFail))
        counter = 0
        countSuc = 0
        countFail = 0
    lexTotal.append(lex_counter(agent1))
#NGLoopEnd

print("Agent1's Lexicon:")
print_good(agent1.Lexicon)
print("Agent2's Lexicon:")
print_good(agent2.Lexicon)
print("Agent3's Lexicon:")
print_good(agent3.Lexicon)
print("Agent4's Lexicon:")
print_good(agent4.Lexicon)
print("Agent5's Lexicon:")
print_good(agent5.Lexicon)
print("Agent6's Lexicon:")
print_good(agent6.Lexicon)
print("Agent7's Lexicon:")
print_good(agent7.Lexicon)
print("Agent8's Lexicon:")
print_good(agent8.Lexicon)
print("Agent9's Lexicon:")
print_good(agent9.Lexicon)
print("Agent10's Lexicon:")
print_good(agent10.Lexicon)

plt.plot(np.linspace(0, 5050, 101, endpoint=False).tolist(), sucList)
plt.grid(True)
plt.margins(x=0, y=0)
plt.ylabel('communicative success rate')
plt.xlabel('number of iterations')
plt.show()

plt.plot(lexTotal)
plt.grid(True)
plt.margins(x=0, y=0)
plt.ylabel('lexicon size')
plt.xlabel('number of iterations')
plt.show()

print("Final Communicative Success Rate: ")
print(max(sucList)*100,"%")

print("Complete Communicative Success: ")
print("Iteration ",len(sucCount)- sucCount[::-1].index(0))

print("Lexicon Size: ")
print(lexTotal[-1])
