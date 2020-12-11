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

    $('.basket_list').on('click', '.button-remove', function () {
        let pk = $(this).attr('data-pk');
        if(pk){
            $.ajax({
                url: "/basket/remove/ajax/" + pk + "/",

                success: function (data) {
                    $('.basket_list').html(data.result);
                }
            })
        }
        return;
    });
};