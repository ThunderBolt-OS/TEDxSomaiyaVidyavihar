$(document).ready(function(){
    $('.btn0').click(function() {
        $(".btn").attr('data-modal-target', '#zeroth');
        $("#slider").style.pointerEvents = "none";
    }); 
    $('.btn1').click(function() {
        $(".btn").attr('data-modal-target', '#first');
        $("#slider").style.pointerEvents = "none";
    }); 
    $('.btn2').click(function() {
        $(".btn").attr('data-modal-target', '#second');
        $("#slider").style.pointerEvents = "none";
    }); 
    $('.btn3').click(function() {
        $(".btn").attr('data-modal-target', '#third');
        $("#slider").style.pointerEvents = "none";
    }); 
    $('.btn4').click(function() {
        $(".btn").attr('data-modal-target', '#forth');
    }); 
    $('.btn5').click(function() {
        $(".btn").attr('data-modal-target', '#fifth');
    }); 
    $('.btn6').click(function() {
        $(".btn").attr('data-modal-target', '#sixth');
    }); 
    $('.btn7').click(function() {
        $(".btn").attr('data-modal-target', '#seventh');
    }); 
    $('.btn8').click(function() {
        $(".btn").attr('data-modal-target', '#eighth');
    }); 
});