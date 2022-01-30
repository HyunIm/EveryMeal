$(function(){
    const WEEK_DAY = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    let today = new Date();
    let weekday = WEEK_DAY[today.getDay()];
    $("#menu").attr("src", "image/" + weekday + ".jpg");
});
