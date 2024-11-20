let pdfUrl = null;
let pdfDoc = null;
let currentPage = 1;
let totalPages = 0;

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

        // Aggiorna lo stato dei pulsanti di navigazione
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

function open_close(id) {
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
}