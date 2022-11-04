"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, size=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Calculo Parameters',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32, np.float32, np.float32, np.float32, np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.size = size

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        average = 0
        sqaverage = 0
        rms = 0
        desvest = 0
        N = len(input_items[0])
        for vectorIndex in range(N):
        	average += input_items[0][vectorIndex]
        	sqaverage += (input_items[0][vectorIndex])**2
        	rms += abs(input_items[0][vectorIndex])**2
        output_items[0][:] = N
        output_items[1][:] = sqaverage/N
        output_items[2][:] = np.sqrt(rms/N)
        output_items[3][:] = rms/N
        for vectorIndex in range(N):
        	desvest += (input_items[0][vectorIndex]-average/N)**2
        output_items[4][:] = np.sqrt(desvest/N)
        return len(output_items)
