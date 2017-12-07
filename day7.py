import re


#Matches program_name weight [prg, prg, prg]?
data_regex = re.compile('(\w+)\s*\((\d+)\)\s*(?:->\s*((?:\w+,?\s*)+))?')

class TowerPart:
    existing = {}

    def __init__(self, name):
        self.name = name
        self.weight = -1
        self.above = []
        self.below = None

    def addAbove(self, name):
        "Adds the towerpart to the above list, adds itself as the above parts below part."
        abovePart = TowerPart.existing.setdefault(name, TowerPart(name))
        self.above.append(abovePart)
        abovePart.below = self

    def getRoot(self):
        if self.below == None:
            return self
        else:
            return self.below.getRoot()

    def total_weight(self):
        return self.weight + sum(map(lambda t:t.total_weight(), self.above))

    def find_imbalance_fix(self, correction_amt = None):
        "The part that needs to be changed is the one in the tree which has programs correctly balanced above."
        above_weights = map(lambda t:(t, t.total_weight()), self.above)
        d = {}
        part = {}
        for (twr, weight) in above_weights:
            d[weight] = 1 + d.setdefault(weight, 0)
            part[weight] = twr
        
        wrong_part = None
        for weight in d:
            if d[weight] == 1:
                wrong_weight = weight
                wrong_part = part[weight]
            else:
                correct_weight = weight

        if wrong_part == None:
            return self.weight + correction_amt
        else:
            return wrong_part.find_imbalance_fix(correct_weight - wrong_weight) #If wrong weight too much, correction is -X , if too little +X


        return correct_weight

    def __str__(self):
        return "T({} ({}){})".format(self.name, self.weight, " -> " + str(self.above) if len(self.above) > 0 else "")

    def __repr__(self):
        return "T({} ({}))".format(self.name, self.weight)

def parse_line(line):
    name, weight, above_progs = data_regex.match(line).groups()
    weight = int(weight)

    if above_progs is not None:
        above_progs = above_progs.split(", ")
    else:
        above_progs = []

    part = TowerPart.existing.setdefault(name, TowerPart(name))
    part.weight = weight

    for prog in above_progs:
        part.addAbove(prog)
    

    return part


if __name__ == '__main__':
    data = []
    with open("input/day7.txt") as f:
        for line in f:
            towerpart = parse_line(line.strip())

    root = towerpart.getRoot()
    print("Task 1: Root is ", root.name)
    print("Task 2: Weight needed to restore balance is", root.find_imbalance_fix())
    
