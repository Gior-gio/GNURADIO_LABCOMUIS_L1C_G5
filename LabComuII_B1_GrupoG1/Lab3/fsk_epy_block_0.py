import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a RF VCO and works as following: Este bloque recibe como entrada
    los paquetes de bits (datos) y una variable que representa la fase Q de la señal 
    modulada. Tambièn tiene como paràmetros la frecuencia de la portadora y la frecuencia
    de muestreo. 
    Primero identifica el tamaño del paquete para generar un vector de muestras, a partir
    del cual se hace la modulaciòn multiplicando la entrada A por un oscilador que 
    representa una portadora que tiene los paràmetros antes mencionados."""

    def __init__(self, fc=128000, samp_rate=320000):  
        gr.sync_block.__init__(
            self,
            name='e_RF_VCO_ff',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32]
        )
        self.fc = fc
        self.samp_rate = samp_rate
        self.n_m=0

    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        n=np.linspace(self.n_m,self.n_m+N-1,N)
        self.n_m += N
        y[:]=A*np.cos(2*math.pi*self.fc*n/self.samp_rate+Q)
        return len(output_items[0])


