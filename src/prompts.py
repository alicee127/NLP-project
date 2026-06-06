import pandas as pd

class PromptBuilder():

    def __init__(self):
        self.persona_prefix = "As a person from"
        self.short_answer_question = "Provide a single answer without any explanations."

    def build_control_prompts(self, df: pd.DataFrame) -> list[str]:
        control_prompts = []

        for question in df['en_question'].tolist():
            prompt = f"{question} {self.short_answer_question}"
            
            control_prompts.append(prompt)

        return control_prompts
         
    def build_persona_prompts(self, df: pd.DataFrame) -> list[str]:
        persona_prompts = []

        country = df['country'].iloc[0]

        for question in df['en_question'].tolist():
            prompt = f"{self.persona_prefix} {country}, {question[0].lower() + question[1:]} {self.short_answer_question}"

            persona_prompts.append(prompt)

        return persona_prompts
    
    def build_language_prompts(self, df: pd.DataFrame) -> list[str]:
        language_prompts = []

        for question in df['local_question'].tolist():
            prompt = f"{question} {self.short_answer_question}"

            language_prompts.append(prompt)

        return language_prompts