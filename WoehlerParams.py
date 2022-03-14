
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


class WoehlerCurve:
    
    def __init__(self, S, N, outcome, infin_only=False, param_fix={}, param_estim={}):
        '''
        The file was provided by Kolyshkin and modified by Mordeja and contains the Maxium-Likelihood estimation for at 4-P model with k_2 = inifinity.
        The file has been censored.
        '''
        self.data ={'loads': np.array(S,np.float64), 'cycles': np.array(N,np.float64), 'outcome': np.array(outcome)}
        #where the result is stored in the end: self.Mali_4p_result
         
@jit(nopython=True, cache=True)
def mali_sum_lolli(SD, TS, k, N_E, fractures, alldata, alldata_outcome):
    """
    Produces the likelihood functions that are needed to compute the parameters of the woehler curve.
    """
    