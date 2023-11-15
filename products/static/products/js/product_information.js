$(window).on('load', function(){
    if ($('#refreshed').val() == "false") {
    $('#refreshed').val("true"); 
    }
    else {
    $('#refreshed').val("false");
    location.reload(true);
    }
});

// We need to make sure the radios are invisible when content is loaded
document.addEventListener("DOMContentLoaded", function () {
    radioShow();
});

// Listener for changed within the page
document.addEventListener("change", function () {
    radioShow();
});

var radios = document.getElementsByClassName('radio');
for (let radio of radios) {
    radio.addEventListener("click", function () {
        // Set value of hidden input to selected radio's name
        document.getElementById('chosen-time').value = radio.id;
    });
}
function radioShow() {
    if (document.getElementById('no-radios') != null) {
        if (document.getElementById('date').value == "") {
            // Make dates invisible and message visible
            let times = document.getElementsByClassName('radio');
            for (i = 0; i < times.length; i++) {
                times[i].style.display = 'none';
            }
            let para = document.getElementsByClassName('timeline-button');
            for (i = 0; i < para.length; i++) {
                para[i].style.display = 'none';
            }
            let noRadios = document.getElementById('no-radios');
            noRadios.style.display = 'block';
        } else if (document.getElementById('date').value != "") {
            // Make message invisible and radios visible
            let times = document.getElementsByClassName('radio');
            for (i = 0; i < times.length; i++) {
                times[i].style.display = 'inline';
            }
            let para = document.getElementsByClassName('timeline-button');
            for (i = 0; i < para.length; i++) {
                para[i].style.display = 'inline';
            }
            let noRadios = document.getElementById('no-radios');
            noRadios.style.display = 'none';
        }
    }
}

// Taken from W3Schools
// This code is to make the Slideshow's work
let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
showSlides(slideIndex = n);
}

function showSlides(n) {
let i;
let slides = document.getElementsByClassName("mySlides");
if (n > slides.length) {slideIndex = 1;}
if (n < 1) {slideIndex = slides.length;}
for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
}
slides[slideIndex-1].style.display = "flex";

if (document.getElementsByClassName("dot").length != 0) {
    let dots = document.getElementsByClassName("dot");
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    dots[slideIndex-1].className += " active";
    }
}

// Grab all the elements provided by views
dates = document.getElementsByClassName('dates')

// Add event listeners for page load and changes being made
document.addEventListener("DOMContentLoaded", function () {
    document.addEventListener("change", function () {

        // Format the date in datepicker to match the dates in the elements id's
        let chosenDate = document.getElementById('date').value.split("-");
        let year = chosenDate[0];
        let month = chosenDate[1];
        let day = chosenDate[2];
        let updatedDate = day + "-" + month + "-" + year

        // Sift through all the dates
        for (i = 0; i < dates.length; i++) {
            // If the dates match
            if (dates.item(i).id == updatedDate) {

                // Lets set all the radios and text back to normal before we change for this item
                document.getElementById('10:00p').innerHTML = ' 10:00';
                document.getElementById('11:00p').innerHTML = ' 11:00';
                document.getElementById('12:00p').innerHTML = ' 12:00';
                document.getElementById('13:00p').innerHTML = ' 13:00';
                document.getElementById('14:00p').innerHTML = ' 14:00';
                document.getElementById('15:00p').innerHTML = ' 15:00';
                document.getElementById('10:00').disabled = false;
                document.getElementById('11:00').disabled = false;
                document.getElementById('12:00').disabled = false;
                document.getElementById('13:00').disabled = false;
                document.getElementById('14:00').disabled = false;
                document.getElementById('15:00').disabled = false;

                // Lets create multiple items for each time and for loop through all the times provided
                timearray = dates.item(i).innerText.split(', ')
                for (i=0; i<timearray.length; i++) {
                    // This is the p element of all the times we want to restrict, lets strike them out
                    var restricted = document.getElementById(timearray[i] + 'p');
                    restricted.innerHTML='<del> ' + timearray[i] + '</del>';
                    restricted.setAttribute('aria-label', 'This session is taken');
                    // And disable the radio button next to it
                    document.getElementById(timearray[i]).disabled = true;
                }

            } else {
                // If the times aren't booked, we need to make them all available
                document.getElementById('10:00p').innerHTML = ' 10:00';
                document.getElementById('11:00p').innerHTML = ' 11:00';
                document.getElementById('12:00p').innerHTML = ' 12:00';
                document.getElementById('13:00p').innerHTML = ' 13:00';
                document.getElementById('14:00p').innerHTML = ' 14:00';
                document.getElementById('15:00p').innerHTML = ' 15:00';
                document.getElementById('10:00').disabled = false;
                document.getElementById('11:00').disabled = false;
                document.getElementById('12:00').disabled = false;
                document.getElementById('13:00').disabled = false;
                document.getElementById('14:00').disabled = false;
                document.getElementById('15:00').disabled = false;
            }
        }
    });
});