let form = document.querySelector('.det_form')
let quantity = form.querySelector('#quantityInp')
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