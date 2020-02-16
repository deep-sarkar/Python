class TempConversion:
    def fahrenheit_celsius(self,temp_fahrenheit):
        if type(temp_fahrenheit) != int :
            raise NameError('Can not pass string argument')
        return round((temp_fahrenheit - 32) * 5/9)

    def celsius_fahrenheit(self,temp_celsius):
        if type(temp_celsius) != int :
            raise NameError('Can not pass string argument')
        return round(temp_celsius * 9/5 + 32)
        