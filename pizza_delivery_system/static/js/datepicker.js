var date = new Date();
var dateToday = new Date(date.getFullYear(), date.getMonth() + 1, 0);
$('input.datepicker1').datepicker(
{
			dateFormat : "mm-dd-yy",
			changeMonth : true,
			changeYear : true,
			yearRange : "-100:+nn",
			minDate : null,
			maxDate : null,
			onSelect : function(selected) {
				$('input.datepicker2').datepicker("option", "minDate",
						$("input.datepicker1").datepicker('getDate'))
			}
		});

$('input.datepicker2').datepicker({
	dateFormat : "mm-dd-yy",
	changeMonth : true,
	changeYear : true,
	yearRange : "-100:+nn",
	minDate : null,
	maxDate : null,
});

$('input.datepicker3').datepicker({
	dateFormat : "mm-dd-yy",
	changeYear : true,
	changeMonth : true,
	yearRange : "-100:+20",
	minDate : '0'
});