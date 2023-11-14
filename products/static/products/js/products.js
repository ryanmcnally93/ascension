document.addEventListener("DOMContentLoaded", function () {
    // Listening for changes to the products filter
    document
        .getElementById("products-filter")
        .addEventListener("change", function () {
            
            var currentUrl = new URL(window.location);
            var selectedValue = this.value;
            
            if (selectedValue == 'no_filter') {
                console.log('No filter has been given');
            } else if (selectedValue != 'all') {
                var sort = selectedValue.split("_")[0];
                var direction = selectedValue.split("_")[1];

                if(direction == 'high') {
                    direction = 'desc';
                } else if(direction == 'low') {
                    direction = 'asc';
                } else {
                    console.log('You have entered an incorrect direction!');
                }

                currentUrl.searchParams.set("sort", sort);
                currentUrl.searchParams.set("direction", direction);
                window.location.replace(currentUrl);
            } else {
                currentUrl.searchParams.delete("sort");
                currentUrl.searchParams.delete("direction");
                window.location.replace(currentUrl);
            }
    });
});

$(window).on('load', function(){
    if ($('#refreshed').val() == "false") {
    $('#refreshed').val("true"); 
    }
    else {
    $('#refreshed').val("false");
    location.reload();
    }
});
$('#myModal').on('shown.bs.modal', function () {
$('#myInput').trigger('focus');
});