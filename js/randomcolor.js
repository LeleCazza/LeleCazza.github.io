function createColor(){
    var r = Math.floor((Math.random() * 127) + 129);
    var g = Math.floor((Math.random() * 127) + 129);
    var b = Math.floor((Math.random() * 127) + 129);
    return "rgb(" + r + "," + g + "," + b +")";
}        
    
document.addEventListener("DOMContentLoaded",function() {
    var color = createColor();
    var divs = document.querySelectorAll(".colore");
    divs.forEach(function (div) {
        div.style.background = color;
    })
})