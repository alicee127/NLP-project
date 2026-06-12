import pandas as pd
import numpy as np
from scipy import stats

class CausalEffectAnalyzer():
    
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def compute_cka(self, group: str) -> float:
        return self.df[f'{group}_score'].mean()
    
    def compute_tce(self, treatment: str) -> float:
        return self.compute_cka(treatment) - self.compute_cka('control')

    def t_tests(self, treatment: str, country: str):
        treatment_arr = self.df[f'{treatment}_score'].to_numpy()
        control_arr = self.df['control_score'].to_numpy()

        t_val, p_val = stats.ttest_ind(treatment_arr, control_arr, equal_var =False)

        alpha = 0.05

        significance = 'SIGNIFICANT STATISTICAL DIFFERENCE' if np.abs(p_val)<=alpha else 'NO SIGNIFICANT STATISTICAL DIFFERENCE'

        print(f'{country} | {treatment} | t = {t_val:.3f} | p = {p_val:.3f} | {significance}')


        return t_val, p_val