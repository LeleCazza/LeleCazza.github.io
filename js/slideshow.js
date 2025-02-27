let pdfUrl = null;
let pdfDoc = null;
let currentPage = 1;
let totalPages = 0;
let bloccoVisibile = null;

function inizialize(url, id){
    currentPage = 1;
    totalPages = 0;
    pdfUrl = url;
    const loadingTask = pdfjsLib.getDocument(pdfUrl);
    loadingTask.promise.then(function (pdf) {
        pdfDoc = pdf;
        totalPages = pdf.numPages;
        renderPage(currentPage, id);
    });
    
}

function renderPage(pageNum, id) {
    pdfDoc.getPage(pageNum).then(function (page) {
        const canvas = document.getElementById(id);
        const context = canvas.getContext('2d');
        const viewport = page.getViewport({ scale: 1 });

        canvas.width = viewport.width;
        canvas.height = viewport.height;

        page.render({
            canvasContext: context,
            viewport: viewport
        });
        $('#prevPage').prop('disabled', currentPage === 1);
        $('#nextPage').prop('disabled', currentPage === totalPages);
    });
};

function prevPage(id){
    if (currentPage > 1) {
        currentPage--;
        renderPage(currentPage,id);
    }
};

function nextPage(id){
    if (currentPage < totalPages) {
        currentPage++;
        renderPage(currentPage,id);
    }
};

function open_close(idBloccoDaNonNascondere, titoloSlides) {
    const elementiBlocco = document.querySelectorAll('[id*="blocco"]');
    if(bloccoVisibile == null){
        elementiBlocco.forEach(elemento => {
            if(elemento.id != idBloccoDaNonNascondere){
                elemento.style.display = "none";    
            }
            bloccoVisibile = idBloccoDaNonNascondere;
        });
        bloccoVisibile = idBloccoDaNonNascondere;
        document.getElementById(titoloSlides).style.display = "";
    }
    else{
        elementiBlocco.forEach(elemento => {
            elemento.style.display = "";    
        });
        bloccoVisibile = null;
        document.getElementById(titoloSlides).style.display = "none";
    }
}