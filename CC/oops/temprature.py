''' Create a Temperature class.
Make two methods :
1. convertFahrenheit - It will take celsius and will print it into
Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into
Celsius.
(Medium) (5'''

class Tempersture:
    
    def convert(self):
        n = int(input("your temperature= "))
        f = (input(" Type C for Celcius Conversion \n Type F for Fahrenhite Conversion \n = "))
        if f == "F" :
            d = n * 5/9  - 32
            print(f"temprature in {d}celsius") 
        else :   
            c = n * 9/5 + 32
            print(f"temprature in {c}fahrenheit")

t = Tempersture()      
t.convert()         

    
         




