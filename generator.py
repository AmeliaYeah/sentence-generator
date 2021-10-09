import random, string, json

verbs = open("verbs", "r").readlines()
nounsRaw = open("nouns", "r").readlines()
transitions = open("sentence-transitions", "r").readlines()
adjectives = open("adjectives", "r").readlines()

bonusNouns = ["they", "you", "I"]
bonusNounsPosessive = ["their", "your", "my"]
bonusNounsAfterVerb = ["them", "you", "me"]
nouns = nounsRaw + bonusNouns

vowels = list("aeiou")
consonants = [char for char in string.ascii_lowercase if char not in vowels]

def calc_syllables(verb):
    syls = 0
    for char in verb:
        if char in vowels:
            syls += 1
    return syls

def verb_to_ing(verb):
    verb = verb.lower()
    if verb.endswith("e") and not verb.endswith("ee"):
        if verb.endswith("ie"):
            verb = verb[:-2] + "y"
        else:
            verb = verb[:-1]
    elif calc_syllables(verb) == 1 and verb[-2] in vowels and verb[-1] in consonants:
        if verb[-1] not in list("wxy"):
            verb += verb[-1]
    elif len(verb) >= 3 and verb[-3] in consonants and verb[-2] in vowels and verb.endswith("l"):
        verb += "l"
    
    return verb + "ing"

def genRandom(arr):
    return arr[random.randint(0, len(arr) - 1)].strip()

def nounToPosessive(noun):
    try:
        return bonusNounsPosessive[bonusNouns.index(noun)]
    except:
        pass

    if noun.endswith("s"):
        return noun + "'"
    else:
        return noun + "'s"

def genVerbString(isING):
    verb = genRandom(verbs)
    if isING:
        verb = verb_to_ing(verb)
    else:
        if(verb.lower().endswith("s")): #so words like "cross" end up as "crosses" and not "crosss"
            verb += "e"
        verb += "s"

    verbPreps = ["on", "to", "with"]
    return verb + " " + verbPreps[random.randint(0, len(verbPreps) - 1)] + " "

def generateBeginningFormatRandom():
    if random.randint(0, 100) > 50:
        return "the "
    else:
        return ""

def getNoun(all_nouns=True):
    if all_nouns == True:
        noun_arr = nouns
    else:
        noun_arr = nounsRaw

    noun = genRandom(noun_arr)
    formatting_rules = [("(T)", lambda: "the "), ("(P)", lambda: ""),("(R)", generateBeginningFormatRandom)]
    for rule in formatting_rules:
        if noun.endswith(rule[0]):
            return rule[1]() + noun[:len(rule[0])]

    #if the noun doesn't have any special formatting rules applied
    if noun[0].lower() in vowels:
        return "an " + noun
    else:
        return "a " + noun
    

def generate_sentence(startsWithING = False, nounCount = None):
    if nounCount == None:
        nounCount = random.randint(0, 5)

    sentence = ""
    if startsWithING:
        if nounCount == 0:
            return verb_to_ing(genRandom(verbs))

        sentence += genVerbString(True)
    
    sentence += getNoun(False)
    for nounNum in range(nounCount):
        isING = random.randint(0, 100) > 50
        verbSeperator = " "
        if isING:
            possibleSeperators = ["was", "is", "is going to"]
            verbSeperator = " " + possibleSeperators[random.randint(0, len(possibleSeperators) - 1)] + " "

        is_possessed_noun = (random.randint(0, 100) > 60)
        nounAfter = getNoun(False)
        if(is_possessed_noun):
            adjectivesArr = []
            adjecStr = " "
            if random.randint(0, 100) > 40: #make it so adjectives have a chance of not spawning
                for i in range(random.randint(1, 4)):
                    adjectivesArr.append(genRandom(adjectives))
                adjecStr = " " + ", ".join(adjectivesArr) + " "

            nounAfter = nounToPosessive(nounAfter) + adjecStr + genRandom(nounsRaw) #very important that genRandom is used instead of getNoun

        sentence += " " + genRandom(transitions) + " " + getNoun() + verbSeperator + genVerbString(isING) + nounAfter

    
    return sentence