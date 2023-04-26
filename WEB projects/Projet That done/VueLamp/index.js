const myInput = document.querySelector("[data-input]")
const lightOfLamp = document.querySelector("[light-data]")
console.log(lightOfLamp)
myInput.checked = true;
myInput.addEventListener('click', e =>{
    if(myInput.value == 'off'){
        myInput.value = 'on'
        lightOfLamp.classList.remove('hidden')
        console.log(lightOfLamp)
    }else{
        myInput.value = 'off'
        lightOfLamp.classList.add('hidden')
        console.log(lightOfLamp)
    }
})
