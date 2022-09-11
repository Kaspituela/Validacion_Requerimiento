import logging
class Pila:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
          try:
               self.items.append(item)
          except:
               logging.error("Error al pushear el texto: " + item)

     def pop(self):
          try:
               return self.items.pop()
          except:
               logging.error("Error al hacer pop en la pila")

     def value(self):
          try:
               return self.items[len(self.items)-1]
          except:
               logging.error("Error al obtener el valor del texto en la pila")

     def len(self):
          try:
               return len(self.items)
          except:
               logging.error("Error al obtener el tamaño de la pila")
     def longest(self):
          try:
               if(self.len() == 0):
                    logging.warning("No hay valores en la pila")
                    return 0
               auxPila = Pila()
               textLongest = []
               tamaño = 0
               while(self.len() > 0):
                    if(tamaño < len(self.value())):
                         textLongest = [self.value()]
                         tamaño = len(self.value())
                    elif(tamaño == len(self.value())):
                         textLongest.append(self.value())
                    auxPila.push(self.pop())
               self.reCreatePila(auxPila)
               return textLongest
          except:
               logging.error("Error al obtener el texto más largo de la pila")
     def shortest(self):
          try:
               if(self.len() == 0):
                    logging.warning("No hay valores en la pila")
                    return 0
               auxPila = Pila()
               textShortest = [self.pop()]
               tamaño = len(textShortest[0])
               auxPila.push(textShortest[0])
               while(self.len() > 0):
                    if(tamaño > len(self.value())):
                         textShortest = [self.value()]
                         tamaño = len(self.value())
                    elif(tamaño == len(self.value())):
                         textShortest.append(self.value())
                    auxPila.push(self.pop())
               self.reCreatePila(auxPila)
               return textShortest
          except:
               logging.error("Error al obtener el texto más corto de la pila")
     def reCreatePila(self, auxPila):
          try:
               while(auxPila.len() > 0):
                    self.push(auxPila.pop())
               return 0
          except:
               logging.error("Error al re-crear la pila")
     def printPila(self):
          try:
               auxPila = Pila()
               while(self.len() > 0):
                    print("{0}) {1}".format(self.len(), self.value()))
                    auxPila.push(self.pop())
               self.reCreatePila(auxPila)
          except:
               logging.error("Error al imprimir la pila")
     def printPos(self, pos):
          try:
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
          except:
               logging.error("Error al imprimir el texto de la pila")

               
logging.basicConfig(filename='Tarea1.log', filemode='w',level=logging.DEBUG, format = '[%(asctime)s] src:%(name)s %(levelname)s:%(message)s', datefmt='%Y-%m-%d:%H:%M:%S')
logging.info('Inicio del programa Tarea1')
p = Pila()
opt = 0
while(opt != "6"):
    print("=======================\nIngrese una opción\n0)Mostrar Pila\n1)Ingresar texto\n2)Texto más largo\n3)Texto más corto\n4)Imprimir texto\n5)Comparar tamaños\n6)Salir")   
    opt = input()
    if opt == "0":
        p.printPila() 
    elif opt == "1":
        print("Ingrese el texto")
        text = input()
        p.push(text)
        logging.info("Se ingresa a la pila el texto: " + text)
    elif opt == "2":
        textLongest = p.longest()
        text = '-'.join((str(n) for n in textLongest))
        print("Los textos más largos son: ",textLongest)
        logging.info("Se retorna el texto más largo: " + text)
    elif opt == "3":
        textShortest = p.shortest()
        print("Los textos más cortos son: ",textShortest)
        text = '-'.join((str(n) for n in textShortest))
        logging.info("Se retorna el texto más corto: " + text)
    elif opt == "4":
        p.printPila()
        print("Ingrese la posición de la pila")
        pos = input()
        try:
             if(int(pos) > p.len() or int(pos) == 0):
                  print("La pila no contiene la posición ingresada")
                  logging.warning('Se ingreso una posición que no se encuentra en la pila, el valor de la pos es: ' + pos)
             else:
                  print("Texto: "+ p.printPos(pos))
        except:
             print("Error al obtener la posición de la pila")
             logging.error("Error al obtener la posición de la pila")
    elif opt == "5":
        p.printPila()
        flag = 1
        print("Ingrese posicion 1")
        pos1 = input()
        try:
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
                       if(len(text1) > len(text2)):
                            print("El texto más largo es: ", text1)
                       elif(len(text1) < len(text2)):
                            print("El texto más largo es: ", text2)
                       else:
                            print("Los dos textos tienen el mismo tamaño")
                       logging.info("Se compara los textos '{0}' y '{1}'".format(text1,text2))
        except:
             print("Error al obtener la posición de la pila")
             logging.error("Error al obtener la posición de la pila")
