var file;
var fileReader = new FileReader();
count= 0;showPic = false;

function doFirst(){
	var movingButton = document.getElementById('movingButton');
	var Body = document.getElementById('Body');
	var Site = document.getElementById('Site');
	var pictureButton = document.getElementById('pictureButton');
	var signalButton = document.getElementById('signalButton');
	var myCakeA = document.getElementById('myCakeA');
	

	signalButton.onmouseover = shining;
	signalButton.onmouseout = shiningBack;
	Site.onclick = turnLight;
	pictureButton.onclick = showPicture;
	pictureButton.ondblclick = backPicture;
	movingButton.onmouseover = Hover;
	movingButton.onmouseout = hoverBack;
}

function hoverBack(){
	if(!showPic){
	pictureButton.style.width=255+ 'px';
	movingButton.style.width=10 + 'px';
	pictureButton.style.color='#666';
	
	}
	
	shiningBack();
}

function Hover(){
	
	if(!showPic){
	pictureButton.style.width=520+ 'px';
	movingButton.style.width=520 + 'px';
	pictureButton.style.color='#aaa';
	}
	
	
	
	shining();
}

function backPicture(){
	
	myCakeA.style.opacity='0';
	Sleep(this,1200); 
	this.NextStep=function() { 
	myCakeA.src='';  
    pictureButton.style.height=70 + 'px';
	pictureButton.style.backgroundColor= '';
	showPic = false;
	}

}


function showPicture(){
	showPic = true;
	pictureButton.style.width=520 + 'px';
	pictureButton.style.height=580 + 'px';
	pictureButton.style.backgroundColor= '#ddeeee';
	movingButton.style.width=520 + 'px';
	pictureButton.style.color='#fa2';
    myCakeA.src='Cake2.jpg';
	Sleep(this,1000); 
	this.NextStep=function() { 
	myCakeA.style.opacity='1';}
	
}

function shiningBack(){
	signalButton.style.backgroundColor='#86c2f4';

}

function shining(){
	signalButton.style.backgroundColor='#9fdfff';

}

function turnLight(){
	if(count ==0){
	Body.style.background='#000';
    Site.style.backgroundColor='#666';
	pictureButton.style.color='#aaa';
	count = 1;
	} else{
    Body.style.background='#666';
    Site.style.backgroundColor='#aaa';
	pictureButton.style.color='#666';
	count = 0;
	}
	
}



window.addEventListener('load',doFirst,false);
