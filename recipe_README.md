#  Recipe Ingredient Extraction (NER Web App)

This project is a **Natural Language Processing (NLP) based web
application** that extracts structured ingredient information
(ingredient name, quantity, and unit) from plain recipe text using a

# Project Overview

The system converts unstructured recipe sentences into structured JSON
output.

# Example Input

    Add 200 grams rice and 1 tsp salt

# Example Output

``` json
{
  "ingredients": [
    {
      "ingredient": "rice",
      "quantity": "200",
      "unit": "grams"
    },
    {
      "ingredient": "salt",
      "quantity": "1",
      "unit": "tsp"
    }
  ],
  "input": "Add 200 grams rice and 1 tsp salt"
}
```


#  Features

-   Custom-trained spaCy Named Entity Recognition (NER) model
-   Extracts:
    -   INGREDIENT
    -   QUANTITY
    -   UNIT
-   Flask backend
-   Web-based UI
-   JSON API output
-   Docker support
-   Training script included
-   Easy deployment

#  Tech Stack

  Layer              Technology
  ------------------ -----------------------
  Language           Python
  NLP                spaCy
  Backend            Flask
  Frontend           HTML, CSS, JavaScript
  Containerization   Docker
  Version Control    Git


#  Project Structure

    recipe-ner/
    │
    ├── app.py                 # Flask backend
    ├── train_data.py          # Model training script
    ├── raw_sentences.txt      # Training dataset
    ├── requirements.txt       # Python dependencies
    ├── Dockerfile             # Docker configuration
    │
    ├── model/                 # Trained spaCy model
    │   ├── config.cfg
    │   ├── meta.json
    │   ├── tokenizer
    │   ├── ner/
    │   └── vocab/
    │
    ├── templates/
    │   └── index.html
    │
    ├── static/
    │   ├── style.css
    │   └── script.js
    │
    └── data/


#  Model Training

The NER model is trained using labeled recipe sentences.

# Training command:

python train_data.py

This generates the trained model inside the `model/` directory.

The Flask app loads the model using:
 python
nlp = spacy.load("model")


#  Run Locally (Without Docker)

# Step 1: Install dependencies

pip install -r requirements.txt


# Step 2: Run server


python app.py

# Step 3: Open in browser

    http://localhost:5000



# Run Using Docker

# Build image

docker build -t recipe-ner .

# Run container

docker run -p 5000:5000 recipe-ner


# Open browser

    http://localhost:5000




#  How the Model Works

1.  Training sentences are labeled with entity tags:
    -   INGREDIENT
    -   QUANTITY
    -   UNIT
2.  spaCy learns token patterns using NER.
3.  The trained model is saved in the `model/` folder.
4.  Flask loads this model at runtime.
5.  User input → model → structured JSON output.


#  Future Improvements

-   Increase dataset size for better accuracy
-   Add confidence scores
-   Upload text/CSV files
-   Improve UI design
-   Add authentication
-   Deploy on cloud (Render / Railway / AWS)
-   Add REST API documentation

