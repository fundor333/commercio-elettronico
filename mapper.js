function mapper() {
    var documenti = this.documenti;
    if (documenti) {
        // quick lowercase to normalize per your requirements
        documenti = documenti.toLowerCase().split(" ");
        for (var i = documenti.length - 1; i >= 0; i--) {
            // might want to remove punctuation, etc. here
            if (documenti[i]) {      // make sure there's something
                emit(documenti[i], 1); // store a 1 for each word
            }
        }
    }
}