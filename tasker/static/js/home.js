
$(function () {

    // about app read more or less toggling
    $('#aboutApp > p:gt(0)').hide();

    $("#readMoreBtn").on('click', function () {
        $("#aboutApp > p:gt(0)").slideToggle(500);

    });

    // the latest post animation
    $("#postCard").hide().show(500).addClass('recent-post');
});
