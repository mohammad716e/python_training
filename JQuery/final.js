//  اسم پلیر ها رو بپرس و رنگ هاشون رو نسبت بده بهشون
// ---------------------------------------------------
// تعیین بازیکن اول
var player1 = prompt("player one: enter your name you will be blue")
var player1Color = 'rgb(86 ,151 ,255)'
// تعیین بازیکن دوم
var player2 = prompt("player two: enter your name you will be blue")
var player2Color = 'rgb(237 ,45 ,73)' 
// گداشتن یک بولیین برای تعیین در جریان بودن بازی
var game_on = true
// گرفتن جدول با جی کوعری
var table =$("table tr")
// ساخت تابعی که با لاگ دقیق بتونه برنده شدن رو گزارش کنه
function report_win(row_num,col_num) {
    console.log("بازیکن در این خانه با شماره ی سطون و سطر  به ترتیب برنده شده")
    console.log(col_num);
    console.log(row_num);
    
}
// ساخت تابعی که بتونه زنگ دکمه رو عوض کنه
// --------------------------------------
// این تابع میاد و رنگ + شماره سطر + شماره ی سطون  رو میگیره و رنگ و عوض میکنه
// در واقع فقط یلکتور هست با تغییر سی اس اس
function changeColor(rowIndex,colIndex,color) { // SELECT AND CHANGE CSS 
    return table.eq(rowIndex).eq(colIndex).find('button').css('background-color',color)
}
//  تابعی که بفمه رنگ دکمه چیه
// -------------------------
//  اینم فقط یک تابع هست که با داشتن شماره ی سطر وسطون به ما اعلام میکنه که رنگ اون خونه چیه فقط یک سی اس اس رو 
// به ما میگه و مثل بالایی هست
function reportColor(rowIndex,colIndex) { // SELECT AND CHANGE CSS 
    return table.eq(rowIndex).eq(colIndex).find('button').css('background-color')
}
// پیدا کردن این که نزدیک ترین خونه برای پر کردن توی هر سطون کدومه
// ---------------------------------------------------------
// چون خونه ها به صورتی پر میشن که انگار رنگ ها روی هم میافتن پس ما هم 
// از پایین شروع میکنیم رنگ ها رو نگاه میکنیکم تا به رنگ خالی یا همون خامستری برسیم
// در واقع به ما میفهمونه که آخرین جا کجاست


function checkBottom(colIndex){ // RETURN ROW IDX
    // حالا باید از پایین ترین خونه شروع کنیم به ریپورت گرفتن از رنگ ها برای و
    // اگر دیدیم که اکستری بود برگردونیمش
    var colorReports = reportColor(5,colIndex)
    // البته میتوانستیم یک استرینگ خالی برای این کار هم بگذاریم بجای صدا کردن فانکشن 
    // البته تا زمانیکه هست هم شاید یک بار کمتر شدا کنه فانکشن ریپورت رو
    // حالا حلقه
    for (var row = 5 ; row > -1 ; row-- ){
        colorReports = reportColor(row,colIndex)
        if (colorReports === 'rgb(128, 128, 128)') {
            return row
        }
    }
}
  
// تابعی برای برسی این که بردیم یا نه
// ---------------------------------
// یکی از شرایط برد این است که رنگ جهارخانه که انتخاب میشوند با هم برابر باشند 
// و خامستری نباشند و از بیرون جئول انتخاب نشوند یعنی undefined  نباشند

function colorMatchCheck(one,two,three,four){
    return (one===two && one === three && one === four && one !=='rgb(128, 128, 128)' && one !== undefined)
}
// تابعی که درست انتخاب بکنه خونه ها رو برای بررسی رنگی که برده ایم یا نه
// ---------------------------------------------------------------
// تابع برنده شدن افقی و عمودی که با حلقه هایی به آسانی قابل برسی هست
// برای افقی
function horizontalWinCheck() {
    // حلقه ی اولی که در هر سطر یک بار عوض میشه
    for(var row = 0; row < 6; row++){
        // حلقه ی دومی که در هر سطری که هستیم برای چهار تا خونه ی اول چک انجام میده
        // چون برای خونه ی پنجم چهار تا اونور ترش بیرون از جدول میافته
        for(var col=0 ; col<4;col++){
            // حالا در هر سطر که هستیم با جابجایی در خانه های اول چهارتا خانه ی بعدی رو چک میکنیم
            // col , col+1 , col+2 , col+3 
            // این سزون ها با همان سطر row 
            // یک رنگ میدهند 
            // این رنگ ها را به چک رنگ میدهیم که به ما درست یا غلط میدهد
            
            if(colorMatchCheck (reportColor(row,col ), reportColor(row,col+1) , reportColor(row,col+2) , reportColor(row,col+3))){
                console.log('افقی')
                report_win(row,col)
                return  true
            } else{
                continue
            }
        }
    }
}

