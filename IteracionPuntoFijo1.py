from sympy import *
class Variables:
   cont = 0;
   def __init__(self , valor):
      self .valor = valor;
      self.iteracion = Variables.cont;
      self.ep = 100;
      Variables.cont += 1;

   def setEp(self,ep):
    self.ep = ep;
   def print(self):
      print("Valor : ",self.valor," iteracion : ",self.iteracion," Ep : ",self.ep)

def buscarIntervalo(limiteInferior,limiteSuperior):
       intervalo = list();
       rango_inferior = limiteInferior
       rango_superior = limiteSuperior
       diferencia = abs((rango_inferior)-(rango_superior));
       if(diferencia<1.0):
          diferenciaComvertido = diferencia*10;
          intervalo.append(rango_inferior);
          for i in range(int(diferenciaComvertido)):
           intervalo.append(round((intervalo[len(intervalo)-1]+0.1),1));
       else:
          intervalo.append(rango_inferior);
          for i in range(int(diferencia*10)):
            intervalo.append(round((intervalo[len(intervalo)-1]+0.1),1)); 
       print(intervalo);
       return intervalo;

def verificarConvergencia(funcionGeneral,intervalo):
 x = symbols('x')
 listSignos = list();
 funcionDeriva = str((diff(funcionGeneral,x)));
 contMenos = 0;
 contMas = 0;
 for i in intervalo:
  listSignos.append(sympify(funcionDeriva).subs({x:i}));
 for l in listSignos:
    if l <0 :
        contMenos+=1;
    elif l>0:
        contMas += 1;
 return True if contMenos==len(intervalo) or contMas==len(intervalo) else False;

def verificarValorEnIntervalo(valor,limiteInferior,limiteSuperior):
   return True if valor>= limiteInferior and valor <= limiteSuperior else False;

def iterarDespeje(funcionDespejada,intervalo):
    x = symbols('x');
    derivadaDelDespeje = str(diff(funcionDespejada,x));
    valores = list();
    seguro = True;
    cont = 1;
    for i in intervalo:
     valores.append(sympify(derivadaDelDespeje).subs({x:i}));
     if(abs(valores[len(valores)-1])>=1):
        seguro = False;
        print("El valor ",valores[len(valores)-1]," Es mayor que 1 con respecto a la derivada de: ",derivadaDelDespeje);
        break;
     cont += 1;
    if(seguro):
       print("El despeje de la funcion seleccionado ",funcionDespejada," es correcto");
       print("");
       print(valores);
    return cont if seguro==False else False
       
def calcularValor(limiteInferior,limiteSuperior):
     print("Hay convergecnia en el intervalo seleccionado!!")
     funcionDespejada = input("Digite la funcion despejada");
     ep = 100;
     sita = 0.1;
     global evaluado;
     evaluado.append(Variables(float(limiteInferior)));
     evaluado2 = list();
     evaluado2.append(1);
     x = symbols('x');
     cont = 1;
     global seguirLosPasos;
     while ep>= sita and cont<= 30:
        valor = sympify(funcionDespejada).subs({x:evaluado[len(evaluado)-1].valor});
        pase = verificarValorEnIntervalo(valor,limiteInferior,limiteSuperior);
        if(pase):
           evaluado.append(Variables(valor));
        else:
             seguirLosPasos = False;
             print("Has escogido un mal despeje para la funcion y por eso el valor se ha salido de los limites")
             break  
        if(cont>=2):
            ep = abs((evaluado[len(evaluado)-1].valor - evaluado[len(evaluado)-2].valor)/evaluado[len(evaluado)-1].valor)*100;
            evaluado[len(evaluado)-1].setEp(ep);
        cont += 1;  
     del evaluado[0];
     return funcionDespejada if seguirLosPasos else False;

def corregirEvaluado(evaluado,contenido):
   evaluado[contenido:];
   print("Hubo una correcion y ahora la lista se modifico y quedo así")

def executeFinish(evaluado):
   print("Hay convergencia en todos los intervalos");
   for e in evaluado:print(e.print());
  
funcion = input("Digite la funcion");
evaluado = list();
limiteInferior = float(input("Digite el limite inferior en decimales"));
limiteSuperior = float(input("Digite el limite Superior en decimales"));
intervalo = buscarIntervalo(limiteInferior,limiteSuperior);
pase = verificarConvergencia(funcion,intervalo);
if(pase):
   seguirLosPasos = True;
   funcionDespejada = calcularValor(limiteInferior,limiteSuperior);
   if(funcionDespejada):
      contenido = iterarDespeje(funcionDespejada,intervalo);
      valor = corregirEvaluado(evaluado,contenido) if contenido else executeFinish(evaluado);
else:print("No hay convergencia !!!!")



