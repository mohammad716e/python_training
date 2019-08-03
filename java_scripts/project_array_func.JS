var things = []

// این یک تابع است که میخواهد یک اسم به آرایه اضافه کند

function addNew() {
    thing = prompt("چه اسمی را میخواهید اضافه کنید")
    things.push(thing)
}

// این یک تابع است که اسم مورد نظر  ما را سرچ میکند و در صورت یافتن آن را از آرایه
// پاک میکند

function remove(){
    remName = prompt( " چه اسمی را میخواهید پاک کنید")
    remIndex = things.indexOf(remName)
    
    things.splice( remIndex , 1 )
    // این متد از یک ایندکس شروع میکند وبه تغداد داده شده که در اینجا یک عدد است از آرایه
    // حذف میکند اول خود آن ایندکس است و بعد جلویی های آن
}

// این تابع فقط آرایه ی اشیا را نشان میدهد

function display() {
    console.log(things);
    
}



// و حالا حلقه ی اصلی برنامه را مینویسیم

var start = prompt(" آیا میخواهید که برنامه ی خیره ی اشیا را استفاده کنید"
+"\n "+" برای بله Y" +" برای خیر N ")

var request = "empty"

if (start.toLowerCase() === "y"){

    while( request != "q"){
        request = prompt(" برای کار با برنامه لطفا انتخاب کنید"
        +"\n "+" برای  حذف کردن R" +" برای اضافه کردن A"  +" برای خارج شدن  Q" +" برای مشاهده کردن D")


        if (request == "a") {
            addNew()
        }else if (request == "r"){
            remove()
        }else if (request == "d"){
            display()
        }







    }
}