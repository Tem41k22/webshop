let searchClose = document.querySelector('.search_btn1')
let searchForm = document.querySelector('.search_logo')
let searchBtn = document.querySelector('.logo_btn')

searchBtn.addEventListener('click', function () {
    searchForm.style.display = 'flex'
})
searchClose.addEventListener('click', function (e) {
    e.preventDefault()
    searchForm.style.display = 'none'
})

let forms = document.querySelectorAll('.detail_form')
forms.forEach(function (form) {
    let quantity = form.querySelector('.detail_input')
    let minus = form.querySelector('.form_btn1')
    minus.addEventListener('click', function (e) {
        e.preventDefault()
        if (quantity.value <= 1) {
            return
        }
        quantity.value = +quantity.value - 1
    })
    let plus = form.querySelector('.form_btn')
    plus.addEventListener('click', function (e) {
        e.preventDefault()
        quantity.value = +quantity.value + 1
    })
    form.addEventListener('keydown', function (e) {
        if (e.key == 'Enter') {
            form.submit()
        }
    })
})