class CurrencyConvertor:
    def Convertor(amount):
        convert = 0
        try:
            amount = float(amount)
            
            if amount < 0:
                raise SyntaxError()
            convert = round(amount*0.94, 1) 
        except SyntaxError:
            print(amount)
            print('Entrez une valeur positive')
            convert = 0
        except TypeError:
            print("L'entrée doit etre un nombre")
            convert = 0
        except:
            convert = None

        return convert
