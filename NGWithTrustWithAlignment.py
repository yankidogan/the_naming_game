import random
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

class Agent:
    def __init__(self, Lexicon, tLev, nTrust, nScore, nStorage, Name):
        self.Lexicon = Lexicon
        self.tLev = tLev
        self.nTrust = nTrust
        self.nScore = nScore
        self.nStorage = nStorage
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

def store_counter(agent):
    store = agent.nStorage
    total = 0
    for x in store:
        total = total + len(store[x])
    return total

def lex_counter(agent):
    lexicon = agent.Lexicon
    total = 0
    for x in lexicon:
        total = total + len(lexicon[x])
    return total

def number_of_words(agent, obj):
    lis = agent.Lexicon
    total = 0
    for x in lis:
        if (x==obj):
            total = len(lis[x])
    return total
            
def gen_trust():
    tLev = {"agent1": random.randint(1, 10),
            "agent2": random.randint(1, 10),
            "agent3": random.randint(1, 10),
            "agent4": random.randint(1, 10),
            "agent5": random.randint(1, 10),
            "agent6": random.randint(1, 10),
            "agent7": random.randint(1, 10),
            "agent8": random.randint(1, 10),
            "agent9": random.randint(1, 10),
            "agent10": random.randint(1, 10)}
    return tLev

def highest_score(agent, obj):
    objList = agent.nScore[obj]
    length = len(objList)
    highest = 0
    indexes = []
    bestNames = []
    for i in range(length):
        if(objList[i]>highest):
            highest = objList[i]
    for i in range(length):
        if (objList[i]==highest):
            indexes.append(i)
    bestNames = [agent.nStorage[obj][i] for i in indexes]
    return bestNames

def print_good(dictionary):
    print()
    for x, y in sorted(dictionary.items()):
        print(x,': ', y)
        print()

def print_good_s(dictionary):
    print()
    counter = 0
    for x, y in sorted(dictionary.items()):
        print(x,': ', y, end= "   ")
        counter = counter + 1
        if counter == 2:
            print()
            print()
            counter = 0
    if counter == 1:
        print()
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
#Name storages of each agent:
nStorage1 = defaultdict(list)
nStorage2 = defaultdict(list)
nStorage3 = defaultdict(list)
nStorage4 = defaultdict(list)
nStorage5 = defaultdict(list)
nStorage6 = defaultdict(list)
nStorage7 = defaultdict(list)
nStorage8 = defaultdict(list)
nStorage9 = defaultdict(list)
nStorage10 = defaultdict(list)
#Trust levels for each name in agents' lexicons:
nTrust1 = defaultdict(int)
nTrust2 = defaultdict(int)
nTrust3 = defaultdict(int)
nTrust4 = defaultdict(int)
nTrust5 = defaultdict(int)
nTrust6 = defaultdict(int)
nTrust7 = defaultdict(int)
nTrust8 = defaultdict(int)
nTrust9 = defaultdict(int)
nTrust10 = defaultdict(int)
#Score values for each name in agents' name storage:
#Trusted agent = +2, others = +1
nScore1 = defaultdict(list)
nScore2 = defaultdict(list)
nScore3 = defaultdict(list)
nScore4 = defaultdict(list)
nScore5 = defaultdict(list)
nScore6 = defaultdict(list)
nScore7 = defaultdict(list)
nScore8 = defaultdict(list)
nScore9 = defaultdict(list)
nScore10 = defaultdict(list)
#Each agent's trust level for each other
tLev1 = gen_trust()
tLev2 = gen_trust()
tLev3 = gen_trust()
tLev4 = gen_trust()
tLev5 = gen_trust()
tLev6 = gen_trust()
tLev7 = gen_trust()
tLev8 = gen_trust()
tLev9 = gen_trust()
tLev10 = gen_trust()
agent1 = Agent(lex1, tLev1, nTrust1, nScore1, nStorage1, "agent1")
agent2 = Agent(lex2, tLev2, nTrust2, nScore2, nStorage2, "agent2")
agent3 = Agent(lex3, tLev3, nTrust3, nScore3, nStorage3, "agent3")
agent4 = Agent(lex4, tLev4, nTrust4, nScore4, nStorage4, "agent4")
agent5 = Agent(lex5, tLev5, nTrust5, nScore5, nStorage5, "agent5")
agent6 = Agent(lex6, tLev6, nTrust6, nScore6, nStorage6, "agent6")
agent7 = Agent(lex7, tLev7, nTrust7, nScore7, nStorage7, "agent7")
agent8 = Agent(lex8, tLev8, nTrust8, nScore8, nStorage8, "agent8")
agent9 = Agent(lex9, tLev9, nTrust9, nScore9, nStorage9, "agent9")
agent10 = Agent(lex10, tLev10, nTrust10, nScore10, nStorage10, "agent10")
objects = ["object1", "object2", "object3", "object4", "object5"]
agents = [agent1, agent2, agent3, agent4, agent5, agent6, agent7, agent8, agent9, agent10]

countSuc = 0
countFail = 0
sucList = []
sucCount = []
counter = 0
lexTotal = []
t_obj1 = []
t_obj2 = []
t_obj3 = []
t_obj4 = []
t_obj5 = []

l_obj1 = []
l_obj2 = []
l_obj3 = []
l_obj4 = []
l_obj5 = []

