import pandas as pd
import json

class BLEnDDataset():
    def __init__(self, countries: list):
        self.countries = countries
        self.data = {}

    def _load_country(self, country: str, ann_dir: str):
        with open(f'{ann_dir}/{country}_data.json', 'r', encoding='utf-8') as file:
            raw_data = json.load(file)
        
        rows = []

        for question_id, content in raw_data.items():
            row = {
                'question_id': question_id,
                'local_question': content['question'],
                'en_question': content['en_question'],
                'local_answer_valid': [a for ann in content['annotations'] for a in ann['answers']],
                'en_answer_valid': [a for ann in content['annotations'] for a in ann['en_answers']],
                'country': country
            }
            rows.append(row)

        df = pd.DataFrame(rows)           

        return df
    
    def load(self, ann_dir: str):
        for country in self.countries:
            self.data[country] = self._load_country(country, ann_dir)

        return self.data
    
    def get_country_data(self, country: str) -> pd.DataFrame:
        return self.data[country]
