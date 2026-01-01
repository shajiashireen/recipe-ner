import spacy
from spacy.training import Example
import random
import os


nlp = spacy.blank("en")


if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
else:
    ner = nlp.get_pipe("ner")


TRAIN_DATA = []

with open("raw_sentences.txt", "r", encoding="utf-8") as f:
    for line in f:
        text = line.strip()
        if not text:
            continue

        parts = text.split()
        if len(parts) < 4:
            continue

        quantity = parts[1]
        unit = parts[2]
        ingredient = " ".join(parts[3:])

        q_start = text.find(quantity)
        u_start = text.find(unit)
        i_start = text.find(ingredient)

        TRAIN_DATA.append((
            text,
            {
                "entities": [
                    (q_start, q_start + len(quantity), "QUANTITY"),
                    (u_start, u_start + len(unit), "UNIT"),
                    (i_start, i_start + len(ingredient), "INGREDIENT"),
                ]
            }
        ))


for _, annotations in TRAIN_DATA:
    for start, end, label in annotations["entities"]:
        ner.add_label(label)


optimizer = nlp.initialize()


n_iter = 20
for epoch in range(n_iter):
    random.shuffle(TRAIN_DATA)
    losses = {}

    for text, annotations in TRAIN_DATA:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update([example], sgd=optimizer, losses=losses)

    print(f"Epoch {epoch + 1}/{n_iter} - Losses: {losses}")


output_dir = "model"
os.makedirs(output_dir, exist_ok=True)
nlp.to_disk(output_dir)

print("\n✅ Training completed and model saved to /model")
