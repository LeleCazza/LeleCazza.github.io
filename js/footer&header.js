function createColor(){
    var r = Math.floor((Math.random() * 127) + 129);
    var g = Math.floor((Math.random() * 127) + 129);
    var b = Math.floor((Math.random() * 127) + 129);
    return "rgb(" + r + "," + g + "," + b +")";
}

function openMenu() {
    $("#menu").load("../../menu.html");
    document.getElementById("menu").style.display = "block";
    document.getElementById("overlay").style.display = "block"; 
    var color = createColor();
    var divs = document.querySelectorAll(".colore");
    divs.forEach(function (div) {
        div.style.background = color;
    })
}

function closeMenu() {
    document.getElementById("menu").style.display = "none";
    document.getElementById("overlay").style.display = "none";
}
    
$(document.addEventListener("DOMContentLoaded",function() {
    var color = createColor();
    var divs = document.querySelectorAll(".colore");
    divs.forEach(function (div) {
        div.style.background = color;
    })
}))

$(function(){
    $("#footer").load("../../footer.html");
    $("#header").load("../../header.html");
});