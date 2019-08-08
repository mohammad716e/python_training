console.log('hello');
var lists = $('li')
lists.css('color','darkgreen')
lists.css('background','lightgreen')
lists.css('padding','0 7px 3px 0')
lists.eq(0).css('color','blue')
lists.eq(-1).css('color','red')
$('h1').text('جی کوعری این متن را تغییر داده است')
// $('h1').html('<strong><em> این متن برای بار دوم با جی گوعری تغییر کرده است و بلد شده است </em></strong>')
var inp = $('input')
inp.eq(1).val('این دکمه هم به دستور جی کوعری تغییر کرد')
inp.eq(0).attr('type','checkbox')

var h =$('h1')
// برای اضافه کردن کلاس addClass
h.addClass('turnred')
// برای حذف کردن کلاس removeClass
h.removeClass('turnred')
// برای کلاس را حذف کردن و اضافه کردن مثل کلید روشن و خاموش  از togglrClass
h.toggleClass('turnred')
h.toggleClass('turnred')
h.toggleClass('turnred')
h.css('padding','0 7px 9px 0')
$('ul').eq(0).css('background','green')