import pandas as pd
import re

def _clean(text: str) -> str:
    clean_text = re.sub(r'[^\w\s]', '', text).lower().strip()
    return clean_text

class Scorer():

    def __init__(self, en_col: str = 'en_answer_valid', local_col : str = 'local_answer_valid'):
        self.en_col = en_col
        self.local_col = local_col

    def assign_score(self, valid_answers: list[str], output: str) -> int:
        return int(any(_clean(answer) in _clean(output) for answer in valid_answers))
    
    def scores_batch(self, df: pd.DataFrame):
        control_scores = []
        persona_scores = []
        language_scores = []

        for idx, row in df.iterrows():
            valid = row[self.en_col] + row[self.local_col]
            control_scores.append(self.assign_score(valid, row['control_output']))
            persona_scores.append(self.assign_score(valid, row['persona_output']))
            language_scores.append(self.assign_score(valid, row['language_output']))
        
        df['control_score'] = control_scores
        df['persona_score'] = persona_scores
        df['language_score'] = language_scores

        return df