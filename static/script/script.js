$(document).ready(function() {

    let pianoOrTheory = document.getElementById("piano-or-theory");
    let onlineorOffline = document.getElementById("online-or-offline");
    let lesson = document.getElementById("lesson-confirmation");
    let lessonType = document.getElementById("lesson-type-confirmation");
    let selectDate = document.getElementById("date-confirmation");
    let selectTime = document.getElementById("time-confirmation");
    let editDateDate = document.getElementById("edit-date-date");
    let editDateTime = document.getElementById("edit-time");
    let editLessonType = document.getElementById("edit_lesson_type");
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

    function getLessonType() {
        lessonType.innerText = booking[1];
        document.getElementById('lesson_type_inp').value = booking[1];
    };

    function getDate() {
        selectDate.innerText = date[0];
        document.getElementById('date_inp').value = date[0];
    };

    // Get time from time picker
    function getTime() {
        selectTime.innerText = time[0];
        document.getElementById('time_inp').value = time[0];
    };

    // Booking confirmation message
    $('#book-confirm').on("click", function() {
        $('#confirm-message').removeClass('d-none');
        $('#calendar').addClass('d-none');
        $('#select-date').addClass('d-none');
        $('#book-for').addClass('d-none');
        getLesson();
        getLessonType();
        getDate();
        getTime();
    });

    // Confirmation message - back button
    $('#back-to-selection').on("click", function() {
        $('#confirm-message').addClass('d-none');
        $('#calendar').removeClass('d-none');
        $('#select-date').removeClass('d-none');
        $('#book-for').removeClass('d-none');
    });

    // Timeout for alert messages
    setTimeout(function () {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 2500);

    // Display status of bookings
    if($('#upc-book, #upc-manage-book').is(':contains("|")')) {
        $('.upc-lessons').text("My upcoming bookings:");
    }

    // Edit date confirmation message
    $('#edit-book-confirm').on("click", function() {
        $('#edit-date-time').addClass('d-none');
        $('#edit-date-form').removeClass('d-none');
        getDateDate();
        getDateTime();
    });

    // Edit date - back button
    $('#edit-date-back-to-selection').on("click", function() {
        $('#edit-date-form').addClass('d-none');
        $('#edit-date-time').removeClass('d-none');
    });

    // Get date from date picker on edit
    function getDateDate() {
        editDateDate.innerText = date[0];
        document.getElementById('edit_date_inp').value = date[0];
    };

    // Get time from time picker on edit
    function getDateTime() {
        editDateTime.innerText = time[0];
        document.getElementById('edit_time_inp').value = time[0];
    };

    // Get lesson type on edit
    $('#edit-lesson-type-confirm').on("click", function() {
        if($("#edit_type_value").is(':contains("Online")')) {
            editLessonType.value = 'Online'
        } else {
            editLessonType.value = 'Offline'
        }
    });

    // Hide paginator
    if (document.location.pathname == "/past_bookings/") {
        if($('.card-body').length < document.getElementById("count").value) {
            $('#pag').addClass("d-none");
        }
     }

    // Hide admin panel buttons and display completed lessons
    $('#completed-lessons').on("click", function() {
        $('#admin-panel-p').addClass('d-none');
        $('#admin-buttons-div').addClass('d-none');
        $('#admin-stats-div').addClass('d-none');
        $('#completed-lessons-p').removeClass('d-none');
        $('#admin-filter').removeClass('d-none');
    });

});