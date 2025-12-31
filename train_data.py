TRAIN_DATA = []

with open("raw_sentences.txt", "r", encoding="utf-8") as f:
    for text in f:
        text = text.strip()
        parts = text.split()

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
                    (i_start, i_start + len(ingredient), "INGREDIENT")
                ]
            }
        ))
