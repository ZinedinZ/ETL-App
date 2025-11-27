import pandas as pd
import numpy as np
import datetime as dt


class Etl:
    def __init__(self):
        self.data = None

    def extract_file(self, path):
        data = pd.read_excel(path)
        self.data = data
        return data

    def time_editor(self, data):
        data["Sale_date"] = pd.to_datetime(data["Sale_date"], dayfirst=True, format="mixed")
        data["Sale_date"] = data["Sale_date"].dt.strftime("%d/%m/%y")
        print(data)

    def Missing_data(self, dataframe):
        pass


