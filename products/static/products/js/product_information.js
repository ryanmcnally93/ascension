$(window).on('load', function(){
    if ($('#refreshed').val() == "false") {
    $('#refreshed').val("true"); 
    }
    else {
    $('#refreshed').val("false");
    location.reload(true);
    }
});

document.addEventListener("DOMContentLoaded", function () {
    radioShow();
});
document.addEventListener("change", function () {
    radioShow();
});
var radios = document.getElementsByClassName('radio');
for (let radio of radios) {
    radio.addEventListener("click", function () {
        document.getElementById('chosen-time').value = radio.id;
    });
};
function radioShow() {
    if (document.getElementById('date').value == "") {
        let times = document.getElementsByClassName('radio')
        for (i = 0; i < times.length; i++) {
            times[i].style.display = 'none';
        }
        let para = document.getElementsByClassName('timeline-button')
        for (i = 0; i < para.length; i++) {
            para[i].style.display = 'none';
        }
        let noRadios = document.getElementById('no-radios')
        noRadios.style.display = 'block';
    } else if (document.getElementById('date').value != "") {
        let times = document.getElementsByClassName('radio')
        for (i = 0; i < times.length; i++) {
            times[i].style.display = 'inline';
        }
        let para = document.getElementsByClassName('timeline-button')
        for (i = 0; i < para.length; i++) {
            para[i].style.display = 'inline';
        }
        let noRadios = document.getElementById('no-radios')
        noRadios.style.display = 'none';
    }
}
// Taken from W3Schools
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
let dots = document.getElementsByClassName("dot");
if (n > slides.length) {slideIndex = 1}
if (n < 1) {slideIndex = slides.length}
for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
}
for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
}
slides[slideIndex-1].style.display = "flex";
dots[slideIndex-1].className += " active";
}