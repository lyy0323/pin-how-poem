import random


bankfile = "./bank.txt"
savefile = "./save.txt"

class Dice:
    '''
    A class to represent a dice.
    Attributes:
        id: int, the id of the dice.
        tone: str, the tone of the dice, "ping" or "ze".
        words: list, the words of the dice, a list of strings. Default with length of 6.
        status: str, the current status of the dice, a string. Imagine that as if the top side of the dice. Default with the first word in words.
    Methods:
        __str__(): return the string representation of the dice.
        __repr__(): return the string representation of the dice.
        roll(): roll the dice, return the current status of the dice.
        __init__(): initialize the dice with id, tone and words.
    '''

    def __init__(self, _id, tone, words):
        '''
        Initialize the dice with id, tone and words.
        id: int, the id of the dice.
        tone: str, the tone of the dice, "ping" or "ze".
        words: list, the words of the dice, a list of strings. Default with length of 6.
        status: str, the current status of the dice, a string. Imagine that as if the top side of the dice. Default with the first word in words.
        '''
        self.id = _id
        self.tone = tone
        self.words = words
        self.status = self.words[0]

    def __str__(self):
        '''
        Return the string representation of the dice.
        '''
        return f"{self.id} ({'平' if self.tone == 'ping' else '仄'}): {' | '.join(self.words)}"
    
    def __repr__(self):
        '''
        Return the string representation of the dice.
        '''
        return self.__str__()
    
    def roll(self):
        '''
        Roll the dice, return the current status of the dice.
        '''
        self.status = random.choice(self.words)
        return self.status

class DiceBank:
    '''
    A class to represent a bank of dices.
    Attributes:
        dices: dict, a dictionary of dices, with keys "double" and "single", and values are dictionaries of dices.
        sample: list, a list of tuples, each tuple contains the length, pingze and id of the dice.
        result: str, the result of the roll.
    Methods:
        __str__(): return the string representation of the bank.
        __repr__(): return the string representation of the bank.
        draw(rule): draw a sample from the bank, according to the rhyme rule.
        roll(): roll the dices in sample, return the result.
    '''

    def __init__(self, bankfile):
        '''
        Initialize the bank with a file.
        '''
        self.dices = {"double": {}, "single": {}}
        self.sample = []
        self.result = ""
        with open(bankfile, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                line_no = int(line.split(" ")[0].strip("."))
                line = line.strip().split(" ", maxsplit=1)[1]
                line = [_.split(" ") for _ in line.split(" | ")]
                if len(line[0][0]) == 1:
                    words_property = "single"
                else:
                    words_property = "double"
                self.dices[words_property][line_no] = (Dice(line_no, "ping", line[0]), Dice(line_no, "ze", line[1]))
        self.single_id = list(self.dices["single"].keys())
        self.double_id = list(self.dices["double"].keys())
    
    def __str__(self):
        return f"DiceBank: {self.dices}"

    def draw(self, rule: list):
        '''
        Draw a sample from the bank, according to the rhyme rule.

        rule: list, a list of tuples, each tuple contains the length and ping-ze. Just need to define the first half of the contrasting sentence.

        For example, if the rule is [("double", "ze"), ("double", "ping"), ("single", "ping"), ("double", "ze")], then the second half of the contrasting sentence is [("double", "ping"), ("double", "ze"), ("single", "ze"), ("double", "ping")], which will be generated automatically.
        '''
        # a sample of rule: [("double", "ze"), ("double", "ping"), ("single", "ping"), ("double", "ze")]
        self.sample = []
        for r in rule:
            self.sample.append((r[0], r[1], random.choice(eval(f"self.{r[0]}_id"))))
        return self
    
    def roll(self):
        '''
        Roll the dices in sample, and return the result. Does not change the sample and the rule.
        '''
        # roll the dices in sample
        result_sentence = ""
        if self.sample:
            for length, pingze, _id in self.sample:
                word = self.dices[length][_id][0 if pingze == 'ping' else 1].roll()
                result_sentence += word
            result_sentence += "，"
            for length, pingze, _id in self.sample:
                word = self.dices[length][_id][1 if pingze == 'ping' else 0].roll()
                result_sentence += word
            result_sentence += "。"
            self.result = result_sentence
        else:
            self.result = ""
            print("No sample drawn, please draw a sample first.")
        return self.result


def experiment(dicebank: DiceBank, rule: list, draws=10, rolls=1, save=False, save_attr=False):
    '''
    Experiment with the dice bank, draw a sample and roll the dices.
    dicebank: DiceBank, the dice bank to use.
    rule: list, a list of tuples, each tuple contains the length and ping-ze. Just need to define the first half of the contrasting sentence.
    draws: int, the number of draws. Default is 10.
    rolls: int, the number of rolls. Default is 1.
    save: bool, whether to save the result to a file. Default is False.
    save_attr: bool, whether to save the attributes of the dices to a file. Default is False.
    '''
    for _ in range(draws):
        dicebank.draw(rule)
        for _1 in range(rolls):
            result = dicebank.roll()
            print(result)
            if save:
                with open(savefile, "a", encoding="utf-8") as f:
                    f.write(result)
                if save_attr:
                    with open(savefile, "a", encoding="utf-8") as f:
                        f.write(" | " + str(dicebank.sample) + "\n")
                else:
                    with open(savefile, "a", encoding="utf-8") as f:
                        f.write("\n")
        if save:
            with open(savefile, "a", encoding="utf-8") as f:
                f.write("-----\n")


if __name__ == "__main__":
    Bank = DiceBank(bankfile)
    rule = [("double", "ze"), ("double", "ping"), ("single", "ping"), ("double", "ze")]
    experiment(Bank, rule, draws=20, rolls=5, save=True, save_attr=True)
