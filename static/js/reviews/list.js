var modal = document.getElementById("myModal");

var btn = document.getElementById("add-review");

var span = document.getElementsByClassName("close")[0];
btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.taget == modal) {
        modal.style.display = "none";
    }
}

// document.addEventListener('DOMContentLoaded', function () {
//     var form = document.getElementById('review-form');
//     form.addEventListener('submit', function () {
//         form.reset();
//     })
// }
// )