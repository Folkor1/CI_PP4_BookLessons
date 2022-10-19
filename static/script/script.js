$(document).ready(function() {

    let pianoOrTheory = document.getElementById("piano-or-theory");
    let onlineorOffline = document.getElementById("online-or-offline");
    let lesson = document.getElementById("lesson-confirmation");
    let lessonType = document.getElementById("lesson-type-confirmation");
    let selectDate = document.getElementById("date-confirmation");
    let selectTime = document.getElementById("time-confirmation");
    let booking = [];
    let date = [];
    let time = [];

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
        onlineorOffline.innerText = "";
    });

    // Back to lesson type selection
    $("#back-lesson-type").on("click", function() {
        $("#calendar").addClass("d-none");
        $("#select-lesson-type").removeClass("d-none");
        $("#select-date").addClass("d-none");
        $("#oo-buttons").removeClass("d-none");
        $('#online').addClass("d-none");
        $('#offline').addClass("d-none");
        booking.splice(booking.indexOf('Online', 'Offline'),1);
        onlineorOffline.innerText = "";
    });

    // Display time picker once date is selected
    $('#date').datepicker().on('changeDate', function() {
    $('#time-picker').removeClass('d-none');
    });

    // Display Book button once time is selected
    $('#time-picker').change(function() {
    $('#book-div').removeClass('d-none');
    time.splice(0);
    var selectedTime = $("#time-picker option:selected").text();
    time.push(selectedTime);
    });

    // Pop-up on hover window
    $(function() {
        var moveLeft = 20;
        var moveDown = 10;
     
        $('a.trigger').hover(function() {
          $('div#pop-up').show();
        }, function() {
          $('div#pop-up').hide();
        });
     
        $('a.trigger').mousemove(function(e) {
          $("div#pop-up").css('top', e.pageY + moveDown).css('left', e.pageX + moveLeft);
        });
      });

    // Get date from the calendar
    $('#date').datepicker().on('changeDate', function (selectedDate) {
        date.splice(0);
        selectedDate = selectedDate.date.toLocaleDateString('en-CA');
        date.push(selectedDate);
        });
    
      // Get selections lesson types from booking menus
      function getLesson() {
        lesson.innerText = booking[0];
        document.getElementById('lesson_inp').value = booking[0];
      };

});