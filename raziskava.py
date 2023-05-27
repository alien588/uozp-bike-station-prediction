import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import csv

def load_data(dt):
    df = pd.read_csv(dt+".csv")

    return df


meta_data = load_data("./podatki/bicikelj_metadata")

data_train = load_data("./podatki/bicikelj_train")
data_test = load_data("./podatki/bicikelj_test")

#print(meta_data)
print(data_train)
print(data_test)

missing_train_data = data_train.isnull().sum()
print(str(missing_train_data.sum()) + " Toliko je manjkajocih vrednosti v podatkih za ucenje.")


povp_temp = []
obl = []
vol_padavin = []
dez = []

vreme_podatki = pd.read_csv('./podatki/povp_temp_obl_dez_lj.txt')
print(vreme_podatki)




