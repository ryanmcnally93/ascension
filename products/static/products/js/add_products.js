document.addEventListener("DOMContentLoaded", function () {
    document
        .getElementById("id_striked_price")
        .addEventListener("change", function () {
            if (this.value == "") {
                document.getElementById('id_is_offers_item').value = 'false';
            } else {
                document.getElementById('id_is_offers_item').value = 'true';
            }
        });
    document
        .getElementById("id_category")
        .addEventListener("change", function () {
            if (this.value == "7") {
                document.getElementById('id_is_hire_room').value = 'true';
            } else if (this.value == "8") {
                document.getElementById('id_is_hire_room').value = 'true';
            } else {
                document.getElementById('id_is_hire_room').value = 'false';
            }
        });
});