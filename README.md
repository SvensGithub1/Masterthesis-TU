# Masterthesis
This repository contains code for experimental planning with Bayesian Modelling for Woehler Experiments. It should be viewed in context of the Masterthesis. 
A html style documentation can be accessed through: /html/index.html.
Some files had to be censored, in order to not release interlectual property of Bosch.

- An example on how to use the most importent functions is provided in "Example Plan Experiment" 
- An example on how to calculate the Maximum-Likelihood is provided in "Example 4-PML with variable k_2"
- The file "bays_model" contains the bayesian model.
- The file "doe" contains the experimental planning.
- The file "t" contains calculations for the spread (Streuspannne).
- The file "data_manager" contains the functions that interact with the databases.
- The file "plot_functions" contains functions for plotting.
- The file "WoehlerParams" has been coded to calculate the four-paramametric Maximum-Likelhood methode with modifications to speed up the calculations. In this file k_2 is assumed to be infinite. (censored)
- The file "WoehlerParamsModified" has been coded to calculate the four-paramametric Maximum-Likelhood methode with modifications to speed up the calculations. In this file k_2 has to be provided. More inforamtion on the likelihood function can be found in chapter 6.3 of the thesis. (censored)
- The file "help_functions" contains several functions, that are used in multiple scrits.
- The file "allData.csv" contains previously run experiments. (censored)
- The files "ml-prediction.csv" and "Pred.csv" contain KI predictions. (censored)
- The file masterthesis.yml contains the used packages for this masterthesis.
