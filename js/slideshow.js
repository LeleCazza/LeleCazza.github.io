let pdfUrl = null;
let pdfDoc = null;
let currentPage = 1;
let totalPages = 0;
let bloccoVisibile = null;

function inizializzaSlides(url, id){
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
        const container = canvas.parentElement;
        const rect = canvas.getBoundingClientRect();
        container.querySelectorAll('.pdf-link').forEach(link => link.remove());
        page.render({ canvasContext: context, viewport: viewport })
            .promise.then(() => {
                return page.getAnnotations();
            }).then((annotations) => {
                annotations.forEach(annotation => {
                    if (annotation.subtype === 'Link' && annotation.url) {
                        const [x1, y1, x2, y2] = annotation.rect;
                        const scale = viewport.scale;
                        const x = x1 * scale;
                        const y = (page.view[3] - y2) * scale;
                        const width = (x2 - x1) * scale;
                        const height = (y2 - y1) * scale;
                        const scaleX = rect.width / canvas.width;
                        const scaleY = rect.height / canvas.height;
                        const link = document.createElement('a');
                        link.className = 'pdf-link';
                        link.href = annotation.url;
                        link.target = '_blank';
                        link.style.position = 'absolute';
                        link.style.left = `${canvas.offsetLeft + x * scaleX}px`;
                        link.style.top = `${canvas.offsetTop + y * scaleY}px`;
                        link.style.width = `${width * scaleX}px`;
                        link.style.height = `${height * scaleY}px`;
                        link.style.pointerEvents = 'auto';
                        container.appendChild(link);
                    }
                });
            });
        $('#prevPage').prop('disabled', currentPage === 1);
        $('#nextPage').prop('disabled', currentPage === totalPages);
    });
}

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

function open_close(idBloccoDaNonNascondere, titoloSlides, pathSlides) {
    const elementiBlocco = document.querySelectorAll('[id*="blocco"]');
    if (window.innerWidth > 981) {
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
    else{
        window.location.href = pathSlides;
    }
}