class CurrencyConvertor:
    def Convertor(amount):
        convert = 0
        try:
            amount = float(amount)
            convert = round(amount*0.94, 1) 
        except:
            convert = 0
        
        return convert
