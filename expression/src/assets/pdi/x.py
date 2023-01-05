
import numpy as np
import pandas as pd
 
# path处填入npy文件具体路径
npfile = np.load("tp%Dm8-5125573-5135954%Zm00001d008316.npy")
# 将npy文件的数据格式转化为csv格式
np_to_csv = pd.DataFrame(data=npfile)
# 存入具体目录下的np_to_csv.csv 文件
np_to_csv.to_csv('tp%Dm8-5125573-5135954%Zm00001d008316.csv')


