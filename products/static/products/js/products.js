document.addEventListener("DOMContentLoaded", function () {
    document
        .getElementById("products-filter")
        .addEventListener("change", function () {
            
            var currentUrl = new URL(window.location);
            var selectedValue = this.value;
            
            if(selectedValue != 'all') {
                var sort = selectedValue.split("_")[0];
                var direction = selectedValue.split("_")[1];

                if(direction == 'high') {
                    direction = 'desc'
                } else if(direction == 'low') {
                    direction = 'asc'
                } else {
                    console.log('You have entered an incorrect direction!')
                }

                currentUrl.searchParams.set("sort", sort);
                currentUrl.searchParams.set("direction", direction);
                console.log(sort + direction)
                window.location.replace(currentUrl);
            } else {
                currentUrl.searchParams.delete("sort");
                currentUrl.searchParams.delete("direction");
                window.location.replace(currentUrl);
            }
    });
});