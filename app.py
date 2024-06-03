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
        for token in doc:
            print(token.text, token.pos_, token.dep_)
        return {'generated_result': json.dumps(doc) } 

    def finalize(self):
        pass
