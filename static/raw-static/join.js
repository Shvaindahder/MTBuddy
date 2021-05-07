const json = [
  {"title": "first", "when": "today", "where": "London", "skill": "middle", "notes": "nth"},
  {"title": "first", "when": "today", "where": "New-York", "skill": "senior", "notes": "nth"},
  {"title": "first", "when": "today", "where": "Los-Angeles", "skill": "junior", "notes": "nth"},
  {"title": "first", "when": "today", "where": "Moscow", "skill": "middle", "notes": "nth"},
  {"title": "first", "when": "today", "where": "Paris", "skill": "senior", "notes": "nth"},
  {"title": "first", "when": "today", "where": "Berlin", "skill": "junior", "notes": "nth"},
  {"title": "first", "when": "today", "where": "Sidney", "skill": "senior", "notes": "nth"}
]
const btn = document.querySelector('.join__btn');
alert(window.innerWidth)

// btn.addEventListener('click', () => {
//   html = 
//   json.map(item => (
  
//     `
//     <div>${item.title}</div>
//     `
//   ))
// })


const show = () => {
const el = document.createElement('div') 
el.innerHTML = json.map(item => {
  return (
    `
    <div>
      <p>${item.title}</p>
      <p>${item.skill}</p>
      <p>${item.title}</p>
    </div>
    `
  )
})
document.body.appendChild(el)
}

btn.addEventListener('click', show)
