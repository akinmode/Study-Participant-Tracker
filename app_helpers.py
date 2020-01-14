"""
    Namespace: Follow Series Generator
"""
import datetime as dt
class GenerateFollowUpSeries(object):
    """Generates the follow up dates as a list of timedates"""
    def __init__(self, baseline):
        self.baseline = dt.datetime.strptime(baseline, '%Y-%m-%d')

    def gen24HrsRecallSeries(self):
        series_24 = {}
        series_24['Baseline_1'] = self.baseline.strftime("%A, %B %d, %Y.")
        series_24['Baseline_2'] = (self.baseline+dt.timedelta(7)).strftime("%A, %B %d, %Y.")
        series_24['Six_months_1'] = (self.baseline+dt.timedelta(209)).strftime("%A, %B %d, %Y.")
        series_24['Six_months_2'] = (self.baseline+dt.timedelta(216)).strftime("%A, %B %d, %Y.")
        series_24['Twelve_months_1'] = (self.baseline+dt.timedelta(365)).strftime("%A, %B %d, %Y.")
        series_24['Twelve_months_2'] = (self.baseline+dt.timedelta(372)).strftime("%A, %B %d, %Y.")
        series_24['Eighteen_months_1'] = (self.baseline+dt.timedelta(545)).strftime("%A, %B %d, %Y.")
        series_24['Eighteen_months_2'] = (self.baseline+dt.timedelta(552)).strftime("%A, %B %d, %Y.")
        return series_24

    def gen24HrsRecallAlerts(self):
        alerts_24 = [[i, dt.datetime.now() - i] for i in self.gen24HrsRecallSeries()]
        return alerts_24
"""
    Namespace: Generate New Id
"""
class ValId(object):
    def new_id(ffq_id):
        """ Generate new identification """
        return "VAL_"+list(ffq_id)[-3]+""+list(ffq_id)[-2]+""+list(ffq_id)[-1]
