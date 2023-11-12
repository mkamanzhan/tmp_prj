$(function()
    {
      $('#censor-check').change(function()
      {
        if ($(this).is(':checked')) {
            for (let i = 0; i < 9; i++) {
                $('#com-text-'+i).text($('#com-'+i).text())
                console.log($('#com-text-'+i).text())
            }
        }
        else{
            for (let i = 0; i < 9; i++) {
                $('#com-text-' + i).text($('#con-' + i).text())
            }
        }
      });
    });
