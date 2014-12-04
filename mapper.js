/**
 * Created by f333 on 04/12/14.
 */
function mapper() {
    var words;
    words = this.text.match(/\w+/g);
    if (words == null)
        return;
    else
        for (var i = 0; i < words.length; i++) {
            emit(words[i], {count: 1})
        }
}