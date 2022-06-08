import numpy as np

class Serie:

    def getSerie(self, numero):
        a = 0;
        b = 0;
        tmp = 0;
        serie = []

        if numero > 0:
            serie.append(0);
        else:
            return serie.append(0);

        b = 1

        for i in range(numero - 1):
            tmp = a + b;
            a = b;
            b = tmp;

            serie.append(a)

        return serie;

        

