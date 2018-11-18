$(function () {
	   ImageLoadEx();
});

function ImageLoadEx() {
	   $('img').error(function () {
	       $(this).attr("src", "static/3/images/bk.jpg");
	   });
}