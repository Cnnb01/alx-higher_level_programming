$(function () {

    var $orders = $('#orders'); //for caching purposes #orders is the ul class where you'll be listing out the orders
    var $name = $('#name');
    var $drink = $('#drink')

    var orderTemplate = "<li>name: {{name}}, drink: {{drink}}</li>" + "<button data-id='{{id}}' class='remove'>X</button>"

    function addOrder(order) {
        $orders.append(Mustache.render(orderTemplate, order));
    }

    // for GET
    $.ajax({
        type: 'GET',
        url: '/api/orders',
        success: function(orders) {
            $.each(orders, function(i, order){
                addOrder(order);
            });
            // console.log('success', data);
        },
        error: function() {
            alert('error loading orders');
        }
    });


    // for POST
    $('#add-order').on('click',function() {
        var order = {
            name: $name.val(),
            drink: $drink.val(),
        };
        $.ajax({
            type: 'POST',
            url: '/api/orders',
            data: order,
            success: function(newOrder) {
                addOrder(newOrder);
            },
            error: function() {
                alert('error loading orders');
            }
        });
    })


    // for DELETE
    $orders.delegate('.remove', 'click', function() {
        var $li = $(this).closest('li')
        $ajax({
            type: 'DELETE',
            url: '/api/orders/' + $(this).attr('data-id'),
            success: function() {
                $li.remove();
            }
        });
    })

    
});