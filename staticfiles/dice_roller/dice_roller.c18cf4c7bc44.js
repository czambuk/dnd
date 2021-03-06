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

    $('.main-input-button').on('click', function () {
        var $throwData = $('textarea').val()
        $dieCode = $throwData.match(/k\d*/)[0]
        $dieSize = $dieCode.match(/\d+/)[0]
        $throwNumberCode = $throwData.match(/\d*k/)[0]
        $throwNumber = $throwNumberCode.match(/\d+/)[0]
        $modCode = $throwData.match(/\+\d*/)[0]
        $modValue = $modCode.match(/\d+/)[0];

        if ($allowedDice.includes(parseInt($dieSize)) === true) {
            var singleResults = [];
//            if ($modCode == null) {
//                $modValue = 0;
//            } else {
//                $modValue = $modValue;
//            };
//            if ($throwNumberCode == null) {
//                $throwNumber = 0;
//            } else {
//                $throwNumber = $throwNumber;
//            };
            for (i = 0; i < $throwNumber; i++) {
                var randomNumber = getRandomNumber(1, $dieSize);
                singleResults.push(randomNumber);
            }

            var $result = singleResults.reduce(addResults, 0) + parseInt($modValue);
            var singleResultsString = singleResults.toString()

        } else {
            $result = "Błędna kostka!"
        }

        $('.results').prepend('<p>Losowanie: ' + $throwData + ', Wylosowano: ' + '[' + singleResultsString + '] ' +
            '+' + $modValue + ' => ' + $result + '</p>');
    });
});