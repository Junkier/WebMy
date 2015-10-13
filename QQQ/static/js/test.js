$(document).ready(function(){
	
	$.get('http://localhost:8000',function(data){
		alert(data);
	});
	
/* 	$.post('http://localhost:8000',
	{	
		name:'QQAAAA',
		number:'211gdfgdgdg111'
	},
	function(data){
		$('#Name').text(data['name']);
		$('#Job').text(data['number']);
	}) */
	
	$('button').click(function(){
		$.post('http://localhost:8000',
		{	
		'Empno':$('input').val()
		},
		function(data){
		$('#Name').text(data['ename']);
		$('#Job').text(data['Job']);
		$('#Sal').text(data['Sal']);
		$('textarea').text(data['empno']+ ',' + data['Comm'])
		})

	});
});