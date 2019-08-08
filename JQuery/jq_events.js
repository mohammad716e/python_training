// تست جی کوعری و جاوا اسکریپت
// console.log("متصل شده");
var h = $('h1')

h.click( function( ){
    h.css('color', 'green' )
    $(this).css('background','lightgreen')
    $(this).text('تمرین ')

})
// برای هر ایونتی میتوان از this استفاده کرد
$('li').click(function(){
    $(this).css('background','lightgreen')
    console.log(" یک li کلیک شد");
    // li های نست شده در همدیگر دوبار کلیک محسوب میشوند

    
})
// میتوان از keypress هم در جی کوعری استفاده کرد
var i =$('input').eq(0)
i.addClass('col-lg-7')
i.val('با هر دکمه در اینپوت رنگ h3 تغییر میکند')
i.keypress( function(evnt){
    
    if (evnt.which === 13) {
        $('h3').toggleClass('turnred')
    }else{
        $('h3').removeClass('turnred')
        $('h3').toggleClass('turnblue')
    }


    console.log(evnt);
    
})
// این اولین فانکشنی است که به کلیک پاس میدهیم ولی همیشه فانکشن های پاس شده به به کلیک یا هر نوع ایونتی click()
// دارای یک متغییر دیفالت هستند که مثلا  ایونت مینامیم اش
// که برای خود یک آبجکت تمام عیار هستند که در کسول میتوان دید


h.on('dblclick', function(){
    h.text('تمرین جی کوعری ')
    $('h6').text(' (حالا شد XD) ')
})

// استفاده از متد on
$('h6').on('mouseenter', function () {
    $(this).text("( کلیک و  یا دابل کلیک کنید)")
})

// استفاده از انیمیشن

// برای fade کردن

$('input').eq(1).on('click', function(){
    $('.container').fadeOut(3000)
})

$("body").on('click',function(){
    $('.container').fadeIn(3000)
})

// برای اسلاید کردن

// $('input').eq(1).on('click', function(){
//     // slideUp کار نمیکنه
//     $('.container').slideToggle(3000)
// })
// $("body").on('click',function(){
//     $('.container').slideToggle(3000)
// })