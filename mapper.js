function mapper() {
    var body = this.body;
    if (body) {
        body = body.toLowerCase().split(" ");
        for (var i = body.length - 1; i >= 0; i--) {
            if (body[i]) {
                emit(body[i], 1);
            }
        }
    }
}