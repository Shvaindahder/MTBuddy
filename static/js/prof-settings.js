
const img = document.getElementsByClassName('psf__img')[0];
const image = document.getElementById('psf__image');
const formInput = document.getElementById('profile-settings__avatar');

img.addEventListener('click', () => {
  console.log('click')
  formInput.click()
  formInput.addEventListener('change', previewFile, true)
  
})


function previewFile() {

  var file    = formInput.files[0];
  var reader  = new FileReader();

  reader.onloadend = function () {
    image.src = reader.result;
  }

  if (file) {
    reader.readAsDataURL(file);
  } else {
    preview.src = "";
  }
}

