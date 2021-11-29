import time

class TrafficLight:

    colors = {'Red' : 7, 'Yellow' : 2, 'Green' : 1}

    def running (self, color):
       self.__color = color
       for i in color:
           print (f'color is {i}')
           time.sleep(color[i])
       return 'GO'

result = TrafficLight()
print(result.running(TrafficLight.colors))
