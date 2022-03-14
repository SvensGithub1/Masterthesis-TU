# The following file was modiefied from the file of Kolyshkin and fitted with a
# new Max-Likelihood methode by Mordeja.
#
# Copyright (c) 2019 - for information on the respective copyright owner
# see the NOTICE file and/or the repository
# https://github.com/boschresearch/pylife
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = "Mustapha Kassem"
__maintainer__ = "Anton Kolyshkin"

import numpy as np
import time
import pandas as pd
import numpy.ma as ma
from numba import jit
from numba_stats import norm
from multiprocessing import Process, freeze_support
from scipy import stats, optimize
import mystic as my


class WoehlerCurve2:
    
    def __init__(self, S, N, outcome, k_2 = 22, infin_only=False, param_fix={}, param_estim={}):
        '''
        The file was provided by Kolyshkin and modified by Mordeja and contains the Maxium-Likelihood estimation for at 4-P model with k_2 beeing specified.
        The formulas used can be found in champter 6.2 in the thesis'''
        self.data ={'loads': np.array(S,np.float64), 'cycles': np.array(N,np.float64), 'outcome': np.array(outcome)}
        #where the result is stored in the end: self.Mali_4p_result
         
def mali_sum_lolli(SD, TS, k, N_E, fractures, alldata, alldata_outcome, k_2):
    '''
    Produces the likelihood functions that are needed to compute the parameters of the woehler curve.

    Parameters
    ----------
    SD : Int
        Endurance Limit.
    TS : Int
        The scatter in load direction.
    k : Int
        The slope k_1.
    N_E : Int
        Load-cycle endurance.
    fractures : Array
        Array of all the fractures.
    alldata : Array
        Array of all data containing the n and s values.
    alldata_outcome : Array
        Array of all the outcomes.
    k_2 : Int
        The slope k_2.

    Returns
    -------
    neg_sum_lolli : Int
        Neg Sum of the log likelihoods.

    '''
   
    TN = TS ** (k)
    TN2 = TS **(k_2)
    Ls = np.array([])
    std_log = np.log10(TS)/2.5631031311
    for ii, outcome in enumerate(alldata_outcome):
        if outcome == 'failure':
            if alldata[0,ii] <= N_E:
                x = np.log10(alldata[0,ii] * ((alldata[1,ii]/SD)**(k)))
                Mu = np.log10(N_E)
                Sigma = np.log10(TS**k)/2.5631031311
                Li = norm.pdf(x, Mu, Sigma)
                
                if Li >= 1e-200:
                    Ls = np.append(Ls, Li)
            else:
                x = np.log10(alldata[0,ii] * ((alldata[1,ii]/SD)**(k_2)))
                Mu = np.log10(N_E)
                Sigma = np.log10(TS**k_2)/2.5631031311
                Li = norm.pdf(x, Mu, Sigma)
                if Li >= 1e-200:
                    Ls = np.append(Ls, Li)
            Li = norm.cdf(np.log10(alldata[1,ii]/SD), np.log10(1), std_log)  
            if Li >= 1e-200:
                Ls = np.append(Ls, Li)
        else:
            Li = 1 - norm.cdf(np.log10(alldata[1,ii]/SD), np.log10(1), std_log)  
            Ls = np.append(Ls, Li)
            
            x = np.log10(alldata[0,ii] * ((alldata[1,ii]/SD)**(k_2)))
            Mu = np.log10(N_E)
            Sigma = np.log10(TS**k_2)/2.5631031311
            Li = 1 - norm.cdf(x, Mu, Sigma) 
            if Li >= 1e-200:
                Ls = np.append(Ls, Li)
   
    LLs= np.log(Ls)

    sum_LLs = np.sum(LLs)
    
    neg_sum_lolli = -sum_LLs

    return neg_sum_lolli
