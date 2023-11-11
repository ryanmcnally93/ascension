$('.toast').toast('show');
$('.toast-close').each(function() {
    $(this).click(function() {
        $('.toast').hide();
    });
});
/* This function acts in the event that the toast is open */
/* and the user clicks on user-options, it closes the toast */
/* making the dropdown visible */
function closeToast() {
    if ($('toast').toast('show')) {
        $('.toast').hide();
    }
}