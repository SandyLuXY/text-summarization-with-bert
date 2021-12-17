import spacy
import neuralcoref


class NeuralCoreference:
    def __init__(self):
        self.nlp = spacy.load('en')
        neuralcoref.add_to_pipe(self.nlp)
        
    def coreference_resolver(self, contents):
        doc = self.nlp(contents)
        return doc._.coref_resolved
