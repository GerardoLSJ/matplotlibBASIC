import urllib.request
from time import time

timeArray=[]
i=0
def responseTime(urlToParse):
    t0 = time()
    partial=0;
    response = urllib.request.urlopen(urlToParse).read()
    partial= time()-t0
    print("Tiempo "+ format(partial) + " de: "+ urlToParse)
    timeArray.append(partial)
  

print("Function:")
responseTime("http://profesores.fi-b.unam.mx/carlos/eda1/fuerza_bruta.py")
responseTime("http://google.com")
responseTime("http://www.facebook.com/")
responseTime("http://www.unam.mx/")
responseTime("http://gadmaweb.com/")
responseTime("http://www.gigigo.com/app/es/home")

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [1,3,5,7,9,11]
y = timeArray

plt.bar(x, y, align='center')
plt.title('Response time')
plt.ylabel('Time')
plt.xlabel('Url')

plt.show()
