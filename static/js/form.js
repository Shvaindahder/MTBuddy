const formImg = document.querySelector('.registration__img');
const img = document.getElementsByClassName('registration__image')[0];
const formInput = document.getElementById('registration__file');

img.addEventListener('click', () => {
  console.log('click')
  formInput.click()
  formInput.addEventListener('change', previewFile, true)
  
})


function previewFile() {

  var file    = formInput.files[0];
  var reader  = new FileReader();

  reader.onloadend = function () {
    img.src = reader.result;
  }

  if (file) {
    reader.readAsDataURL(file);
  } else {
    preview.src = "";
  }
}

