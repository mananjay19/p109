import pandas as pd
import csv
import statistics

df = pd.read_csv('StudentsPerformance.csv')
datalist = df ['reading score'].tolist()

datamean=statistics.mean(datalist)

datamedian=statistics.median(datalist)

datamode=statistics.mode(datalist)

datastd=statistics.stdev(datalist)

print('mean,meadian,mode,stdev for reading score are',datamean,datamedian,datamode,datastd)

data_first_std_start,data_first_std_end = datamean - datastd, datamean + datastd
data_second_std_start,data_second_std_end = datamean - datastd*2, datamean + datastd*2
data_third_std_start,data_third_std_end = datamean - datastd*3, datamean + datastd*3
datalistofdatawithinfirststd = [result for result in datalist if result > data_first_std_start and result < data_first_std_end]
datalistofdatawithinsecondstd = [result for result in datalist if result > data_second_std_start and result < data_second_std_end]
datalistofdatawithinthirdstd = [result for result in datalist if result > data_third_std_start and result < data_third_std_end]
print('{} % of data for reading score lies within first std range'.format(len(datalistofdatawithinfirststd)*100.0/len(datalist)))
print('{} % of data for reading score lies within second std range'.format(len(datalistofdatawithinsecondstd)*100.0/len(datalist)))
print('{} % of data for reading score lies within third std range'.format(len(datalistofdatawithinthirdstd)*100.0/len(datalist)))
