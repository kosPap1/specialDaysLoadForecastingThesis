# input and setting data tables
import pandas as pd
# change the path according to your local path in order to work
# Δεδομένα Φορτίου
load2012 = pd.read_excel('/home/konstantinospappas/PycharmProjects/Paradoteo_Case1/data/LoadData/load2012.xlsx', names=pd.date_range(start='1/1/2012', periods=366, freq='D'))
load2013 = pd.read_excel('/home/konstantinospappas/PycharmProjects/Paradoteo_Case1/data/LoadData/load2013.xlsx', names=pd.date_range(start='1/1/2013', periods=365, freq='D'))
load2014 = pd.read_excel('//home/konstantinospappas/PycharmProjects/Paradoteo_Case1/data/LoadData/load2014.xlsx', names=pd.date_range(start='1/1/2014', periods=365, freq='D'))
load2015 = pd.read_excel('/home/konstantinospappas/PycharmProjects/Paradoteo_Case1/data/LoadData/load2015.xlsx', names=pd.date_range(start='1/1/2015', periods=365, freq='D'))
load2016 = pd.read_excel('//home/konstantinospappas/PycharmProjects/Paradoteo_Case1/data/LoadData/load2016.xlsx', names=pd.date_range(start='1/1/2016', periods=366, freq='D'))
load2017 = pd.read_excel('/home/konstantinospappas/PycharmProjects/Paradoteo_Case1/data/LoadData/load2017.xlsx', names=pd.date_range(start='1/1/2017', periods=365, freq='D'))
load2018 = pd.read_excel('/home/konstantinospappas/PycharmProjects/Paradoteo_Case1/data/LoadData/load2018.xlsx', names=pd.date_range(start='1/1/2018', periods=365, freq='D'))
load2019 = pd.read_excel('/home/konstantinospappas/PycharmProjects/Paradoteo_Case1/data/LoadData/load2019.xlsx', names=pd.date_range(start='1/1/2019', periods=365, freq='D'))

# Δεδομένα θερμοκρασίας
temp2012 = pd.read_excel('/home/konstantinospappas/PycharmProjects/Paradoteo_Case1/data/temperatureData/temp2012.xlsx', names=pd.date_range(start='1/1/2012', periods=366, freq='D'))
temp2013 = pd.read_excel('/home/konstantinospappas/PycharmProjects/Paradoteo_Case1/data/temperatureData/temp2013.xlsx', names=pd.date_range(start='1/1/2013', periods=365, freq='D'))
temp2014 = pd.read_excel('/home/konstantinospappas/PycharmProjects/Paradoteo_Case1/data/temperatureData/temp2014.xlsx', names=pd.date_range(start='1/1/2014', periods=365, freq='D'))
temp2015 = pd.read_excel('/home/konstantinospappas/PycharmProjects/Paradoteo_Case1/data/temperatureData/temp2015.xlsx', names=pd.date_range(start='1/1/2015', periods=365, freq='D'))
temp2016 = pd.read_excel('/home/konstantinospappas/PycharmProjects/Paradoteo_Case1/data/temperatureData/temp2016.xlsx', names=pd.date_range(start='1/1/2016', periods=366, freq='D'))
temp2017 = pd.read_excel('/home/konstantinospappas/PycharmProjects/Paradoteo_Case1/data/temperatureData/temp2017.xlsx', names=pd.date_range(start='1/1/2017', periods=365, freq='D'))
temp2018 = pd.read_excel('/home/konstantinospappas/PycharmProjects/Paradoteo_Case1/data/temperatureData/temp2018.xlsx', names=pd.date_range(start='1/1/2018', periods=365, freq='D'))
temp2019 = pd.read_excel('/home/konstantinospappas/PycharmProjects/Paradoteo_Case1/data/temperatureData/temp2019.xlsx', names=pd.date_range(start='1/1/2019', periods=365, freq='D'))




