var DownloaderPlugin = {
    Download: function(text, fileType, fileName) {
        var textPtr = Pointer_stringify(text);
        var fileTypePtr = Pointer_stringify(fileType);
        var fileNamePtr = Pointer_stringify(fileName);

        var blob = new Blob([textPtr], { type: fileTypePtr });

        var a = document.createElement('a');
        a.download = fileNamePtr;
        a.href = URL.createObjectURL(blob);
        a.dataset.downloadurl = [fileTypePtr, a.download, a.href].join(':');
        a.style.display = "none";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        setTimeout(function() { URL.revokeObjectURL(a.href); }, 1500);
        }
};
mergeInto(LibraryManager.library, DownloaderPlugin);