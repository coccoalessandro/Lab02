class Dictionary:
    def __init__(self, dictionary = {}):

        self.dictionary = dictionary
        pass

    def addWord(self, entry):

        campi = entry.split(' ')
        n = 1
        flag = False
        for campo in self.dictionary:
            if campi[0].lower().strip() == campo:
                flag = True
                while n <= len(campi) - 1:
                    self.dictionary[campo].append(campi[n])
                    n += 1
        if flag == False:
            self.dictionary[campi[0]] = []
            while n <= len(campi) - 1:
                self.dictionary[campi[0]].append(campi[n])
                n += 1
        print(self.dictionary)
        pass

    def translate(self, query):

        mystr = ""
        for campo in self.dictionary:
            if campo == query:
                for traduzione in self.dictionary[campo]:
                    mystr += traduzione + '\n'
        print(mystr)



    def translateWordWildCard(self, query):

        n = query.find('?')
        mystr = ""

        new = query.replace("?", "")
        for campo in self.dictionary:
            campoin = campo
            if len(campo) > n:
                nuovo = campo[:n] + campo[n + 1:]
                if nuovo == new:
                    for traduzione in self.dictionary[campo]:
                        mystr += traduzione + '\n'
        print(mystr)
