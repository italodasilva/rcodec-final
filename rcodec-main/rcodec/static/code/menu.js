var ul = document.querySelector('nav ul');
var menuBtn = document.querySelector('.menu-btn i');

function menuShow() {
    var ul = $('#menubar')

    if(!ul.hasClass('open')) {
        ul.addClass('open')
    }else{
        ul.removeClass('open');
    }
}