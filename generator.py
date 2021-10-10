import random, string, json

def read_file(name):
    with open(name, "r") as f:
        return f.readlines()

verbs = read_file("verbs")
nounsRaw = read_file("nouns")
transitions = read_file("sentence-transitions")
adjectives = read_file("adjectives")

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

def gen_random(arr):
    return arr[random.randint(0, len(arr) - 1)].strip()

def noun_to_posessive(noun):
    try:
        return bonusNounsPosessive[bonusNouns.index(noun)]
    except:
        pass

    if noun.endswith("s"):
        return noun + "'"
    else:
        return noun + "'s"

def gen_verb(isING):
    verb = gen_random(verbs)
    if isING:
        verb = verb_to_ing(verb)
    else:
        if(verb.lower().endswith("s")): #so words like "cross" end up as "crosses" and not "crosss"
            verb += "e"
        verb += "s"

    verbPreps = ["on", "to", "with"]
    return verb + " " + verbPreps[random.randint(0, len(verbPreps) - 1)] + " "

def _generate_beginning_format_random():
    if random.randint(0, 100) > 50:
        return "the "
    else:
        return ""

def gen_noun(all_nouns=True):
    if all_nouns == True:
        noun_arr = nouns
    else:
        noun_arr = nounsRaw

    noun = gen_random(noun_arr)
    formatting_rules = [("(T)", lambda: "the "), ("(P)", lambda: ""),("(R)", _generate_beginning_format_random)]
    for rule in formatting_rules:
        if noun.endswith(rule[0]):
            return rule[1]() + noun[:len(rule[0])]

    #if the noun doesn't have any special formatting rules applied
    if noun[0].lower() in vowels:
        return "an " + noun
    else:
        return "a " + noun
    

def generate(startsWithING = False, nounCount = None):
    if nounCount == None:
        nounCount = random.randint(0, 5)

    sentence = ""
    if startsWithING:
        if nounCount == 0:
            return verb_to_ing(gen_random(verbs))

        sentence += gen_verb(True)
    
    sentence += gen_noun(False)
    for nounNum in range(nounCount):
        isING = random.randint(0, 100) > 50
        verbSeperator = " "
        if isING:
            possibleSeperators = ["was", "is", "is going to"]
            verbSeperator = " " + possibleSeperators[random.randint(0, len(possibleSeperators) - 1)] + " "

        is_possessed_noun = (random.randint(0, 100) > 60)
        nounAfter = gen_noun(False)
        if(is_possessed_noun):
            adjectivesArr = []
            adjecStr = " "
            if random.randint(0, 100) > 40: #make it so adjectives have a chance of not spawning
                for i in range(random.randint(1, 4)):
                    adjectivesArr.append(gen_random(adjectives))
                adjecStr = " " + ", ".join(adjectivesArr) + " "

            nounAfter = noun_to_posessive(nounAfter) + adjecStr + gen_random(nounsRaw) #very important that gen_random is used instead of gen_noun

        sentence += " " + gen_random(transitions) + " " + gen_noun() + verbSeperator + gen_verb(isING) + nounAfter

    
    return sentence.lower()

if __name__ == "__main__":
    while True:
        try:
            startING = False
            if input("Start with ING? (Press Y): ").strip().lower() == "y":
                startING = True
                
            print(generate(startING, int(input("How much nouns? "))))
        except Exception as e:
            print(f"Error: {e}")
