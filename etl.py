import pandas as pd
import numpy as np


class Etl:
    def __init__(self):
        self.data = None

    def extract_file(self, path):
        data = pd.read_excel(path)
        self.data = data

    def time_editor(self):
        pass
