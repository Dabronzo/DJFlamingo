jQuery(document).ready(function($) {

    setTimeout(function(){
        let message = document.getElementById('msg');
        let alert = new bootstrap.Alert(message)
        alert.close();

    }, 3000);

    var alterClass = function() {
        var ww = document.body.clientWidth;
        if (ww < 800) {
            $(".form-custom").removeClass("w-50");
        } else if (ww >= 800) {
            $(".form-custom").addClass("w-50");
        }
    };
    $(window).resize(function() {
        alterClass();
    });
    //Fire it when the page first loads:
    alterClass();
});