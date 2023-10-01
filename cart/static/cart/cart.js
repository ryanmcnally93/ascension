let prices = document.getElementByClassNames('prices');
let quantities = document.getElementByClassName('quantity-middle');
let total_prices = document.getElementByClassName('total-price');

$('total-price').each.value = $('prices').each.value * $('quantity-middle').each.value