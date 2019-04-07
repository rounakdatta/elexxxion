const fs = require('fs');

var obj;
var filePath = './data/wb_2014_constituency_2.json';
var writePath = './data/constituencies2014URL';
var writePathComparison = './data/constituenciesComparison2014URL';

// the constituency information (not so tabulated)
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
            });
        }
    }

});

// the tabulated candidate comparison information
fs.writeFile(writePathComparison, "", function(err) {
    console.log(err);
});

fs.readFile(filePath, 'utf8', function (err, data) {
    if (err) throw err;
    obj = JSON.parse(data);

    for (var foo in obj) {
        for (var bar in obj[foo]) {
            let consURL = obj[foo][bar]['url'].replace("index.php?action=show_candidates&", "comparisonchart.php?") + "^" + obj[foo][bar]['data'] + '\n';
            fs.appendFile(writePathComparison, consURL, function(err) {
            });
        }
    }

});