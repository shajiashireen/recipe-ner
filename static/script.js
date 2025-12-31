function toggleTheme() {
    document.body.classList.toggle("dark");
}

async function extractIngredients() {
    const text = document.getElementById("recipe").value.trim();
    const resultsBox = document.getElementById("results");
    const ingredientBox = document.getElementById("ingredientCards");
    const jsonBox = document.getElementById("jsonOutput");

    if (!text) {
        alert("Please enter a recipe first.");
        return;
    }

    const response = await fetch("/extract", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ recipe: text })
    });

    const data = await response.json();

    resultsBox.classList.remove("hidden");
    ingredientBox.innerHTML = "";

    if (!data.ingredients || data.ingredients.length === 0) {
        ingredientBox.innerHTML = "<p>No ingredients detected.</p>";
    } else {
        data.ingredients.forEach(item => {
            const div = document.createElement("div");
            div.className = "ingredient-card";
            div.innerHTML = `
                <b>Ingredient:</b> ${item.ingredient}<br>
                <b>Quantity:</b> ${item.quantity}<br>
                <b>Unit:</b> ${item.unit}
            `;
            ingredientBox.appendChild(div);
        });
    }

    jsonBox.textContent = JSON.stringify(data, null, 2);
}
