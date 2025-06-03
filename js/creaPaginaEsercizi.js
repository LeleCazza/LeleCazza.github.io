function CreaPaginaEsercizi(nomeCartellaEsercizi, numeroDiEsercizi, intro, soluzioni, nomiFileSoluzioni){
    if(intro) {
        CreaBloccoIntro();
        CaricaIntro(nomeCartellaEsercizi);
    }
    for (let i = 1; i <= numeroDiEsercizi; i++) {
        CreaBloccoEsercizio(i);
        CaricaEsercizio(i, nomeCartellaEsercizi);
        if(soluzioni)
            CaricaSoluzione(i, nomeCartellaEsercizi, nomiFileSoluzioni);                    
    }
}

function CreaBloccoIntro(){
    IniziaTemplateBloccoEsercizio();
    CreaIntro();
    FineTemplateBloccoEsercizio();
}

function CreaIntro(){
    let codiceHTML = '<div id="intro"></div>';
    document.write(codiceHTML);
}

function CaricaIntro(nomeCartellaEsercizi) {
    $("#intro").load("materiale/esercizi/"+nomeCartellaEsercizi+"/intro.html");
};

function CreaBloccoEsercizio(i){
    IniziaTemplateBloccoEsercizio();
    CreaEsercizio(i);
    CreaSoluzione(i);
    FineTemplateBloccoEsercizio();
}

function IniziaTemplateBloccoEsercizio() {
    let codiceHTML =
        '<div class="w3-cell-row">'+
        '   <div class="w3-container w3-cell w3-mobile">'+
        '       <div class="w3-panel w3-card-4 w3-black w3-round-large w3-border-white w3-border">'+
        '           <div class="w3-container" style="text-align: justify;">';
    document.write(codiceHTML);
}

function CreaEsercizio(i){
    let codiceHTML = '<h1>ESERCIZIO '+i+'</h1><div id="esercizio'+i+'"></div><br>';
    document.write(codiceHTML);
}

function CreaSoluzione(i){
    let codiceHTML = '<div id="soluzione'+i+'"></div>';
    document.write(codiceHTML);
}

function CaricaEsercizio(numEsercizio, nomeCartellaEsercizi) {
    $("#esercizio" + numEsercizio).load("materiale/esercizi/"+nomeCartellaEsercizi+"/esercizio" + numEsercizio + "/esercizio.html", function(){
        $("#esercizio" + numEsercizio + " a").each(function () {
            let href = $(this).attr("href");
            if(href != null && (!href.includes("https://") && !href.includes("http://")))
                $(this).attr("href", "materiale/esercizi/"+nomeCartellaEsercizi+"/esercizio" + numEsercizio + '/' + href);
        });
    });
}

function CaricaSoluzione(numEsercizio, nomeCartellaEsercizi, nomiFileSoluzioni) {
    var div = document.getElementById("soluzione" + numEsercizio);
    div.innerHTML += 'Soluzioni:<br><i>';
    nomiFileSoluzioni.forEach(soluzione => {
        let titolo = GeneraTitoli(soluzione.split(".")[0]);
        div.innerHTML += 
            '<a href="materiale/esercizi/'
                + nomeCartellaEsercizi
                + '/esercizio'
                + numEsercizio
                + '/'
                + soluzione
                + '" target=_blank>'
                + titolo
                + '</a><br>';
    });
    div.innerHTML += '</i><br>';
}

function FineTemplateBloccoEsercizio() {
    var codiceHTML = '</div></div></div></div>'
    document.write(codiceHTML);
}