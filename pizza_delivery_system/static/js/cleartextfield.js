$(".reset").click(function() {
    		$(this).closest('form').find("input[type=text],textarea,select").val("");
    		$('input:checkbox').removeAttr('checked');
  
});

	

$(".clear").click(function() {
	$(this).closest('form').find("input[type=text],textarea,select").val("");
	$('input:checkbox').removeAttr('checked');
	$('#resetform').submit();

});


