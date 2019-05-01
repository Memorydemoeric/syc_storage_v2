$(function () {

    var table_head_width = $('.table_head').css('width').split('px')[0];
    $('.table_body').css('width', (parseInt(table_head_width) + 17) + 'px');
    content_fit(1200, table_head_width);

    $(window).resize(function () {
        var table_head_width = $('.table_head').css('width').split('px')[0];
        $('.table_body').css('width', (parseInt(table_head_width) + 17) + 'px');
        content_fit(1200, table_head_width);
    });


    $('#search_condition')[0].focus();


    $('#upload_btn').on('click', function () {
        console.log('点击...');
        $('#upload_file').click();
    });


    $('#upload_file').on('change', function () {
        var dataForm = new FormData($('#upload_file_form')[0]);
        var fileURL = $('#upload_btn').attr('data-fileURL');
        Ewin.confirm({message: '确定上传客户资料?'}).on(function (ev) {
            if (ev) {
                upload_file(fileURL, dataForm);
            }
            else {
                window.location.href = ''
            }
        })

    });


    function content_fit(limit, table_head_width) {
        if (parseInt(table_head_width) < limit) {
            $('.pre_hidden').css('display', 'none');
        }
        else {
            $('.pre_hidden').css('display', '');
        }
    }


    function upload_file(url, dataForm) {
        $.ajax({
            'url': url,
            'contentType': false,
            'processData': false,
            'cache': false,
            'type': 'post',
            'data': dataForm,
            success: function (result) {
                if (result.code == 'ok') {
                    Ewin.alert({message: '客户资料上传成功...'}).on(function () {
                        window.location.href = ''
                    })

                }
                else if (result.code == 'error') {
                    Ewin.alert({message: '上传失败...'}).on(function () {
                    })
                }
            }
        });
    }

});