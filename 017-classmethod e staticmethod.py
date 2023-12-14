class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        print(self)


    @classmethod
    def de_string(cls, data_string): # 10-10-2021
        print(cls)
        dia, mes, ano = map(int, data_string.split('-'))
        data = cls(dia, mes, ano)
        return data
    
    @staticmethod
    def is_date_valid(data_string):
        dia, mes, ano = map(int, data_string.split('-'))
        return dia <=31 and mes <=12 and ano <=2024


data = Data(10,10,10)


# <__main__.Data object at 0x0000025DE2493F80>
# <class '__main__.Data'>
data1 = Data.de_string("10-10-2023")
print(data1)

print(data1.is_date_valid("12-06-2023"))