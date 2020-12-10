window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let t_href = event.target;

        $.ajax({
            url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",

            success: function (data) {
                $('.basket_list').html(data.result);
            },
        });

        event.preventDefault();
    });

    // $('.btn-delete').on('click', function () {
    //     let t_href = event.target;
    //     // alert(t_href.parentElement.className);
    //     // alert((t_href.className));
    //    $.ajax({
    //        url: "/basket/delete/" + t_href.name,
    //
    //        // success: function (data) {
    //        //     $('.basket_list').html((data.result));
    //        // },
    //    });
    //
    //    // event.preventDefault();
    // });
}