$(function () {

    var offset = $('#offset').val();
    $('.table_body').scrollTop(parseInt(offset));

    var table_head_width = $('.table_head').css('width').split('px')[0];
    $('.table_body').css('width', (parseInt(table_head_width) + 17) + 'px');
    content_fit(1200, table_head_width);

    $(window).resize(function () {
        var table_head_width = $('.table_head').css('width').split('px')[0];
        $('.table_body').css('width', (parseInt(table_head_width) + 17) + 'px');
        content_fit(1200, table_head_width);
    });


    $('#search_condition')[0].select();


    $('#upload_btn').on('click', function () {
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

    $('.modify_customer_info').on('click', function (e) {
        e.preventDefault();
        var cust_id = $(this).parent().attr('cust_id');
        var modify_customer_info_url = $(this).parent().attr('data-modifyCustomerInfoURL') + '?cust_id=' + cust_id;
        var dialog_height;

        if ($(window).width() <= 750) {
            dialog_height = 700;
        }
        else {
            dialog_height = 450;
        }

        Ewin.dialog({
            'title': '修改客户信息',
            'url': modify_customer_info_url,
            'height': dialog_height,
            'width': 450,
        })
    });


    $('#add_btn').on('click', function () {
        var add_customer_info_url = $(this).attr('data-addCustomerInfoURL');
        var dialog_height;

        if ($(window).width() <= 750) {
            dialog_height = 700;
        }
        else {
            dialog_height = 450;
        }

        Ewin.dialog({
            'title': '添加客户信息',
            'url': add_customer_info_url,
            'height': dialog_height,
            'width': 450,
        })
    });

    $('.delete_customer_info').on('click', function (e) {
        e.preventDefault();
        var cust_location = $(this).parents('tr').children('td').eq(1).text();
        var cust_name = $(this).parents('tr').children('td').eq(2).text();
        var offset = $('.table_body').scrollTop();
        console.log(offset);
        var cust_id = $(this).parent().attr('cust_id');
        var delete_customer_info_url = $(this).parent().attr('data-deleteCustomerInfoURL');
        Ewin.confirm({message: '确定删除客户 ' + cust_location + cust_name + ' ?'}).on(function (e) {
            if (e) {
                window.location.href = delete_customer_info_url + '?cust_id=' + cust_id + '&offset=' + offset
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