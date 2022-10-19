$(document).ready(function() {

    let pianoOrTheory = document.getElementById("piano-or-theory");
    let onlineorOffline = document.getElementById("online-or-offline");

    let booking = [];

    // Change lesson type options when clicked
    $("#piano-btn").on("click", function() {
        $("#piano-theory").addClass("d-none");
        $("#book-for").removeClass("d-none");
        $("#select-lesson-type").removeClass("d-none");
        $("#oo-buttons").removeClass("d-none");
        booking.push('Piano');
        pianoOrTheory.innerText = booking[0];
    });

    $("#theory-btn").on("click", function() {
        $("#piano-theory").addClass("d-none");
        $("#book-for").removeClass("d-none");
        $("#select-lesson-type").removeClass("d-none");
        $("#oo-buttons").removeClass("d-none");
        $("#theory").removeClass("d-none");
        booking.push('Theory');
        pianoOrTheory.innerText = booking[0];
    });

    // Change online/offline options when clicked
    $("#online-btn").on("click", function() {
        $("#select-lesson-type").addClass("d-none");
        $("#oo-buttons").addClass("d-none");
        $("#select-date").removeClass("d-none");
        $("#calendar").removeClass("d-none");
        $('#online').removeClass("d-none");
        booking.push('Online');
        onlineorOffline.innerText = booking[1];
    });

    $("#offline-btn").on("click", function() {
        $("#select-lesson-type").addClass("d-none");
        $("#oo-buttons").addClass("d-none");
        $("#select-date").removeClass("d-none");
        $("#calendar").removeClass("d-none");
        $('#offline').removeClass("d-none");
        booking.push('Offline');
        onlineorOffline.innerText = booking[1];
    });

    // Back to lesson selection
    $("#back-lesson").on("click", function() {
        $("#select-lesson-type").addClass("d-none");
        $("#piano-theory").removeClass("d-none");
        $("#book-for").addClass("d-none");
        $("#oo-buttons").addClass("d-none");
        $("#piano").addClass("d-none");
        $("#theory").addClass("d-none");
        booking.splice(booking.indexOf('Piano', 'Theory'),1);
    });

});