alert("hello")
// object Iterator
var obj ={
    type:"ماشین",
    name:"تویوتا",
    model:"کمری",
    color:"قهوه ای ",

}

var obj_key_persian ={
    type:"نوع",
    name:"اسم",
    model:"مدل",
    color:"رنگ ",

}

//  کار نمیکند
// for (k , j in obj , obj_key_persian){
//     console.log(boj_key_persian[j])
//     console.log(obj[k])
    
// }
for(k in obj) {
    console.log(obj_key_persian[k]+" :");
    console.log(obj[k]);
    console.log("------------------");
}
// و این هم نحوه ی شماردن دو آبچکتهمزمان در جاوا اسکریپت
var b = {
    name :" محمد ",
    greet: function () {
        console.log(" سلام "+this.name);
        
    }
}