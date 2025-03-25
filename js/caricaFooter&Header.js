function openMenu() {
    $("#menu").load("/pagine/menu.html");
    document.getElementById("menu").style.display = "block";
    document.getElementById("overlay").style.display = "block"; 
}

function closeMenu() {
    document.getElementById("menu").style.display = "none";
    document.getElementById("overlay").style.display = "none";
}

$(function(){
    $("#footer").load("/pagine/footer.html");
    $("#header").load("/pagine/header.html");
});