storageTotal = []

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
                if hearer.tLev[speaker.Name] > hearer.nTrust[obj]:
                    index = hearer.nStorage[obj].index(name)
                    hearer.nScore[obj][index] = hearer.nScore[obj][index] + 2
                    hearer.nTrust[obj] = hearer.tLev[speaker.Name]
                else:
                    index = hearer.nStorage[obj].index(name)
                    hearer.nScore[obj][index] = hearer.nScore[obj][index] + 1
                hearer.Lexicon[obj] = highest_score(hearer, obj)
            #Hearer uses a different name:
            else:
                #Check if the hearer ever heard of the name before
                #Hearer heard of the name before:
                if name in hearer.nStorage[obj]:
                    #Check the trust level
                    #If the trust level is higher or equal, add 2 points
                    if hearer.tLev[speaker.Name] > hearer.nTrust[obj]:
                        index = hearer.nStorage[obj].index(name)
                        hearer.nScore[obj][index] = hearer.nScore[obj][index] + 2
                        hearer.nTrust[obj] = hearer.tLev[speaker.Name]
                    #If the trust level is lower, add 1 point
                    else:
                        index = hearer.nStorage[obj].index(name)
                        hearer.nScore[obj][index] = hearer.nScore[obj][index] + 1
                    #Make sure that only the name with the highest score for the object is in the lexicon
                    hearer.Lexicon[obj] = highest_score(hearer, obj)
                #Hearer hasn't heard of the name before
                else:
                    hearer.nStorage[obj].append(name)
                    if hearer.tLev[speaker.Name] > hearer.nTrust[obj]:
                        hearer.nScore[obj].append(2)
                    else:
                        hearer.nScore[obj].append(0)
                hearer.Lexicon[obj] = highest_score(hearer, obj)
                countFail = countFail+1
                sucCount.append(0)
        #Hearer has no name:
        else:
            hearer.Lexicon[obj] = [name]
            hearer.nTrust[obj] = hearer.tLev[speaker.Name]
            hearer.nStorage[obj].append(name)
            hearer.nScore[obj].append(0)
            countFail = countFail+1
            sucCount.append(0)
    #Speaker has no name:
    else:
        name = gen_name()
        speaker.Lexicon[obj] = [name]
        speaker.nStorage[obj].append(name)
        speaker.nScore[obj].append(0)
        countFail = countFail+1
        sucCount.append(0)
    counter = counter + 1
    if counter == 50:
        sucList.append(countSuc/(countSuc+countFail))
        counter = 0
        countSuc = 0
        countFail = 0
    lexTotal.append(lex_counter(agent1))
    storageTotal.append(store_counter(agent1))
    t_obj1.append(agent1.nTrust['object1'])
    t_obj2.append(agent1.nTrust['object2'])
    t_obj3.append(agent1.nTrust['object3'])
    t_obj4.append(agent1.nTrust['object4'])
    t_obj5.append(agent1.nTrust['object5'])
    l_obj1.append(number_of_words(agent1, 'object1'))
    l_obj2.append(number_of_words(agent1, 'object2'))
    l_obj3.append(number_of_words(agent1, 'object3'))
    l_obj4.append(number_of_words(agent1, 'object4'))
    l_obj5.append(number_of_words(agent1, 'object5'))
#NGLoopEnd


print("Agent1's tLev:")
print_good_s(agent1.tLev)
print("Agent1's nTrust:")
print_good_s(agent1.nTrust)
print("Agent1's nStorage:")
print_good(agent1.nStorage)
print("Agent1's nScore:")
print_good(agent1.nScore)
print("Agent1's Lexicon:")
print_good(agent1.Lexicon)
print("Agent2's nStorage:")
print_good(agent2.nStorage)
print("Agent2's nScore:")
print_good_s(agent2.nScore)
print("Agent2's Dictionary:")
print_good(agent2.Lexicon)
print("Agent3's Dictionary:")
print_good(agent3.Lexicon)
print("Agent4's Dictionary:")
print_good(agent4.Lexicon)
print("Agent5's Dictionary:")
print_good(agent5.Lexicon)
print("Agent6's Dictionary:")
print_good(agent6.Lexicon)
print("Agent7's Dictionary:")
print_good(agent7.Lexicon)
print("Agent8's Dictionary:")
print_good(agent8.Lexicon)
print("Agent9's Dictionary:")
print_good(agent9.Lexicon)
print("Agent10's Dictionary:")
print_good(agent10.Lexicon)

plt.plot(np.linspace(0, 5050, 100, endpoint=False).tolist(), sucList)
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

plt.plot(t_obj1[0:1000], label='object1')
plt.plot(t_obj2[0:1000], label='object2')
plt.plot(t_obj3[0:1000], label='object3')
plt.plot(t_obj4[0:1000], label='object4')
plt.plot(t_obj5[0:1000], label='object5')
plt.grid(True)
plt.margins(x=0, y=0)
plt.ylabel('nTrust value')
plt.xlabel('number of iterations')
plt.yticks(np.arange(0, 11, step = 1))
plt.legend()
plt.show()

plt.plot(l_obj1[0:1000], label='object1')
plt.plot(l_obj2[0:1000], label='object2')
plt.plot(l_obj3[0:1000], label='object3')
plt.plot(l_obj4[0:1000], label='object4')
plt.plot(l_obj5[0:1000], label='object5')
plt.grid(True)
plt.margins(x=0, y=0)
plt.ylabel('number of names')
plt.xlabel('number of iterations')
plt.yticks(np.arange(0, 5, step = 1))
plt.legend()
plt.show()

plt.plot(storageTotal)
plt.grid(True)
plt.margins(x=0, y=0)
plt.ylabel('nStorage size')
plt.xlabel('number of iterations')
plt.show()

print("Final Communicative Success Rate: ")
print(sucList[-1]*100,"%")

print("Complete Communicative Success: ")
print("Iteration ",len(sucCount)- sucCount[::-1].index(0))

print("Lexicon Size: ")
print(lexTotal[-1])