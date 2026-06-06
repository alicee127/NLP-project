from transformers import pipeline

class LLMWrapper():

    def __init__(self, model_name: str):
        self.model_name = model_name
        self.pipe = None

    def load(self):
        self.pipe = pipeline('text-generation', model= self.model_name)

    def generate(self, prompt: str) -> str:
        message = [{'role': 'user', 'content': prompt}]
        output = self.pipe(message, max_new_tokens = 50, max_length = None, temperature = 0.1, do_sample = True)

        return output[0]['generated_text'][-1]['content']
    
    def generate_batch(self, prompts: str) -> list[str]:

        answers = []

        for prompt in prompts:
            answer = self.generate(prompt)
            
            answers.append(answer)
        

        return answers
        


    


    