// برای عمودی
function verticalWinCheck() {
    for(var col = 0 ; col <7 ; col++){
        for(var row = 0;row<3;row++){
            if(colorMatchCheck (reportColor(row,col ), reportColor(row+1,col) , reportColor(row+2,col) , reportColor(row+3,col))){
                console.log('عمودی')
                report_win(row,col)
                return  true
            }else{
                continue
            }
        }
    }
}
// برای مورب
// انتخاب خونه بهاین صورت هست
// ↳ ↘  برای مورب با حرکت i+1 , j+1
// ↲ ↙ برای مورب با حرکت i-1 , j+1
// حالا فقط میمونه چطوری بگیریم که بیرون نیافته از جدول
// میشه با دو حلقه نوشت و میشه با یه حلقه نوشت
// حال با خساب سختی که وجود داره میشه فهمید که 
// اگر 5 تا سطون بگیریم با هفت تا سطر همه ی مورب ها رو با یه حلقه چک کردیم
// نمیدونم خداییش ولی دو حلفه ای هم میشه
// ------------------------------------
// یک حلقه ای
function diagonalWinCheck() {
    for(var col=0 ; col<5;col++){
        for(var row=0;row<7;row++){
            if(colorMatchCheck (reportColor(row,col ), reportColor(row+1,col+1) , reportColor(row+2,col+2) , reportColor(row+3,col+3))){
                console.log('مورب مثبت ↘ ')
                report_win(row,col)
                return  true
            }else if(colorMatchCheck (reportColor(row,col ), reportColor(row-1,col+1) , reportColor(row-2,col+2) , reportColor(row-3,col+3))){
                console.log('مورب منفی ↙ ')
                report_win(row,col)
                return  true
            }else{
                continue
            }
        }
    }
}

// تابعی برای پیدا کردن انکه بازی تمام شده یا نه

// منطق بازی که با پلیر اول شروع میشه که پلیر ها بازی میکنند به نوبت و برنده مشخص میشه
// -----------------------------------------------------------------------------

// ما یک پلیر کونی در نظر میگیریم که باید تغییر کند و عوض شود به نوبت و با پلیر اول شروع میکنیم
var currentPlayer = 1
var currentName = player1
var currentColor =player1Color

// تغییر هدینگ در هر نوبت برا مشخص شدن نوبت هر پلیر
// البته فقط اینیشیعیت کردن  برای ماست و ما بجای خلقه ی
// while true با ایونت کلیک چک ها و غیره  وتعویض پلیر را انجام میدهیم

$('h3').text(player1+"نوبت شماست که بازی کنید و یک خانه انتخاب کنید")
// نوشتن ایونت لیسر برا ی کلیک ها
$(' button').on('click',function () {
    var col =$(this).closest('td').index()
    
    var bottomAvail = checkBottom(col)
    //  بردن را چک کن

    changeColor(bottomAvail,col,currentColor)
    if( horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck() ){
        $('h1').text( currentName+ 'شما برنده شده ایدس')
        $("h3").fadeOut('fast')
        $("h2").fadeOut('fast')
    }

    // پلیر را عوض کن
    currentPlayer = currentPlayer * -1
    //  ا استفاده از شماره ی پلیر آن را اساین کن

    if( currentPlayer ===1 ){
        currentName =player1
        $("h3").text(currentName+" نوب شماست")
        currentColor =player1Color
    }else{
        currentName =player2
        $("h3").text(currentName+" نوب شماست")
        currentColor =player2Color
    }
})

