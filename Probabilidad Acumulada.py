import pylab
import random
import numpy as np

sampleSize = 500


## Let's simulate the repeated throwing of a single six-sided die
singleDie = []
for i in range(sampleSize):
    newValue = random.randint(1,6)
    singleDie.append(newValue)

print ("Resultados de tirar un dado", sampleSize, "veces.")
print ("Media del tamaño de la muestra =", pylab.mean(singleDie))
print ("Mediana del tamaño de la muestra =", pylab.median(singleDie))
print ("Desviación estándar de la muestra =", pylab.std(singleDie))

pylab.hist(singleDie, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5])
pylab.xlabel('Valor')
pylab.ylabel('Cuenta')
#pylab.savefig('singleDie.png')
pylab.show()

## What about repeatedly throwing two dice and summing them?
twoDice = []
for i in range(sampleSize):
    newValue = random.randint(1,6) + random.randint(1,6)
    twoDice.append(newValue)

print ("Resultados de tirar dos dados", sampleSize, "times.")
print ("Media del tamaño de la muestra =", pylab.mean(twoDice))
print ("Mediana del tamaño de la muestra =", pylab.median(twoDice))

pylab.hist(twoDice, bins= pylab.arange(1.5,12.6,1.0))
pylab.xlabel('Valor')
pylab.ylabel('Cuenta')
#pylab.savefig('twoDice.png')
pylab.show()

pylab.hist(twoDice, bins=pylab.arange(1.5,12.6,1.0), normed=1, histtype='step', cumulative=True)
pylab.xlabel('Valor')
pylab.ylabel('Fraccion')
pylab.show()
