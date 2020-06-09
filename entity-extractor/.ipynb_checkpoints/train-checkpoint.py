import spacy
from spacy.matcher import PhraseMatcher
import plac
from pathlib import Path
import random

def offseter (label, doc, matchItem):
  o_one = len(str(doc[0:matchItem[1]])) + 1
  subdoc = doc[matchItem[1]:matchItem[2]]
  o_two = o_one + len(str(subdoc))
  return (o_one, o_two, label)

nlp = spacy.load('es_core_news_sm')

if 'ner' not in nlp.pipe_names:
  ner = nlp.create_pipe('ner')
  nlp.add_pipe(ner)
else:
  ner = nlp.get_pipe('ner')

label = 'VEGGIE'
matcher = PhraseMatcher(nlp.vocab)
ner.add_label(label)

for i in ['cebolla']:
  matcher.add(label, None, nlp(i))

# Busco inici i fi de cada ocurrencia dins el bunch of text
res = []
to_train_ents = []
with open('./test.txt') as gh:
  line = True
  while line:
    line = gh.readline()
    mnlp_line = nlp(line)
    matches = matcher(mnlp_line)
    # print("Matches", matches)
    res = [offseter(label, mnlp_line, x)
           for x
           in matches]
    to_train_ents.append((line, dict(entities=res)))

# Entreno el reconeixador
optimizer = nlp.begin_training()
other_pipes = [pipe
               for pipe
               in nlp.pipe_names
               if pipe != 'ner']

with nlp.disable_pipes(*other_pipes):
  for itn in range(20):
    losses = {}
    random.shuffle(to_train_ents)
    for item in to_train_ents:
      if item[0] != '' and len(item[1]['entities']) > 0:
        nlp.update([item[0]],
                  [item[1]],
                  sgd=optimizer,
                  drop=0.35,
                  losses=losses)
        print('Losses', losses)


# TEST
doc = nlp("7 motivos para consumir cebolla en Barcelona")
for ent in doc.ents:
    print(ent.label_, ent.text)

# Save model
nlp.meta['name'] = 'nyora'  # rename model
nlp.to_disk('./model')
print("Saved model to", './model')