const modal = document.getElementById("myModal");

const btn = document.getElementById("add-review");

const span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "flex";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.taget == modal) {
        modal.style.display = "none";
    }
}