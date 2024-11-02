var slideIndex = 1;

function plusDivs(n, className) {
  showDivs(slideIndex += n, className);
}

function currentDiv(n, className) {
  showDivs(slideIndex = n, className);
}

function showDivs(n, className) {
    var i;
    var x = document.getElementsByClassName(className);
    if (n > x.length){
        slideIndex = 1
    }
    if (n < 1){
        slideIndex = x.length
    }
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";  
    }
    x[slideIndex-1].style.display = "block";  
}

function open_close(id, className) {
  var x1 = document.getElementById(id);
  var x2 = document.getElementsByClassName("w3-show");
  for (let i = 0; i < x2.length; i++) {
    if(x1 != x2[i])
      x2[i].className = x2[i].className.replace(" w3-show", "");
  }
  if (x1.className.indexOf("w3-show") == -1) {
    x1.className += " w3-show";
  } else { 
    x1.className = x1.className.replace(" w3-show", "");
  }
  slideIndex = 1;
  showDivs(slideIndex, className);
}