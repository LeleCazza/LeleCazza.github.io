function InizioBloccoEsercizio() {
    var codiceHTML = 
    '<div class="w3-cell-row">'+
    '   <div class="w3-container w3-cell w3-mobile">'+
    '       <div class="w3-panel w3-card-4 colore w3-round-large">'+
    '           <div class="w3-container" style="text-align: justify;">'
    document.write(codiceHTML);
}

function InizioBloccoLink() {
    var codiceHTML = 
    '<div class="w3-cell-row">'+
    '   <div class="w3-container w3-cell w3-mobile">'+
    '       <div class="w3-panel w3-card-4 colore w3-round-large">'+
    '           <div class="w3-container w3-center">'
    document.write(codiceHTML);
}

function InizioBloccoSlide(idBlocco) {
    var codiceHTML = 
    '   <div id="'+idBlocco+'" class="w3-container w3-cell w3-mobile">'+
    '       <div class="w3-panel w3-card-4 colore w3-round-large">'+
    '           <div class="w3-container w3-center" style="text-align: justify; ">'
    document.write(codiceHTML);
}

function Testo(nomeEsercizio, pathEsercizio) {
    $("#" + nomeEsercizio).load(pathEsercizio);
}

function FineBlocco() {
    var codiceHTML = '</div></div></div></div>'
    document.write(codiceHTML);
}

function FineBloccoSlide() {
    var codiceHTML = '</div></div></div>'
    document.write(codiceHTML);
}

function CaricaSlides(idSlides, idBlocco, pathSlides, titoloSlides) {
    var div = document.getElementById("slides" + idSlides);
    div.innerHTML +=
        '<p>' +
        '   <button onclick="inizialize(\'' + pathSlides + '\', \'' + idSlides + '\'); open_close(\'' + idBlocco + '\', \'' + titoloSlides + '\');" class="titolo">'+
        '   <b>' + titoloSlides + '</b>' +
        '   </button>' +
        '   <a href="' + pathSlides + '"><img src="../../images/floppy_logo.png" alt="scarica" style="width: 18px"></a>' +
        '</p>' +
        '<div id="' + titoloSlides + '" class="w3-content w3-display-container" style="display:none">' +
        '   <div id="pdf-container">' +
        '       <canvas class="w3-mobile" id="' + idSlides + '"></canvas>' +
        '   </div>' +
        '   <div class="w3-center w3-container w3-section w3-large w3-text-white w3-display-bottommiddle" style="width:100%">' +
        '       <button id="prevPage" onclick="prevPage(\'' + idSlides + '\')" class="w3-left w3-black">&#10094;</button>' +
        '       <button id="nextPage" onclick="nextPage(\'' + idSlides + '\')" class="w3-right w3-black">&#10095;</button>' +
        '   </div>' +
        '</div>'
}