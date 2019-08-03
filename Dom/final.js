var btn_reset = document.querySelector(".btn")
var all_td = document.querySelectorAll("td")
btn_reset.addEventListener("click",function () {
    all_td.forEach(element => {
        element.innerText =""
    });
})

all_td.forEach(element => {
    element.addEventListener("click",function () {
        
        if (element.textContent == ""){
            element.textContent = "O"
        }else if ( element.textContent == "O"){
            element.textContent = "X"
        }else {
            element.textContent = ""
        }
    })
});