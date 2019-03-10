const fs = require('fs');

var obj;
var filePath = './data/wb_2011_assembly_2.json';
var writePath = './data/constituencies2011URL';

fs.writeFile(writePath, "", function(err) {
    console.log(err);
});

fs.readFile(filePath, 'utf8', function (err, data) {
    if (err) throw err;
    obj = JSON.parse(data);

    for (var foo in obj) {
        for (var bar in obj[foo]) {
            let consURL = obj[foo][bar]['url'] + "^" + obj[foo][bar]['data'] + '\n';
            fs.appendFile(writePath, consURL, function(err) {
            })
        }
    }

});