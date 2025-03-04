import dictionary
from dictionary import *

class Translator:

    def __init__(self):
        self.dictionary = {}
        self.diz = Dictionary()
        pass

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Stampa tutto il dizionario
        # 5. Exit

        print(f'-------------------------------\n   Translator Alien-Italian\n-------------------------------\n1. Aggiungi una parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Stampa tutto il dizionario\n5. Exit\n-------------------------------\n')
        pass

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary

        inf = open(dict, 'r', encoding='utf-8')
        righe = inf.readlines()

        for riga in righe:
            campi = riga.split(' ')
            self.dictionary[campi[0].lower().strip()] = [campi[1].lower().strip()]
        self.diz = Dictionary(self.dictionary)

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        self.diz.addWord(entry)
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        self.diz.translate(query)
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        self.diz.translateWordWildCard(query)
        pass

    def printAllDict(self):
        mystr = ''
        for key in self.dictionary:
            mystr += key + ' ; '
            for traduzione in self.dictionary[key]:
                mystr += traduzione + ', '
        print(mystr)