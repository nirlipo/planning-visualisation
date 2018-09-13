var DownloaderPlugin ={
    Download : function(textptr, fileTypeptr,fileNameptr) {
    var text = Pointer_stringify(textptr);
    var fileType = Pointer_stringify(fileTypeptr);
    var fileName = Pointer_stringify(fileNameptr);
    var blob = new Blob([text], { type: fileType });

    var a = document.createElement('a');
    a.download = fileName;
    a.href = URL.createObjectURL(blob);
    a.dataset.downloadurl = [fileType, a.download, a.href].join(':');
    a.style.display = "none";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(function() { URL.revokeObjectURL(a.href); }, 1500);
    }
};
mergeInto(LibraryManager.library, DownloaderPlugin);