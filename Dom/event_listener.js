headone = document.querySelector("#one")
headtwo = document.querySelector("#two")
headthree = document.querySelector("#three")

headone.addEventListener("mouseover",function(){
    headone.style.color ="red"
    headone.textContent = "شما موس را در اینجا نگه داشتید"
})

headone.addEventListener("mouseout",function(){
    headone.textContent= " موس را روی من نگاه دارید"
    headone.style.color="black"
})

headtwo.addEventListener("click",function(){
    headtwo.textContent = "شما در اینجا کلیک کردید"
    headtwo.style.color = "blue"
})

headthree.addEventListener("dblclick",function () {
    headthree.textContent =" شما در اینجا دابل کلیک کردید"
    headthree.style.color ="green"
})