function InizioBlocco() {
    var codiceHTML = 
    '<div class="w3-cell-row">'+
    '   <div class="w3-container w3-cell w3-mobile">'+
    '       <div class="w3-panel w3-card-4 colore w3-round-large">'+
    '           <div class="w3-container" style="text-align: justify;">'
    document.write(codiceHTML);
}

function InizioBloccoSlide() {
    var codiceHTML = 
    '<div class="w3-cell-row">'+
    '   <div class="w3-container w3-cell w3-mobile">'+
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