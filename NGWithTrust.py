import random
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

class Agent:
    def __init__(self, Lexicon, tLev, nTrust, Name):
        self.Lexicon = Lexicon
        self.tLev = tLev
        self.nTrust = nTrust
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

def print_good_s(dictionary):
    print()
    counter = 0
    for x, y in dictionary.items():
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
agent1 = Agent(lex1, tLev1, nTrust1, "agent1")
agent2 = Agent(lex2, tLev2, nTrust2, "agent2")
agent3 = Agent(lex3, tLev3, nTrust3, "agent3")
agent4 = Agent(lex4, tLev4, nTrust4, "agent4")
agent5 = Agent(lex5, tLev5, nTrust5, "agent5")
agent6 = Agent(lex6, tLev6, nTrust6, "agent6")
agent7 = Agent(lex7, tLev7, nTrust7, "agent7")
agent8 = Agent(lex8, tLev8, nTrust8, "agent8")
agent9 = Agent(lex9, tLev9, nTrust9, "agent9")
agent10 = Agent(lex10, tLev10, nTrust10, "agent10")
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
                    hearer.nTrust[obj] = hearer.tLev[speaker.Name]
            #Hearer uses a different name:
            else:
                #We change the name only if it is heard from a more trusted speaker
                #If it is heard from a more trusted speaker:
                if hearer.tLev[speaker.Name] > hearer.nTrust[obj]:
                    hearer.Lexicon[obj] = [name]
                    hearer.nTrust[obj] = hearer.tLev[speaker.Name]
                #If it is heard from an equally trusted speaker:
                elif hearer.tLev[speaker.Name] == hearer.nTrust[obj]:
                    hearer.Lexicon[obj].append(name)
                countFail = countFail+1
                sucCount.append(0)
        #Hearer has no name:
        else:
            hearer.Lexicon[obj] = [name]
            hearer.nTrust[obj] = hearer.tLev[speaker.Name]
            countFail = countFail+1
            sucCount.append(0)
    #Speaker has no name:
    else:
        name = gen_name()
        speaker.Lexicon[obj] = [name]
        countFail = countFail+1
        sucCount.append(0)
    counter = counter + 1
    if counter == 50:
        sucList.append(countSuc/(countSuc+countFail))
        counter = 0
        countSuc = 0
        countFail = 0
    lexTotal.append(lex_counter(agent1))
    t_obj1.append(agent1.nTrust['object1'])
    t_obj2.append(agent1.nTrust['object2'])
    t_obj3.append(agent1.nTrust['object3'])
    t_obj4.append(agent1.nTrust['object4'])
    t_obj5.append(agent1.nTrust['object5'])
#NGLoopEnd
    
print("Agent1's tLev:")
print_good_s(agent1.tLev)
print("Agent1's nTrust:")
print_good_s(agent1.nTrust)
print("Agent1's Lexicon:")
print_good(agent1.Lexicon)
print("Agent2's Lexicon:")
print_good(agent2.Lexicon)
print("Agent3's tLev:")
print_good_s(agent3.tLev)
print("Agent3's nTrust:")
print_good_s(agent3.nTrust)
print("Agent3's Lexicon:")
print_good(agent3.Lexicon)
print("Agent4's tLev:")
print_good_s(agent4.tLev)
print("Agent4's nTrust:")
print_good_s(agent4.nTrust)
print("Agent4's Lexicon:")
print_good(agent4.Lexicon)
print("Agent5's tLev:")
print_good_s(agent1.tLev)
print("Agent5's nTrust:")
print_good_s(agent1.nTrust)
print("Agent5's Lexicon:")
print_good(agent5.Lexicon)
print("Agent6's tLev:")
print_good_s(agent6.tLev)
print("Agent6's nTrust:")
print_good_s(agent6.nTrust)
print("Agent6's Lexicon:")
print_good(agent6.Lexicon)
print("Agent7's tLev:")
print_good_s(agent7.tLev)
print("Agent7's nTrust:")
print_good_s(agent7.nTrust)
print("Agent7's Lexicon:")
print_good(agent7.Lexicon)
print("Agent8's tLev:")
print_good_s(agent8.tLev)
print("Agent8's nTrust:")
print_good_s(agent8.nTrust)
print("Agent8's Lexicon:")
print_good(agent8.Lexicon)
print("Agent9's tLev:")
print_good_s(agent9.tLev)
print("Agent9's nTrust:")
print_good_s(agent9.nTrust)
print("Agent9's Lexicon:")
print_good(agent9.Lexicon)
print("Agent10's tLev:")
print_good_s(agent10.tLev)
print("Agent10's nTrust:")
print_good_s(agent10.nTrust)
print("Agent10's Lexicon:")
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

axis_x = np.arange(0, 550, 50)
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

print("Final Communicative Success Rate: ")
print(sucList[-1]*100,"%")

print("Complete Communicative Success: ")
print("Iteration ",len(sucCount)- sucCount[::-1].index(0))

print("Lexicon Size: ")
print(lexTotal[-1])