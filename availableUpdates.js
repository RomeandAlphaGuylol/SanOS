var fs = require("fs")

function updates(){
    var openit = fs.open("changes_on_branch.json");
    console.log(openit);
}
updates();


