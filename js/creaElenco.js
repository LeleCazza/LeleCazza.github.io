function creaElenco(elenco, icona) {
    for (let i = 0; i < elenco.length; i++) {
        if (i % 2 === 0) {
            document.write('<div class="w3-cell-row">');
        }

        document.write(`
            <div class="w3-cell w3-half w3-padding w3-mobile">
                <div class="w3-panel w3-display-container w3-card-4 w3-black w3-round-large w3-border-white w3-border" style="height: 100%;">
                    <div class="w3-display-container w3-center" style="text-align: justify; height: 100%;">
                        <a href="${elenco[i].link}" style="text-decoration: none;">
                            <br>
                            ${elenco[i].copertina ? '<img src=' + elenco[i].copertina + ' class="w3-round w3-image" style="max-height:80px">' : '<h1>' + icona + '</h1>'}
                            <div class="w3-container">
                                <p>
                                    <b>${elenco[i].nome}</b>
                                    <br>
                                    ${elenco[i].autore ? elenco[i].autore + '<br>' : ''}
                                    ${elenco[i].anno ? elenco[i].anno : ''}
                                </p>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
        `);

        if (i % 2 === 1 || i === elenco.length - 1)
            document.write('</div>');
    }
}