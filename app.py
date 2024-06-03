import spacy
import json

class InferlessPythonModel:

    def initialize(self):
        model_id = "en_core_web_sm"  # Specify the model repository ID
        spacy.cli.download("en_core_web_sm")
        self.nlp = spacy.load("en_core_web_sm")
        
    def infer(self,inputs):
        prompts = inputs["prompt"]  # Extract the prompt from the input
        doc = self.nlp(prompts)
        result = ""
        for token in doc:
            result += "\n " + token.text + " - "  +  oken.dep_ 
        return {'generated_result': result } 

    def finalize(self):
        pass
