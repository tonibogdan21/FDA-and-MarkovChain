from informatiiMarkov_Tema_1 import *
import re

class Markov(object):

    def __init__(self, SyntaxRules, rules, vocabulary):
        self.SyntaxRules = SyntaxRules
        self.rules = rules
        self.vocabulary = vocabulary

    def inputText(self):
        exists = False
        print('Vocabular:')
        for i in vocabulary:
            print(i)
        print('--------')
        while exists == False:
            text = input("Introduceti un text ce urmeaza a fi derivat utilizat algoritmul Markov. Textul trebuie sa contina cel putin un element din vocabularul de mai sus.")
            if any(s in text.split() for s in self.vocabulary):
                exists = True
                return text

    def extractreplacements(self, rules):
        return [ (matchobj.group('pat'), matchobj.group('repl'), bool(matchobj.group('term')))
                    for matchobj in re.finditer(self.SyntaxRules, self.rules)
                    if matchobj.group('rule')]

    def replace(self, text, replacements):
        while True:
            for pat, repl, term in replacements:
                if pat in text:
                    print(text)
                    text = text.replace(pat, repl, 1)
                    if term:
                        return text
                        break
            else:
                print(text)
                return text

    def reWriting(self):
        while True:
            text = self.inputText()
            self.replace(text, self.extractreplacements(rules))
            yesOrNo = input("Doriti sa mai derivati un alt cuvant? da sau nu: ")
            if yesOrNo == "nu":
                break

if __name__ == '__main__':
    ExempluMarkov = Markov(SyntaxRules, rules, vocabulary)
    ExempluMarkov.reWriting()
