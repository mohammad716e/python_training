var  v = document.querySelector("h1")
function set_color (color){
    v.style.color=color
}
function set_bg_color(color){
    v.style.backgroundColor=color
}

function random_color(){
    hex_colors_array = "012345689abcdef"
    // برای انتخاب از بین 1 تا 16 باید درصد را در 16 ضرب کنیم
    // و آن عددی بین ضفر تا یک است
    // که از Math.random() با حرف اول بزرگ حساب میشود
    color_random="#"
    for (var i=0 ; i<6;i++){
    generate_random_index = Math.floor(Math.random()*16)
    color_letter = hex_colors_array[generate_random_index]
    color_random +=color_letter
    // به اضافه یک متد استرینگ در جاوا اسکریپت است
    }
    return color_random
}
function do_chenge_color(){
    var k= random_color()
    set_color(k)
    var j = random_color()
    set_bg_color(j)
}

setInterval("do_chenge_color()",500)