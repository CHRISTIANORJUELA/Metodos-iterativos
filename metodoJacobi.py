from sympy import *;
from fractions import *;
from itertools import repeat;
import time;
"""" ----Clase----
"""
class Variable:
   parada = False;
   def __init__(self , clave):
      self.clave = clave;
      self.valorActual = 0.0;
      self.valorAnterior = 0.0;
      self.ep = 999;
      self.iteracion = 0;
   
   def getClave(self):
      return self.clave;

   def getValorActual(self): return self.valorActual;

   def setValorActual(self,valor):self.valorActual = valor;
    
   def setValorAnterior(self,valor):self.valorAnterior = valor;
   
   def getEp(self):return self.ep;

   def setEp(self , ep):self.ep = ep;
   
   def getParada(self):return self.parada;

   def setParada(self,valor):self.parada = valor;

   def getIteracion(self):return self.iteracion;

   def setIteracion(self, iteracion):self.iteracion = iteracion;
   
   def print(self):print("clave ",self.clave," valor  ",float(self.valorActual),"Iteracion ",self.iteracion," parada ",self.parada);
    
""""
------------------Utilitarios------------------------;
"""
def obtenerParVariables(contFunciones,listFunciones):
    listParMomento = list();
    listParMomento.append(listFunciones[len(listFunciones)-contFunciones]);
    listParVariables = calcularNumeroVariables(listParMomento);
    listParMomento.clear();
    return listParVariables;

def obtenerParVariableSinContador(l):
    listParMomento = list();
    listParMomento.append(l);
    listParVariables = calcularNumeroVariables(listParMomento);
    listParMomento.clear();
    return listParVariables;

def obtenerNombre(listObjects,listParVariables):
   for l in listObjects:
      if l.clave not in listParVariables:
         return l.clave;
"""
--------------------*****----------------------------
"""
def llenarListFunciones(numeroFunciones):
    listFunciones = list();
    """""
    listFunciones.append(input("Digite la funcion despejada"));
    """
    listFunciones.append("(0.4 + x2 +x3)/2");
    listFunciones.append("(4.7 -3*x1-2*x3)/5");
    listFunciones.append("(7.9 -x1 -3*x2)/4");
    return listFunciones;

def listaVariablesSimplificado(lisVariables):
   listNewVariables = list();
   for valor in lisVariables:
      if valor not in listNewVariables:
         listNewVariables.append(valor);
   return listNewVariables;

def calcularNumeroVariables(listFunciones):
    variable = ["x1","x2","x3","x4","x5","x5","x7","x8","x10"]
    listVariables = list();
    for i in range(len(listFunciones)):
        cadena = listFunciones[i];
        for w in range(len(variable)):
          if(variable[w] in cadena):
            listVariables.append(variable[w]);
    return listVariables;
    
def ordenarVariables(listLetrasVariables):
   listCadena = list();
   listNewCadena = list();
   for valor in listLetrasVariables:
      for indice in valor:
         if(indice.isdigit()):
          listCadena.append(indice);
   listCadena.sort();
   for valor in listCadena:
      valor += "x";
      listNewCadena.append(valor[::-1]);
      valor = valor[::-1];
   return listNewCadena;

def getValorListaObjetos(v,listaObjetos):
   for l in listaObjetos:
      if(l.clave == v):
         return l.getValorActual();

def calcularValor(contFunciones,listFunciones,listaObjetos):
   listParVariables = obtenerParVariables(contFunciones,listFunciones);
   newDiccionario = {};
   for v in listParVariables:
      valor =  getValorListaObjetos(v,listaObjetos);
      newDiccionario[symbols(v)] =valor;
   funcion = Fraction(str(sympify(listFunciones[len(listFunciones)-contFunciones]).subs(newDiccionario)));
   listParVariables.clear();
   newDiccionario.clear();
   return funcion;

def updateListObjects(listObjects,nombreVariableAmodificar,xtotal,contListFunciones,cont,cualEs):
   if(cualEs == "actual"):
    for l in listObjects:
     if l.clave == nombreVariableAmodificar:
      l.setValorActual(xtotal[len(xtotal)-contListFunciones]);
      l.setIteracion(cont);
   elif cualEs =="anterior":
      for l in listObjects:
       if l.clave == nombreVariableAmodificar:
        l.setValorAnterior(xtotal[len(xtotal)-contListFunciones]);

def modifyListObjects(listObjects,listFunciones,xtotal,cont,cualEs):
  contListFunciones = len(listFunciones);
  for l in listFunciones:
    listParVariables = obtenerParVariableSinContador(l);
    nombreVariableAmodificar = obtenerNombre(listObjects,listParVariables);
    pase = filter(lambda x: x.getClave() == nombreVariableAmodificar and x.getParada()==False,listObjects)
    if pase:
       updateListObjects(listObjects,nombreVariableAmodificar,xtotal,contListFunciones,cont,cualEs);
    contListFunciones -= 1;
    listParVariables.clear();


def crearObjetos(listVariablesOrdenada):
   listaObjetos = list();
   for l in listVariablesOrdenada:
    variable = Variable(l)
    listaObjetos.append(variable);
   return listaObjetos

def setsEp(listaObjetos,sita):
   for l in listaObjetos:
      l.setEp(abs((l.valorActual-l.valorAnterior)/l.valorActual)*100)
      if l.getEp() <= sita:
         l.setParada(True);
   return any(l.getParada()==False for l in listaObjetos); 
  
def calcularRaiz(numeroFunciones):  
    listFunciones = llenarListFunciones(numeroFunciones);
    inicio = time.time();
    listLetrasVariables = calcularNumeroVariables(listFunciones);
    listNewVariables = listaVariablesSimplificado(listLetrasVariables);
    listVariablesOrdenada = ordenarVariables(listNewVariables);
    xtotal = list(repeat([],numeroFunciones));
    listaObjetos = crearObjetos(listVariablesOrdenada);
    sita = 0.005;
    contFunciones = numeroFunciones;
    cont = 1;
    seguir = True;
    while seguir == True and cont<=100:
       contFunciones = numeroFunciones;
       if cont>=2:
         modifyListObjects(listaObjetos,listFunciones,xtotal,cont,"anterior");
       for i in range(numeroFunciones):
        xtotal[len(xtotal)-contFunciones] = calcularValor(contFunciones,listFunciones,listaObjetos);
        contFunciones -= 1;
       modifyListObjects(listaObjetos,listFunciones,xtotal,cont,"actual");
       if cont>=2:
          seguir = setsEp(listaObjetos,sita);
       cont += 1;   
    print(xtotal);
    final = time.time();
    resultado = final-inicio;
    print("Tiempo de ejecucion ",resultado)
    for l in listaObjetos:
       print(l.print());
numeroFunciones = int(input("Digite el numero de funciones"));
calcularRaiz(numeroFunciones);


   