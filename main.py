import translator as tr

t = tr.Translator()

t.loadDictionary("dictionary.txt")

while(True):

    t.printMenu()

    txtIn = input()

    # Add input control here!

    if txtIn.isdigit() :
        if int(txtIn) == 1:
            print('Ok, quale parola devo aggiungere?')
            txtIn = input()
            flag = False
            for parola in txtIn.split(" "):
                if parola.isalpha() == False:
                    flag = True
                    print("Errore inserimento")
            if flag == False:
                t.handleAdd(txtIn)
                print("Aggiunta!")
                pass
        elif int(txtIn) == 2:
            print('Ok, quale parola devo cercare?')
            txtIn = input()
            flag = False
            for parola in txtIn.split(" "):
                if parola.isalpha() == False:
                    flag = True
                    print("Errore inserimento")
            if flag == False:
                t.handleTranslate(txtIn.strip())
                pass
        elif int(txtIn) == 3:
            print('Ok, quale parola devo cercare?')
            txtIn = input()
            flag = False
            for parola in txtIn.split(" "):
                if parola.isalpha() == False:
                    flag = True
                    print("Errore inserimento")
            if flag == False:
                t.handleWildCard(txtIn.strip())
            pass
        elif int(txtIn) == 4:
            t.printAllDict()
        elif int(txtIn) == 5:
            break
    else :
        print("Inserire un numero da 1 a 5")