class CurrencyConvertor:
    def Convertor(amount):
        convert = 0
        try:
            amount = float(amount)
            if (amount<0):
                raise ValueError()
            convert = round(amount*0.94, 1) 
        except ValueError:
            print('Entrez une valeur positive')
            convert = 0
        except:
            convert = 0

        return convert
