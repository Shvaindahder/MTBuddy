const formImg = document.querySelector('.registration__img');
const img = document.getElementsByClassName('registration__image')[0];
const formInput = document.getElementById('registration__file');
img.addEventListener('click', () => {
  console.log('click')
  formInput.click()
  formInput.addEventListener('change', previewFile, true)
  
})

// function dos() {
//   formInput.()
// }
// formInput.addEventListener('chenge', function onFileSelected(event) {
//   var selectedFile = event.target.files[0];
//   var reader = new FileReader();

//   // var imgtag = document.getElementById("myimage")
//   img.title = selectedFile.name;

//   reader.onload = function(event) {
//     img.src = event.target.result;
//   };

//   reader.readAsDataURL(selectedFile);
// })
// formImg.addEventListener('click', () => {
// console.log('click')
//   formInput.addEventListener('change', readURL, true);
  
// })


function previewFile() {

  var file    = formInput.files[0];
  var reader  = new FileReader();d

  reader.onloadend = function () {
    img.src = reader.result;
  }

  if (file) {
    reader.readAsDataURL(file);
  } else {
    preview.src = "";
  }
}


// var readFile = function(e) {
//   var input = e.target;

//   var reader = new FileReader();

//   reader.onload = function(){
//     var img = document.createElement('img');
//     img.src = reader.result;

//     var image = new fabric.Image(img);
//     canvas.add(image);
//   };

//   reader.readAsDataURL(input.files[0]);
// };

// formInput.addEventListener('change', readFile);

// var canvas = new fabric.Canvas(document.getElementById('canvas'), {
//   backgroundColor: '#c8c8c8'
// });