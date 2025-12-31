import spacy
from spacy.training.example import Example
from data.train_data import TRAIN_DATA

# Create blank English model
nlp = spacy.blank("en")

# Add NER pipe
ner = nlp.add_pipe("ner")

# Add labels
for _, ann in TRAIN_DATA:
    for ent in ann["entities"]:
        ner.add_label(ent[2])

# Initialize model (spaCy v3+ way)
nlp.initialize()

# Train
for epoch in range(25):
    losses = {}
    for text, ann in TRAIN_DATA:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, ann)
        nlp.update([example], losses=losses)

    print(f"Epoch {epoch + 1} | Loss: {losses}")

# Save model
nlp.to_disk("model")
print("✅ Model saved in ./model")
