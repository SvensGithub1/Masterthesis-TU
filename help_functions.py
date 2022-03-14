# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:26:27 2021

@author: Sven Mordeja
"""
import numpy as np
import scipy.stats as stats
'''
In this script some helperfunctions are collected. Some functions are used in multiple scripts.

'''

#%% help functions
def calc_n(woehler_params, s):
    '''
    Calculates the number of cycles for a 50% failure probaility.

    Parameters
    ----------
    woehler_params : Dict
        A dictionary containing the four woehler parameter.
    s : Int
        The amlitude with 50% failure probaility at which n is calculated.

    Returns
    -------
    n : Int
        Number of cycles for a 50% failure probaility.

    '''
    k = woehler_params['k']
    s_d_50 = woehler_params['s_d']
    n_e     = woehler_params['n_e']
    one_t_s = woehler_params['one_t_s']
    n      = 10**(np.log10(n_e)+k*(np.log10(s_d_50)-np.log10(s)))
    return n
def calc_s_long(woehler_params, p):
    '''
    Calculates the amplitude for a runout probaility p.

    Parameters
    ----------
    woehler_params : Dict
        A dictionary containing the four woehler parameter.
    p : Int
        Runout probability.

    Returns
    -------
    s : Int
        The amlitude with a runout probaility p.

    '''
    k = woehler_params['k']
    s_d_50 = woehler_params['s_d']
    n_e     = woehler_params['n_e']
    one_t_s = woehler_params['one_t_s']
    factor_p = stats.norm.ppf(p)
    s_p = 1/(2.564)*factor_p*np.log10(one_t_s)
    s = 10**(s_p + np.log10(s_d_50))
    return s
    
def calc_s_short(woehler_params, n):
    '''
    Calculates the amplitude for a 50% failure probaility.

    Parameters
    ----------
    woehler_params : Dict
        A dictionary containing the four woehler parameter.
    n : Int
        Number of cycles for a 50% failure probaility.

    Returns
    -------
    s : Int
        The amlitude with 50% failure probaility.

    '''
    k = woehler_params['k']
    s_d_50 = woehler_params['s_d']
    n_e     = woehler_params['n_e']
    one_t_s = woehler_params['one_t_s']
    s= 10**(-1*((np.log10(n)-np.log10(n_e))/k-np.log10(s_d_50)))
    
    return s
def get_runout_and_failure(woehler_points):
    '''
    Returns the amplitudes and number of cycles of the runouts and the failures seperatly.

    Parameters
    ----------
    woehler_points : Dict
        A dictonary containing the measured data points. 
        (s_a, n, outcome)

    Returns
    -------
    s_a_failure : Array
        All failure amplitudes.
    n_failure : Array
        All failure amplitudes.
    s_a_runout : Array
        All runout amplitudes.
    n_runout : Array
        All runout amplitudes.

    '''
    s_a = woehler_points['s_a']
    n = woehler_points['n']
    outcome = woehler_points['outcome']
    
    n_failure = np.array([])
    n_runout = np.array([])
    s_a_failure = np.array([])
    s_a_runout = np.array([])
    for ii in range(len(outcome)):
           
        if outcome[ii] == 'failure':
            n_failure = np.append(n_failure, n[ii])
            s_a_failure = np.append(s_a_failure, s_a[ii])
            
        else:
            n_runout = np.append(n_runout, n[ii])
            s_a_runout = np.append(s_a_runout, s_a[ii])
    return s_a_failure, n_failure, s_a_runout, n_runout