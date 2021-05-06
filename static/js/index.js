const header__sign = document.querySelector('.header__sign');
const link = document.querySelectorAll('a');
const popupBody = document.querySelector('.popup__body');
const logPopupBody = document.querySelector('.log__popup__body');
const log__popup__body = document.querySelector('.log__popup__body');
const login__popup = document.querySelector('.log-in__popup');
const header_log = document.querySelector('.header__log');
const popup = document.querySelector('.sign-in__popup');
const close = document.querySelector('.popup__close');
const logClose = document.querySelector('.log__popup__close');
const content = document.querySelector('.popup__content');
const logContent = document.querySelector('.log__popup__content');

for(let i = 0; i < link.length; i++) {
  link[i].addEventListener('click', (e) => {
    e.preventDefault()
  })
}
header_log.addEventListener('click', (e) => {
  // e.preventDefault()
  login__popup.classList.toggle('open')
  logContent.classList.toggle('content__open')
})
header__sign.addEventListener('click', (e) => {
  // e.preventDefault()
  popup.classList.toggle('open')
  content.classList.toggle('content__open')
})

close.addEventListener('click', () => {
  popup.classList.remove('open')
  content.classList.remove('content__open')
})

logClose.addEventListener('click', () => {
  login__popup.classList.remove('open')
  logContent.classList.remove('content__open')
})
content.addEventListener('click', e => {
  e.stopPropagation()
})

popupBody.addEventListener('click', () => {
  popup.classList.remove('open')
  content.classList.remove('content__open')
})
logPopupBody.addEventListener('click', () => {
  login__popup.classList.remove('open')
  logContent.classList.remove('content__open')
})

// header_log.addEventListener('click', (e) => {
//   e.preventDefault()
//   popup.classList.toggle('open')
//   content.classList.toggle('content__open')
// })

