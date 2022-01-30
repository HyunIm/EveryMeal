$(function() {
    set_daily_menu();
    set_date();
});

function set_daily_menu() {
    const WEEK_DAY = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    let today = new Date();
    let weekday = WEEK_DAY[today.getDay()];
    
    $("#menu").attr("src", "image/" + weekday + ".jpg");
}

function set_date() {
    const WEEK_DAY_KOR = ['일', '월', '화', '수', '목', '금', '토']
    let today = new Date();
    let month = today.getMonth() + 1;
    let date = today.getDate();
    let day = WEEK_DAY_KOR[today.getDay()];

    $("#todayDate").text(month + "월 " + date + "일 (" + day + ")")
}
