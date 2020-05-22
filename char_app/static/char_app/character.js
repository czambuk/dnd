$(".stat").bind("input", function () {
        var inputName = $(this).attr("id");
        var mod = parseInt($(this).val()) - 10;

        if (mod % 2 === 0) {
            mod = mod / 2
        } else {
            mod = (mod - 1) / 2
        }

        if (isNaN(mod)) {
            mod = ""
        } else {
            if (mod >= 0) {
                mod = mod
            }
        }

        var scoreName = inputName.slice(0, inputName.indexOf("score"));
        var modName = scoreName + "mod";

        $("[id='" + modName + "']").val(mod);
    }
);

$("[id='level']").bind("input", function () {
    var classes = $(this).val();
    var r = new RegExp(/\d+/g);
    var total = 0;
    var result;
    while ((result = r.exec(classes)) != null) {
        var lvl = parseInt(result);
        if (!isNaN(lvl)) total += lvl;
    }
    var prof = 2;
    if (total > 0) {
        total -= 1;
        prof += Math.trunc(total / 4);
    } else {
        prof = "";
    }
    $("[id='proficiencybonus']").val(prof);
});

$("[id='totalhd']").bind("input", function () {
    $("[id='remaininghd']").val($(this).val());
});
function totalhd_clicked() {
    $("[name='remaininghd']").val($("[name='totalhd']").val());
}

$('input').attr('autocomplete','off');


