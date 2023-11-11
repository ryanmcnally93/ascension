$(window).on("load", function () {
    if ($("#refreshed").val() == "false") {
      $("#refreshed").val("true");
    } else {
      $("#refreshed").val("false");
      location.reload(true);
    }
  });