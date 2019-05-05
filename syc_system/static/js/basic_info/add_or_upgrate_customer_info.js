$(function () {

    $('#id_location')[0].select();

    $('#id_location').on('keypress', function (e) {
        if (e.charCode == 13) {
            e.preventDefault();
            if ($(this).val()) {
                $('#id_name')[0].select();
            }
        }
    });

    $('#id_name').on('keypress', function (e) {
        if (e.charCode == 13) {
            e.preventDefault();
            if ($(this).val()) {
                $('#id_mobilephones')[0].select();
            }
        }
    });

    $('#id_mobilephones').on('keypress', function (e) {
        if (e.charCode == 13) {
            e.preventDefault();
            $('#id_phone')[0].select();
        }
    });

    $('#id_phone').on('keypress', function (e) {
        if (e.charCode == 13) {
            e.preventDefault();
            $('#id_address')[0].select();
        }
    });


    $('#id_address').on('keypress', function (e) {
        if (e.charCode == 13) {
            e.preventDefault();
            $('#id_default_rebate')[0].select();
        }
    });

});

