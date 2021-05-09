const input = document.querySelector('.limit-int');
const button = document.querySelector('.limit-btn');
let flag = false;
let val = input.value;
button.style.wordWrap = 'nowrap'
button.addEventListener('click', () => {
  flag = !flag
  
  if(flag) {
    val = input.value;
    input.value = '';
    input.disabled = true;
    button.style.color = 'red';
  } else {
    input.disabled = false;
    input.value = val
    button.style.color = '#fff';
  }
  console.log(flag)
 
})