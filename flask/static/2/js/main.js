const container = document.getElementById('avatar-container');
const avater = document.getElementById('avatar');

container.ondragover = function() {
	this.className = 'avatar-container-hover';
	return false;
}

container.ondragend = function() {
	this.className = 'avatar-container';
	return false;
}

container.ondrop = function (e) {
	this.className = 'avatar-container';
	e.preventDefault();
	const file = e.dataTransfer.files[0];
	if (file.type == 'image/png' || file.type == 'image/jpg' || file.type == 'image/jpeg') {
		avatar.src = URL.createObjectURL(file);
	}
	else {
		var warning = "您似乎上传的不是一张照片呢(*^_^*)，重新上传一张叭"
		alert(warning);
		console.log(file.type);
	}
}

window.container = container;

reUpload = function () {
	avatar.src = 'static/2/pic/patch.png';
}