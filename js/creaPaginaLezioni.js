function CreaPaginaLezioni(nomiCartelleLezioni, nomiPagineEsercizi){
    if(nomiCartelleLezioni[0] != "NULL"){
        CreaNuovaRiga();
        for (let i = 1; i <= nomiCartelleLezioni.length; i++) {
            CreaBloccoSlides(i);
            CaricaSlides(i,nomiCartelleLezioni[i-1]);    
            TerminaOCreaNuovaRiga(i, nomiCartelleLezioni.length);
        }
        TerminaRiga(nomiCartelleLezioni.length);
    }
    if(nomiPagineEsercizi[0] != "NULL"){
        for (let i = 1; i <= nomiPagineEsercizi.length; i++) 
            CreaBloccoLink(i, nomiPagineEsercizi[i-1]);
    }
}

function CreaBloccoSlides(i){
    IniziaTemplateBloccoSlide(i);
    CreaLezione(i);
    FineTemplateBloccoSlide();
}

function CaricaSlides(idBloccoSlides, nomeCartellaSlides) {
    let pathSlides = "materiale/lezioni/"+nomeCartellaSlides+"/slides.pdf";
    let pathHandout  = "materiale/lezioni/"+nomeCartellaSlides+"/handout.pdf";
    let titoloSlides = GeneraTitoli(nomeCartellaSlides);
    let div = document.getElementById("slides" + idBloccoSlides);
    div.innerHTML +=
        '<p>' +
        '   <button onclick="inizializzaSlides(\'' + pathSlides + '\', \'' + idBloccoSlides + '\'); open_close(\'blocco' + idBloccoSlides + '\', \'' + titoloSlides + '\', \'' + pathSlides + '\');" class="titolo">'+
        '   <b>' + titoloSlides + '</b>' +
        '   </button>' +
        '   <a href="' + pathSlides + '">&#128196</a>' +
        '   <a href="' + pathHandout + '">&#128424</a>' +
        '</p>' +
        '<div id="' + titoloSlides + '" class="w3-content w3-display-container" style="display:none">' +
        '   <div id="pdf-container">' +
        '       <canvas class="w3-mobile" id="' + idBloccoSlides + '"></canvas>' +
        '   </div>' +
        '   <div class="w3-center w3-container w3-section w3-large w3-text-white w3-display-bottommiddle" style="width:100%">' +
        '       <button id="prevPage" onclick="prevPage(\'' + idBloccoSlides + '\')" class="w3-left w3-black">&#10094;</button>' +
        '       <button id="nextPage" onclick="nextPage(\'' + idBloccoSlides + '\')" class="w3-right w3-black">&#10095;</button>' +
        '   </div>' +
        '</div>';
}

function IniziaTemplateBloccoSlide(idBlocco) {
    var codiceHTML = 
    '   <div id="blocco'+idBlocco+'" class="w3-cell w3-padding w3-mobile">'+
    '       <div class="w3-panel w3-display-container w3-card-4 w3-black w3-round-large w3-border-white w3-border" style="height: 100%;">'+
    '           <div class="w3-display-container w3-center" style="height: 100%;">'
    document.write(codiceHTML);
}

function CreaLezione(numLezione){
    let codiceHTML = '<div id="slides'+numLezione+'"></div>';
    document.write(codiceHTML);
}

function FineTemplateBloccoSlide() {
    var codiceHTML = '</div></div></div>'
    document.write(codiceHTML);
}

function CreaBloccoLink(i, nomiPagineEsercizi){
    IniziaTemplateBloccoLink();
    Crea_CaricaLink(i, nomiPagineEsercizi);
    FineTemplateBloccoLink();
}

function IniziaTemplateBloccoLink() {
    var codiceHTML = 
    '<div class="w3-cell-row">'+
    '   <div class="w3-container w3-cell w3-mobile">'+
    '       <div class="w3-panel w3-card-4 w3-black w3-round-large w3-border-white w3-border">'+
    '           <div class="w3-container w3-center">'
    document.write(codiceHTML);
}

function Crea_CaricaLink(i,pathEsercizio){
    let codiceHTML = '<a href="'+pathEsercizio+'.html" style="text-decoration: none;"><p><b>'+GeneraTitoli(NOMI_PAGINE_ESERCIZI[i-1])+'</b></p></a>';
    document.write(codiceHTML);
}

function FineTemplateBloccoLink() {
    var codiceHTML = '</div></div></div></div>'
    document.write(codiceHTML);
}

function CreaNuovaRiga(){
    let codiceHTML = '<div class="w3-cell-row">';
    document.write(codiceHTML);
}

function TerminaOCreaNuovaRiga(i,numCartelle){
    if(i%4 == 0){
        FineRiga();
        if(i != numCartelle)
            CreaNuovaRiga();
    }
}

function TerminaRiga(numCartelle){
    if(numCartelle%4 != 0)
        FineRiga();
}

function FineRiga(){
    let codiceHTML = '</div>';
    document.write(codiceHTML);
}