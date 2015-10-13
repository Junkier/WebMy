$(document).ready(function(){
	/*  $.get('http://localhost:8000/',function(source_code){	
	 
	 
	})  */
	
	/* $('#Title').load('http://localhost:8000/'); */
	 $('#searchButton').click(function(){
		 
		$.get('http://localhost:8000/',function(data){
			
		var message = ''; 
		
		for(var num in data){
			message += data[num] +'\n';
		}
		
		$('#showArea').text(message);
	
	}) 
		 
		 
		 
		 
		 
	 });
	 
	
	/*  $('.topBar').load('http://localhost:8000/');  */
	/* alert('QQ');
	var SS  = {{excuse}};
	alert(SS);
	 */
	
});