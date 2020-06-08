import spacy
print("Loading from ./model")
nlp = spacy.load('./model')
doc = nlp("""
Como guarnición, acompañamiento, "topping"... Esta cebolla caramelizada, una receta deliciosa y sencilla de elaborar, hará más delicioso si cabe todo aquello que toque. ¿Quieres probar una tortilla española distinta? Añádele esta cebolla confitada y déjate sorprender por el resultado. No te pierdas el paso a paso y aprende con RecetasGratis.net a cocinar la cebolla de esta forma, ¡te encantará!
""")

for ent in doc.ents:
    print(ent.label_, ent.text)