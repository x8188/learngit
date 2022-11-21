'''
Autor: Sakurag1_LSJ
LastEditors: Sakurag1_LSJ
'''
from utils.cos_utils import content_upload
import os

# 传入的可能是文件地址，也可能是序列，判断是否为文件
# 输入由两部分组成 taskID;(seq|file_path) 使用;连接
s = input()
taskID,seqOrFile = s.split(';')
if os.path.exists(seqOrFile):
    flag = 1
    pass
else: 
    flag = 0;


# do something
import keras
from tensorflow.keras.models import load_model
import random

import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import metrics


OTHER_INFO = ['Tissue__Leaf','Tissue__Root', 'Tissue__Tassel', 'ATAC__atac', 'Genic__3UTR',
 'Genic__5UTR' ,'Genic__DOWN5K' ,'Genic__EXON' ,'Genic__GENE' ,'Genic__MRNA',
 'Genic__UP5K' ,'TE__CACTA_TIR_transposon' ,'TE__centromeric_repeat',
 'TE__Copia_LTR_retrotransposon' ,'TE__Gypsy_LTR_retrotransposon',
 'TE__hAT_TIR_transposon', 'TE__helitron' ,'TE__knob',
 'TE__L1_LINE_retrotransposon' ,'TE__LINE_element',
 'TE__long_terminal_repeat' ,'TE__low_complexity' ,'TE__LTR_retrotransposon',
 'TE__Mutator_TIR_transposon' ,'TE__PIF_Harbinger_TIR_transposon',
 'TE__rDNA_intergenic_spacer_element', 'TE__repeat_region',
 'TE__RTE_LINE_retrotransposon', 'TE__subtelomere',
 'TE__target_site_duplication', 'TE__Tc1_Mariner_TIR_transposon']


LMR_seq = [];HMR_seq = []
LMR_Id = [];HMR_Id = []

if (flag==1):
    data = pd.read_csv(seqOrFile,sep='\t')
    data.set_index("SWID",inplace=True)
    data_index = data.index
    random.shuffle(data_index)
    columns = data.columns

    for index in data_index:
        seqs = []
        seqs.append(data.loc[index]['Seq'])
        for info in OTHER_INFO:
            if (info in columns):
                seqs.append(str(data.loc[index][info]))
            else:
                seqs.append(str(0))
        LMR_seq.append(seqs)
        LMR_Id.append(index)
else:
    for seq_data in seqOrFile:
        seqs = []
        seqs.append(seq_data)
        for info in OTHER_INFO:
            seqs.append(str(0))
        LMR_seq.append(seqs)


#load_model
print(tf.__version__)
model_src = 'NCNR_CG20220312095846'
keras_model = load_model(model_src)



onehot_dict = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1], 'N': [0, 0, 0, 0]}



def one_hot_encoding(seq):
    one_hot_encoded = np.zeros(shape=(len(seq) + len(seq[0]) - 1, 4))
    for i, nt in enumerate(seq[0]):
        one_hot_encoded[i, :] = onehot_dict[nt]

    for i, nt in enumerate(seq[1:]):
        one_hot_encoded[i+1000, :] = 4*[float(nt)]

    return one_hot_encoded

LMR_onehot = np.array([one_hot_encoding(seq) for seq in LMR_seq], dtype=np.float32)

#Prediction
if(flag==1):
    predictions = []
    LMR_predictions = keras_model.predict(LMR_onehot)
    for i in range(LMR_predictions.shape[0]):
        if(LMR_predictions[i][1] >= 0.5):
            predictions.append("LMR")
        else:
            predictions.append("HMR")
        LMR_Index.append(LMR_Id[i])

    dicts = {"ID":LMR_Index,"Prediction":predictions}

    dataframe = pd.DataFrame(dicts)
    dataframe.to_csv('00_NCNR_CG_Prediction.csv')

    simple_upload('%s.suffix'%taskID,"00_NCNR_CG_Prediction.csv")

    os.remove("00_NCNR_CG_Prediction.csv")
else:
    predictions = []
    LMR_predictions = keras_model.predict(LMR_onehot)
    for i in range(LMR_predictions.shape[0]):
        if(LMR_predictions[i][1] >= 0.5):
            predictions.append("LMR")
        else:
            predictions.append("HMR")

    dicts = {"Prediction":predictions}

    dataframe = pd.DataFrame(dicts)
    dataframe.to_csv('00_NCNR_CG_Prediction.csv')

    simple_upload('00_NCNR_CG_Prediction%s.suffix'%taskID,"00_NCNR_CG_Prediction.csv")

    os.remove("00_NCNR_CG_Prediction.csv")