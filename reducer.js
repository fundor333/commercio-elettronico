/**
 * Created by f333 on 04/12/14.
 */

function reducer() {
    var total = 0;
    for (var i = 0; i < value.length; i++) {
        total += value[i].count;
    }

    return{count: total}
}