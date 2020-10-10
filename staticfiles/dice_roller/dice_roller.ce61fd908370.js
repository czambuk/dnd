$(document).ready(function () {
    $('#id_roll_data').on('click', function () {
        $(this).val('');
    });

    var $allowedDice = [4, 6, 8, 10, 12, 20, 100];

    function getRandomNumber(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    function addResults(a, b) {
        return a + b;
    }

    $('.roll-button').on('click', function () {
        var $throwData = $('textarea').val(),
            $dieCode, $dieSize, $throwNumberCode, $throwNumber, $modCode, $modValue;
        if ($throwData !== null) {
            if ($throwData.match(/k\d*/) != null) {
                $dieCode = $throwData.match(/k\d*/)[0]
            } else {
                $dieCode = 0
            }

            if ($dieCode.match(/\d+/) != null) {
                $dieSize = $dieCode.match(/\d+/)[0]
            } else {
                $dieSize = 0
            }

            if ($throwData.match(/\d*k/) != null) {
                $throwNumberCode = $throwData.match(/\d*k/)[0]
            } else {
                $throwNumberCode = 0
            }

            if ($throwNumberCode.match(/\d+/) != null) {
                $throwNumber = $throwNumberCode.match(/\d+/)[0]
            } else {
                $throwNumber = 0
            }

            if ($throwData.match(/\+\d*/) != null) {
                $modCode = $throwData.match(/\+\d*/)[0]
            } else {
                $modCode = 0
            }

            if ($modCode.match(/\d+/) != null) {
                $modValue = $modCode.match(/\d+/)[0]
            } else {
                $modValue = 0
            }
        } else {
            $throwData = 0
        }

        console.log("$throwData = " + $throwData);
        console.log("$dieCode = " + $dieCode);
        console.log("$dieSize = " + $dieSize);
        console.log("$throwNumberCode = " + $throwNumberCode);
        console.log("$throwNumber = " + $throwNumber);
        console.log("$modCode = " + $modCode);
        console.log("$modValue = " + $modValue);

        if ($allowedDice.includes(parseInt($dieSize)) === true) {
            var singleResults = [];
            for (i = 0; i < $throwNumber; i++) {
                var randomNumber = getRandomNumber(1, $dieSize);
                singleResults.push(randomNumber);
            }

            var $result = singleResults.reduce(addResults, 0) + parseInt($modValue);
            var singleResultsString = singleResults.toString();

        } else {
            $result = "Błędna kostka!"
        }

        $('.results').prepend('<p>Losowanie: ' + $throwData + ', Wylosowano: ' + '[' + singleResultsString + '] ' +
            '+' + $modValue + ' => ' + $result + '</p>');
    });
});