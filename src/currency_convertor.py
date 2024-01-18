class CurrencyConvertor:
    def Convertor(amount):
        convert = 0
        try:
            convert = round(float(amount)*0.94, 1) 
        except:
            convert = 0
        
        return convert
