from flask import Flask, request, jsonify, render_template
import spacy

app = Flask(__name__)
nlp = spacy.load("model")


@app.route("/")
def home():
    return render_template("index.html")


from flask import Flask, request, jsonify, render_template
import spacy

app = Flask(__name__)
nlp = spacy.load("model")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/extract", methods=["POST"])
def extract():
    data = request.get_json()
    text = data.get("recipe", "")

    lines = [line.strip() for line in text.split("\n") if line.strip()]
    results = []

    for line in lines:
        doc = nlp(line)
        current = {}

        for ent in doc.ents:
            clean_value = (
                ent.text
                .replace("\n", " ")
                .replace("\t", " ")
                .replace("Add", "")
                .replace("add", "")
                .strip()
            )

            if ent.label_ == "QUANTITY":
                current["quantity"] = clean_value

            elif ent.label_ == "UNIT":
                current["unit"] = clean_value

            elif ent.label_ == "INGREDIENT":
                current["ingredient"] = clean_value

        if current:
            results.append(current)

    return jsonify({
        "input": text,
        "ingredients": results
    })



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


