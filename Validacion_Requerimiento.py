import logging
class Pila:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def value(self):
         return self.items[len(self.items)-1]

     def len(self):
         return len(self.items)
     def longest(self):
         if(self.len() == 0):
             logging.warning("No hay valores en la pila")
             return 0
         auxPila = Pila()
         textLongest = ""
         while(self.len() > 0):
             if(len(textLongest) < len(self.value())):
                 textLongest = self.value()
             auxPila.push(self.pop())
         self.reCreatePila(auxPila)
         return textLongest
     def shortest(self):
         if(self.len() == 0):
             logging.warning("No hay valores en la pila")
             return 0
         auxPila = Pila()
         textShortest = self.value()
         while(self.len() > 0):
             if(len(textShortest) > len(self.value())):
                 textShortest = self.value()
             auxPila.push(self.pop())
         self.reCreatePila(auxPila)
         return textShortest
     def reCreatePila(self, auxPila):
         while(auxPila.len() > 0):
             self.push(auxPila.pop())
         return 0
     def printPila(self):
         auxPila = Pila()
         while(self.len() > 0):
             print("{0}) {1}".format(self.len(), self.value()))
             auxPila.push(self.pop())
         self.reCreatePila(auxPila)
     def printPos(self, pos):
         if(self.len() == 0):
             logging.warning("No hay valores en la pila")
             return ""
         auxPila = Pila()
         text = ""
         while(self.len() > int(pos)):
             auxPila.push(self.pop())
         text = self.value()
         self.reCreatePila(auxPila)
         return text
logging.basicConfig(filename='Tarea1.log', filemode='w',level=logging.DEBUG, format = '[%(asctime)s] src:%(name)s %(levelname)s:%(message)s', datefmt='%Y-%m-%d:%H:%M:%S')
logging.info('Inicio del programa Tarea1')
p = Pila()
opt = 0
while(opt != "6"):
    print("=======================\nIngrese una opción\n1)Ingresar texto\n2)Texto más largo\n3)Texto más corto\n4)Imprimir texto\n5)Comparar tamaños\n6)Salir")   
    opt = input()
    if opt == "1":
        print("Ingrese el texto")
        text = input()
        p.push(text)
        logging.info("Se ingresa a la pila el texto: " + text)
    elif opt == "2":
        textLongest = p.longest()
        print("Texto más largo: ",textLongest)
        logging.info("Se retorna el texto más largo: " + textLongest)
    elif opt == "3":
        textShortest = p.shortest()
        print("Texto más corto: ",textShortest)
        logging.info("Se retorna el texto más corto: " + textShortest)
    elif opt == "4":
        p.printPila()
        print("Ingrese la posición de la pila")
        pos = input()
        if(int(pos) > p.len() or int(pos) == 0):
            print("La pila no contiene la posición ingresada")
            logging.warning('Se ingreso una posición que no se encuentra en la pila, el valor de la pos es: ' + pos)
        else:
            print("Texto: "+ p.printPos(pos))
    elif opt == "5":
        p.printPila()
        flag = 1
        print("Ingrese posicion 1")
        pos1 = input()
        if(int(pos1) > p.len() or int(pos1) == 0):
            print("La pila no contiene la posición ingresada")
            logging.warning('Se ingreso una posición que no se encuentra en la pila, el valor de la pos es: ' + pos1)
            flag = 0
        else:
             text1 = p.printPos(pos1)
        if (flag == 1):
             print("Ingrese posicion 2")
             pos2 = input()
             if(int(pos2) > p.len() or int(pos2) == 0):
               print("La pila no contiene la posición ingresada")
               logging.warning('Se ingreso una posición que no se encuentra en la pila, el valor de la pos es: ' + pos2)
             else:
               print("Texto: {0} ; Tamaño: {1}".format(text1,len(text1)))
               text2 = p.printPos(pos2)
               print("Texto: {0} ; Tamaño: {1}".format(text2,len(text2)))
               logging.info("Se compara los textos '{0}' y '{1}'".format(text1,text2))
