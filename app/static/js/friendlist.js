
var table = $('#friendslist').DataTable( {
    dom: 'Bfrtip',
    select: true,
    buttons: [
        {
            action: function () {
                var rows = table.rows( { selected: true } )
                console.log(rows)

            }
        }
    ]
} );
$('#friendslist tbody').on( 'click', 'td', function () {

    $.ajax({
      url:'/choosefriend',
      type: 'POST',
      data: {
             'username':table.cell( this ).data(),
           },
      async: true,
      cache: false,

      success: function() {
        console.log('here')
        window.location.replace('/chat')
      }
    });
} );
