const container = document.getElementById("cards-grid");
const searchInput = document.getElementById("search-input");
const categoryFilter = document.getElementById("category-filter");
function displayDishes(dishesToDisplay) {
    container.innerHTML = "";

    dishesToDisplay.forEach(function(dish) {
        const card = document.createElement("article");

        card.innerHTML = `
    <img src="${dish.image}" alt="${dish.title}">
    <h3>${dish.title}</h3>
    <p>${dish.shortDescription}</p>
    <p>${dish.metric}</p>
    <button class="details-button">View Details</button>`;

    const detailsButton = card.querySelector(".details-button");

detailsButton.addEventListener("click", function() {
    dialogContent.innerHTML = `
        <h2>${dish.title}</h2>
        <img src="${dish.image}" alt="${dish.title}" width="250">
        <p>${dish.fullDetails}</p>
    `;

    dishDialog.showModal();
});


        container.appendChild(card);
    });
}
const sortSelect = document.getElementById("sort-select");
const dishDialog = document.getElementById("dish-dialog");
const dialogContent = document.getElementById("dialog-content");
const closeDialog = document.getElementById("close-dialog");
function filterDishes() {
    const searchText = searchInput.value.toLowerCase();
    const selectedCategory = categoryFilter.value;

    const filteredDishes = dishes.filter(function(dish) {
        const matchesSearch = dish.title.toLowerCase().includes(searchText);

        const matchesCategory =
            selectedCategory === "all" || dish.category === selectedCategory;

        return matchesSearch && matchesCategory;
    });
    if (sortSelect.value === "az") {
    filteredDishes.sort(function(a, b) {
        return a.title.localeCompare(b.title);
    });
}

if (sortSelect.value === "za") {
    filteredDishes.sort(function(a, b) {
        return b.title.localeCompare(a.title);
    });
}

    displayDishes(filteredDishes);
    const emptyState = document.getElementById("empty-state");
    emptyState.hidden = filteredDishes.length > 0;
}

searchInput.addEventListener("input", filterDishes);
categoryFilter.addEventListener("change", filterDishes);
sortSelect.addEventListener("change", filterDishes);

closeDialog.addEventListener("click", function() {
    dishDialog.close();
});
dishDialog.addEventListener("close", function() {
    dialogContent.innerHTML = "";
});
filterDishes();
