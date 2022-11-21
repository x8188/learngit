'''
Autor: Sakurag1_LSJ
LastEditors: Sakurag1_LSJ
'''
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
model_src = 'NCNR_CG20220312095846'



onehot_dict = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1], 'N': [0, 0, 0, 0]}



def one_hot_encoding(seq):
    one_hot_encoded = np.zeros(shape=(len(seq) + len(seq[0]) - 1, 4))
    for i, nt in enumerate(seq[0]):
        one_hot_encoded[i, :] = onehot_dict[nt]

    for i, nt in enumerate(seq[1:]):
        one_hot_encoded[i+1000, :] = 4*[float(nt)]

    return one_hot_encoded

LMR_onehot = np.array([one_hot_encoding(seq) for seq in LMR_seq], dtype=np.float32)





#DeepLIfT

from collections import OrderedDict
import deeplift
from deeplift.conversion import kerasapi_conversion as kc
from deeplift.util import compile_func
from keras.models import load_model
import pandas as pd
import numpy as np
import tensorflow as tf
from vizsequence.viz_sequence import plot_weights, dna_plot_weights
from deeplift.util import get_hypothetical_contribs_func_onehot

from deeplift.util import get_shuffle_seq_ref_function
from deeplift.dinuc_shuffle import dinuc_shuffle #function to do a dinucleotide shuffle

from deeplift.util import get_shuffle_seq_ref_function
from deeplift.dinuc_shuffle import dinuc_shuffle #function to do a dinucleotide shuffle


import deeplift.conversion.kerasapi_conversion as kc


deeplift_model = kc.convert_model_from_saved_files(
        model_src,
        nonlinear_mxts_mode=deeplift.layers.NonlinearMxtsMode.DeepLIFT_GenomicsDefault)


print(deeplift_model.get_name_to_layer().keys())

find_scores_layer_idx = 1

deeplift_contribs_func = deeplift_model.get_target_contribs_func(
    find_scores_layer_name="input_1_0",
    pre_activation_target_layer_name="dense_2_0")




contribs_many_refs_func = get_shuffle_seq_ref_function(
    #score_computation_function is the original function to compute scores
    score_computation_function=deeplift_contribs_func,
    #shuffle_func is the function that shuffles the sequence
    #On real genomic data, a dinuc shuffle is advisable due to
    #the strong bias against CG dinucleotides
    shuffle_func=dinuc_shuffle)


#HyperContribScores


from deeplift.util import get_hypothetical_contribs_func_onehot

multipliers_func = deeplift_model.get_target_multipliers_func(find_scores_layer_name="input_1_0",
    pre_activation_target_layer_name="dense_2_0")
hypothetical_contribs_func = get_hypothetical_contribs_func_onehot(multipliers_func)



#Once again, we rely on multiple shuffled references
hypothetical_contribs_many_refs_func = get_shuffle_seq_ref_function(
    score_computation_function=hypothetical_contribs_func,
    shuffle_func=dinuc_shuffle)

num_refs_per_seq = 10
task_to_contrib_scores = {}
task_to_hyp_contrib_scores = {}
all_tasks = [1]
for task_idx in all_tasks:
    print("On task",task_idx)
    task_to_contrib_scores[task_idx] =\
        np.sum(contribs_many_refs_func(
            task_idx=task_idx,
            input_data_sequences=LMR_onehot,
            num_refs_per_seq=num_refs_per_seq,
            batch_size=100,
            progress_update=4000,
        ),axis=2)[:,:,None]*LMR_onehot
    task_to_hyp_contrib_scores[task_idx] =\
        hypothetical_contribs_many_refs_func(
            task_idx=task_idx,
            input_data_sequences=LMR_onehot,
            num_refs_per_seq=num_refs_per_seq,
            batch_size=100,
            progress_update=4000,
        )



import csv

a = []
for i in range(1,1032):
  a.append(i)
print(a)

if(flag==1):
    with open("00_NCNR_CG_Contrib.csv","w") as csvfile: 
        writer = csv.writer(csvfile)
        #先写入columns_name
        writer.writerow(a)
        #写入多行用writerows
        for i,data in enumerate(task_to_contrib_scores[1]):
            writer.writerow([LMR_Index[i]])
            writer.writerows(data.T)

    simple_upload('%s.suffix'%taskID,"00_NCNR_CG_Contrib.csv")

    os.remove("00_NCNR_CG_Contrib.csv")

    with open("00_NCNR_CG_HyperContrib.csv","w") as csvfile: 
        writer = csv.writer(csvfile)
        #先写入columns_name
        writer.writerow(a)
        #写入多行用writerows
        for i,data in enumerate(task_to_hyp_contrib_scores[1]):
            writer.writerow([LMR_Index[i]])
            writer.writerows(data.T)

    simple_upload('%s.suffix'%taskID,"00_NCNR_CG_HyperContrib.csv")

    os.remove("00_NCNR_CG_HyperContrib.csv")
else:
    with open("00_NCNR_CG_Contrib.csv","w") as csvfile: 
        writer = csv.writer(csvfile)
        #先写入columns_name
        writer.writerow(a)
        #写入多行用writerows
        for i,data in enumerate(task_to_contrib_scores[1]):
            writer.writerows(data.T)

    simple_upload('%s.suffix'%taskID,"00_NCNR_CG_Contrib.csv")

    os.remove("00_NCNR_CG_Contrib.csv")

    with open("00_NCNR_CG_HyperContrib.csv","w") as csvfile: 
        writer = csv.writer(csvfile)
        #先写入columns_name
        writer.writerow(a)
        #写入多行用writerows
        for i,data in enumerate(task_to_hyp_contrib_scores[1]):
            writer.writerows(data.T)

    simple_upload('%s.suffix'%taskID,"00_NCNR_CG_HyperContrib.csv")

    os.remove("00_NCNR_CG_HyperContrib.csv")