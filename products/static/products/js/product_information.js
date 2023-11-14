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