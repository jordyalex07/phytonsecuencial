import os

pies = float (input ('Ingresa el valor de pies: '))
pulgadas=pies*12
yardas=pies/3
cm=pulgadas*2.54
metros=cm/100
print ('Valor de cm: ' + repr (cm))
print ('Valor de metros: ' + repr (metros))
print ('Valor de pulgadas: ' + repr (pulgadas))
print ('Valor de yardas: ' + repr (yardas))
print ()
os.system ('pause')