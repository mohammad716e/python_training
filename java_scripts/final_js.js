var person = {
    name:"جان اسمیت",
    job:"طراح وب",
    age:21,
    report: function(){
        console.log("سلام اسم من "+this.name+" هست و شغل من "+this.job+" میباشد وسن من "+ this.age + " است ");
        
    },
    say_last_name: function (){
        console.log( this.name.split( " ")[1] )
    },
    say_name_length: function(){
        console.log(this.name.length);
        
    }
}
