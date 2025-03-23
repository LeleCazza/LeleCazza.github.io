function openMenu() {
    $("#menu").load("/menu.html");
    document.getElementById("menu").style.display = "block";
    document.getElementById("overlay").style.display = "block"; 
}

function closeMenu() {
    document.getElementById("menu").style.display = "none";
    document.getElementById("overlay").style.display = "none";
}

$(function(){
    $("#footer").load("/footer.html");
    $("#header").load("/header.html");
});