"""
    Namespace: Summary Generator
"""
import pandas as pd
class ProcessSummary(object):
    """Generates Summary from database"""

    def __init__(self, data):
        self.data = pd.DataFrame(data, columns=['ID', 'Date Entered', 'pffqID', 'p24ID', 'Names', 'Sex', 'Tribe', 'Age', 'pum1', 'pum2', 'Ses'])

    def summaryALS(self):
        summaryData = pd.DataFrame({"count": self.data.groupby(['Age', 'Tribe', 'Sex']).size()})
        dict_Data = summaryData.to_dict('index')
        sData = {
            ('21-30', 'Hausa', 'Male'): {'count': 0},
            ('21-30', 'Hausa', 'Female'): {'count': 0},
            ('21-30', 'Igbo', 'Male'): {'count': 0},
            ('21-30', 'Igbo', 'Female'): {'count': 0},
            ('21-30', 'Yoruba', 'Male'): {'count': 0},
            ('21-30', 'Yoruba', 'Female'): {'count': 0},
            ('31-40', 'Hausa', 'Male'): {'count': 0},
            ('31-40', 'Hausa', 'Female'): {'count': 0},
            ('31-40', 'Igbo', 'Male'): {'count': 0},
            ('31-40', 'Igbo', 'Female'): {'count': 0},
            ('31-40', 'Yoruba', 'Male'): {'count': 0},
            ('31-40', 'Yoruba', 'Female'): {'count': 0},
            ('41-50', 'Hausa', 'Male'): {'count': 0},
            ('41-50', 'Hausa', 'Female'): {'count': 0},
            ('41-50', 'Igbo', 'Male'): {'count': 0},
            ('41-50', 'Igbo', 'Female'): {'count': 0},
            ('41-50', 'Yoruba', 'Male'): {'count': 0},
            ('41-50', 'Yoruba', 'Female'): {'count': 0},
            ('51-60', 'Hausa', 'Male'): {'count': 0},
            ('51-60', 'Hausa', 'Female'): {'count': 0},
            ('51-60', 'Igbo', 'Male'): {'count': 0},
            ('51-60', 'Igbo', 'Female'): {'count': 0},
            ('51-60', 'Yoruba', 'Male'): {'count': 0},
            ('51-60', 'Yoruba', 'Female'): {'count': 0},
            ('Above 60', 'Hausa', 'Male'): {'count': 0},
            ('Above 60', 'Hausa', 'Female'): {'count': 0},
            ('Above 60', 'Igbo', 'Male'): {'count': 0},
            ('Above 60', 'Igbo', 'Female'): {'count': 0},
            ('Above 60', 'Yoruba', 'Male'): {'count': 0},
            ('Above 60', 'Yoruba', 'Female'): {'count': 0}
        }
        for k,v in sData.items():
            if k in dict_Data.keys():
                sData[k] = dict_Data[k]
        return sData

    def summarySALS(self):
        summaryData = pd.DataFrame({"count": self.data.groupby(['Ses', 'Age', 'Tribe', 'Sex']).size()})
        dict_Data = summaryData.to_dict('index')
        sData = {
            ('Low', '21-30', 'Hausa', 'Male'): {'count': 0},
            ('Low', '21-30', 'Hausa', 'Female'): {'count': 0},
            ('Low', '21-30', 'Igbo', 'Male'): {'count': 0},
            ('Low', '21-30', 'Igbo', 'Female'): {'count': 0},
            ('Low', '21-30', 'Yoruba', 'Male'): {'count': 0},
            ('Low', '21-30', 'Yoruba', 'Female'): {'count': 0},
            ('Low', '31-40', 'Hausa', 'Male'): {'count': 0},
            ('Low', '31-40', 'Hausa', 'Female'): {'count': 0},
            ('Low', '31-40', 'Igbo', 'Male'): {'count': 0},
            ('Low', '31-40', 'Igbo', 'Female'): {'count': 0},
            ('Low', '31-40', 'Yoruba', 'Male'): {'count': 0},
            ('Low', '31-40', 'Yoruba', 'Female'): {'count': 0},
            ('Low', '41-50', 'Hausa', 'Male'): {'count': 0},
            ('Low', '41-50', 'Hausa', 'Female'): {'count': 0},
            ('Low', '41-50', 'Igbo', 'Male'): {'count': 0},
            ('Low', '41-50', 'Igbo', 'Female'): {'count': 0},
            ('Low', '41-50', 'Yoruba', 'Male'): {'count': 0},
            ('Low', '41-50', 'Yoruba', 'Female'): {'count': 0},
            ('Low', '51-60', 'Hausa', 'Male'): {'count': 0},
            ('Low', '51-60', 'Hausa', 'Female'): {'count': 0},
            ('Low', '51-60', 'Igbo', 'Male'): {'count': 0},
            ('Low', '51-60', 'Igbo', 'Female'): {'count': 0},
            ('Low', '51-60', 'Yoruba', 'Male'): {'count': 0},
            ('Low', '51-60', 'Yoruba', 'Female'): {'count': 0},
            ('Low', 'Above 60', 'Hausa', 'Male'): {'count': 0},
            ('Low', 'Above 60', 'Hausa', 'Female'): {'count': 0},
            ('Low', 'Above 60', 'Igbo', 'Male'): {'count': 0},
            ('Low', 'Above 60', 'Igbo', 'Female'): {'count': 0},
            ('Low', 'Above 60', 'Yoruba', 'Male'): {'count': 0},
            ('Low', 'Above 60', 'Yoruba', 'Female'): {'count': 0},
            ('LowMI', '21-30', 'Hausa', 'Male'): {'count': 0},
            ('LowMI', '21-30', 'Hausa', 'Female'): {'count': 0},
            ('LowMI', '21-30', 'Igbo', 'Male'): {'count': 0},
            ('LowMI', '21-30', 'Igbo', 'Female'): {'count': 0},
            ('LowMI', '21-30', 'Yoruba', 'Male'): {'count': 0},
            ('LowMI', '21-30', 'Yoruba', 'Female'): {'count': 0},
            ('LowMI', '31-40', 'Hausa', 'Male'): {'count': 0},
            ('LowMI', '31-40', 'Hausa', 'Female'): {'count': 0},
            ('LowMI', '31-40', 'Igbo', 'Male'): {'count': 0},
            ('LowMI', '31-40', 'Igbo', 'Female'): {'count': 0},
            ('LowMI', '31-40', 'Yoruba', 'Male'): {'count': 0},
            ('LowMI', '31-40', 'Yoruba', 'Female'): {'count': 0},
            ('LowMI', '41-50', 'Hausa', 'Male'): {'count': 0},
            ('LowMI', '41-50', 'Hausa', 'Female'): {'count': 0},
            ('LowMI', '41-50', 'Igbo', 'Male'): {'count': 0},
            ('LowMI', '41-50', 'Igbo', 'Female'): {'count': 0},
            ('LowMI', '41-50', 'Yoruba', 'Male'): {'count': 0},
            ('LowMI', '41-50', 'Yoruba', 'Female'): {'count': 0},
            ('LowMI', '51-60', 'Hausa', 'Male'): {'count': 0},
            ('LowMI', '51-60', 'Hausa', 'Female'): {'count': 0},
            ('LowMI', '51-60', 'Igbo', 'Male'): {'count': 0},
            ('LowMI', '51-60', 'Igbo', 'Female'): {'count': 0},
            ('LowMI', '51-60', 'Yoruba', 'Male'): {'count': 0},
            ('LowMI', '51-60', 'Yoruba', 'Female'): {'count': 0},
            ('LowMI', 'Above 60', 'Hausa', 'Male'): {'count': 0},
            ('LowMI', 'Above 60', 'Hausa', 'Female'): {'count': 0},
            ('LowMI', 'Above 60', 'Igbo', 'Male'): {'count': 0},
            ('LowMI', 'Above 60', 'Igbo', 'Female'): {'count': 0},
            ('LowMI', 'Above 60', 'Yoruba', 'Male'): {'count': 0},
            ('LowMI', 'Above 60', 'Yoruba', 'Female'): {'count': 0},
            ('HighMI', '21-30', 'Hausa', 'Male'): {'count': 0},
            ('HighMI', '21-30', 'Hausa', 'Female'): {'count': 0},
            ('HighMI', '21-30', 'Igbo', 'Male'): {'count': 0},
            ('HighMI', '21-30', 'Igbo', 'Female'): {'count': 0},
            ('HighMI', '21-30', 'Yoruba', 'Male'): {'count': 0},
            ('HighMI', '21-30', 'Yoruba', 'Female'): {'count': 0},
            ('HighMI', '31-40', 'Hausa', 'Male'): {'count': 0},
            ('HighMI', '31-40', 'Hausa', 'Female'): {'count': 0},
            ('HighMI', '31-40', 'Igbo', 'Male'): {'count': 0},
            ('HighMI', '31-40', 'Igbo', 'Female'): {'count': 0},
            ('HighMI', '31-40', 'Yoruba', 'Male'): {'count': 0},
            ('HighMI', '31-40', 'Yoruba', 'Female'): {'count': 0},
            ('HighMI', '41-50', 'Hausa', 'Male'): {'count': 0},
            ('HighMI', '41-50', 'Hausa', 'Female'): {'count': 0},
            ('HighMI', '41-50', 'Igbo', 'Male'): {'count': 0},
            ('HighMI', '41-50', 'Igbo', 'Female'): {'count': 0},
            ('HighMI', '41-50', 'Yoruba', 'Male'): {'count': 0},
            ('HighMI', '41-50', 'Yoruba', 'Female'): {'count': 0},
            ('HighMI', '51-60', 'Hausa', 'Male'): {'count': 0},
            ('HighMI', '51-60', 'Hausa', 'Female'): {'count': 0},
            ('HighMI', '51-60', 'Igbo', 'Male'): {'count': 0},
            ('HighMI', '51-60', 'Igbo', 'Female'): {'count': 0},
            ('HighMI', '51-60', 'Yoruba', 'Male'): {'count': 0},
            ('HighMI', '51-60', 'Yoruba', 'Female'): {'count': 0},
            ('HighMI', 'Above 60', 'Hausa', 'Male'): {'count': 0},
            ('HighMI', 'Above 60', 'Hausa', 'Female'): {'count': 0},
            ('HighMI', 'Above 60', 'Igbo', 'Male'): {'count': 0},
            ('HighMI', 'Above 60', 'Igbo', 'Female'): {'count': 0},
            ('HighMI', 'Above 60', 'Yoruba', 'Male'): {'count': 0},
            ('HighMI', 'Above 60', 'Yoruba', 'Female'): {'count': 0},
            ('High', '21-30', 'Hausa', 'Male'): {'count': 0},
            ('High', '21-30', 'Hausa', 'Female'): {'count': 0},
            ('High', '21-30', 'Igbo', 'Male'): {'count': 0},
            ('High', '21-30', 'Igbo', 'Female'): {'count': 0},
            ('High', '21-30', 'Yoruba', 'Male'): {'count': 0},
            ('High', '21-30', 'Yoruba', 'Female'): {'count': 0},
            ('High', '31-40', 'Hausa', 'Male'): {'count': 0},
            ('High', '31-40', 'Hausa', 'Female'): {'count': 0},
            ('High', '31-40', 'Igbo', 'Male'): {'count': 0},
            ('High', '31-40', 'Igbo', 'Female'): {'count': 0},
            ('High', '31-40', 'Yoruba', 'Male'): {'count': 0},
            ('High', '31-40', 'Yoruba', 'Female'): {'count': 0},
            ('High', '41-50', 'Hausa', 'Male'): {'count': 0},
            ('High', '41-50', 'Hausa', 'Female'): {'count': 0},
            ('High', '41-50', 'Igbo', 'Male'): {'count': 0},
            ('High', '41-50', 'Igbo', 'Female'): {'count': 0},
            ('High', '41-50', 'Yoruba', 'Male'): {'count': 0},
            ('High', '41-50', 'Yoruba', 'Female'): {'count': 0},
            ('High', '51-60', 'Hausa', 'Male'): {'count': 0},
            ('High', '51-60', 'Hausa', 'Female'): {'count': 0},
            ('High', '51-60', 'Igbo', 'Male'): {'count': 0},
            ('High', '51-60', 'Igbo', 'Female'): {'count': 0},
            ('High', '51-60', 'Yoruba', 'Male'): {'count': 0},
            ('High', '51-60', 'Yoruba', 'Female'): {'count': 0},
            ('High', 'Above 60', 'Hausa', 'Male'): {'count': 0},
            ('High', 'Above 60', 'Hausa', 'Female'): {'count': 0},
            ('High', 'Above 60', 'Igbo', 'Male'): {'count': 0},
            ('High', 'Above 60', 'Igbo', 'Female'): {'count': 0},
            ('High', 'Above 60', 'Yoruba', 'Male'): {'count': 0},
            ('High', 'Above 60', 'Yoruba', 'Female'): {'count': 0}
        }
        for k,v in sData.items():
            if k in dict_Data.keys():
                sData[k] = dict_Data[k]
        return sData
