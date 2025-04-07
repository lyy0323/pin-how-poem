import random


bankfile = "./bank.txt"
savefile = "./save.txt"

# print(bank_1)
# print(bank_2)

class Dice:
    def __init__(self, _id, tone, words):
        self.id = _id
        self.tone = tone
        self.words = words
        self.status = self.words[0]

    def __str__(self):
        return f"{self.id} ({'平' if self.tone == 'ping' else '仄'}): {' | '.join(self.words)}"
    
    def __repr__(self):
        return self.__str__()
    
    def roll(self):
        self.status = random.choice(self.words)
        return self.status

class DiceBank:
    def __init__(self, bankfile):
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
        # a sample of rule: [("double", "ze"), ("double", "ping"), ("single", "ping"), ("double", "ze")]
        self.sample = []
        for r in rule:
            self.sample.append((r[0], r[1], random.choice(eval(f"self.{r[0]}_id"))))
        return self
    
    def roll(self):
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
    # print(Bank.dices)
    rule = [("double", "ze"), ("double", "ping"), ("single", "ping"), ("double", "ze")]
    experiment(Bank, rule, draws=10, rolls=5, save=True, save_attr=True)
