$(document).ready(function() {
    $('#id_roll_data').on('click', function() {
        $(this).val('');
    });

    var $allowedDice = [4, 6, 8, 10, 12, 20, 100];

    function getRandomNumber(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1)) + min;
    };

    $('.main-input-button').on('click', function() {
         var $throwData = $('input:text').val()
             $dieCode = $throwData.match(/k\d*/)[0]
             $dieSize = $dieCode.match(/\d+/)[0]
             $throwNumberCode = $throwData.match(/\d*k/)[0]
             $throwNumber = $throwNumberCode.match(/\d+/)[0]
             $modCode = $throwData.match(/\+\d*/)[0]
             $modValue = $modCode.match(/\d+/)[0];

         if ($allowedDice.includes(parseInt($dieSize)) == true) {
            var randomNumber = getRandomNumber(1,$dieSize);
            var $result = parseInt($throwNumber) * randomNumber + parseInt($modValue);
         } else {
            $result = "Błędna kostka!"
         };

         $('.results').append('<p>Losowanie: '+ $throwData + ', Wylosowano: ' + $result + '</p>');
        });
});