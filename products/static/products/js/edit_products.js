document.addEventListener("DOMContentLoaded", function () {
    if (document.getElementById('id_name').value != "") {
        document.getElementById('invisible-form').style.display = "flex";
        document.getElementById('product-id').value = document.getElementById('id_name').value;
    } else {
        document.getElementById('invisible-form').style.display = "none";
    }
});
document.addEventListener("DOMContentLoaded", function () {
    document
        .getElementById("id_striked_price")
        .addEventListener("change", function () {
            // If the striked price is empty, this is a normal item
            if (this.value == "") {
                document.getElementById('id_is_offers_item').value = 'false';
            } else {
                // If a striked price is entered, it's on offer!
                document.getElementById('id_is_offers_item').value = 'true';
            }
        });
    document
        .getElementById("id_category")
        .addEventListener("change", function () {
            // Checking if the category value is one of a hire rooms
            if (this.value == "7") {
                document.getElementById('id_is_hire_room').value = 'true';
            } else if (this.value == "8") {
                document.getElementById('id_is_hire_room').value = 'true';
            } else {
                document.getElementById('id_is_hire_room').value = 'false';
            }
        });
});