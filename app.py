from flask import Flask, request, jsonify, render_template
import spacy
import re
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model")

nlp = spacy.load(MODEL_PATH)


UNITS = [
    "cup", "cups", "tbsp", "tsp", "ml", "l", "kg", "g",
    "teaspoon", "tablespoon", "oz", "pound"
]


quantity_pattern = re.compile(r"\b\d+(\.\d+)?|\b½|\b¼|\b¾")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/extract", methods=["POST"])
def extract():
    data = request.get_json()
    text = data.get("recipe", "").lower()

    results = []

    parts = re.split(r"\n|,| and ", text)

    for line in parts:
        line = line.strip()
        if not line:
            continue

        
        if any(x in line for x in ["docker", "http", "run"]):
            continue

        quantity = None
        unit = None
        ingredient = None

       
        qty_match = quantity_pattern.search(line)
        if qty_match:
            quantity = qty_match.group()

        
        for u in UNITS:
            if re.search(rf"\b{u}\b", line):
                unit = u
                break

       
        doc = nlp(line)
        for ent in doc.ents:
            if ent.label_ == "INGREDIENT":
                ingredient = ent.text.strip()

        
        if ingredient is None:
            cleaned = line
            if quantity:
                cleaned = cleaned.replace(quantity, "")
            if unit:
                cleaned = cleaned.replace(unit, "")
            cleaned = re.sub(r"\b(add|of)\b", "", cleaned)
            ingredient = cleaned.strip()

        if ingredient:
            results.append({
                "ingredient": ingredient,
                "quantity": quantity,
                "unit": unit
            })

    return jsonify({"ingredients": results})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)