#!/usr/bin/env python

# Level 3

import pylab as pyl
import numpy as np
import matplotlib.pyplot as pp
import scipy as scp
import scipy.ndimage as ni

import copy
import pickle
import optparse
import string
from collections import Counter
import os
import re
import unittest

class Problem:
    def __init__(self, level_num, input_str):
        self.level_num = level_num
        self.input_str = input_str
         
    def apply_rule(self, param):
        # Params
        ltr_fwd_back = param
	str_len = len(self.input_str)
        ans = ''

        # Body
	pattern = r'\b[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]\b'
	for i in range(ltr_fwd_back+1,str_len-ltr_fwd_back-1):
	    str_temp = self.input_str[i-ltr_fwd_back-1:i+ltr_fwd_back+2] 
            d = re.match(pattern, str_temp)
            if d is not None:
                ans = ans + d.group(0)[4]
        return ans
            
    def gen_output(self, param):
        output = self.apply_rule(param)  
        return output
        
    
######################################################################################################

if __name__ == '__main__':

    
    filename = "equality.txt"
    sub_dir = "./data/"
    f = open(os.path.join(sub_dir, filename))
    inp_string = f.read()
    
    level_no = 3
    fwd_back = 3
        
    level = Problem(level_no, inp_string)
    solution = level.gen_output(fwd_back)        
        
    print "The solution to Level ", level_no, " is:", solution
        
