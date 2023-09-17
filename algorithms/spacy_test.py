import spacy
from spacy.parts_of_speech import PROPN, NUM


def is_proper_noun(token):
    if token.doc.is_tagged is False:  # check if the document was POS-tagged
        raise ValueError('token is not POS-tagged')

    if token.pos == PROPN:
        return True
    
    if token.pos == NUM:
        return True
    
    return False


text = input()

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

token_count = {}
for token in doc:
    if not is_proper_noun(token):
        continue

    text = token.text

    if text not in token_count:
        token_count[text] = 1
    else:
        token_count[text] += 1


for k, v in token_count.items():
    out = f'"{k}" was found {v} times'
    print(f"{out : >20}")

