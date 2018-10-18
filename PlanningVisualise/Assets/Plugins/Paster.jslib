mergeInto(LibraryManager.library, {
 
 
  PasteHereWindow: function () {
    var pastedtext= prompt("Please paste here:", "");
    SendMessage("Canvas", "GetPastedText", pastedtext);
  },
 
});