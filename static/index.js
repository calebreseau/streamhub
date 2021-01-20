$( document ).ready(function() {
    console.log('oka');
    $('#searchbar').focus(function(e){
        //console.log('ok');
        console.log($('#searchbar').val());;
        $('#ui').css('padding-top','3%');
        $('#searchbar').css('font-size','32px');
    });

    $('input').bind("enterKey",function(e){
        console.log('ok');
        $('#ui').css('padding-top','3%');
        $('#searchbar').css('font-size','25px');
        $('#searchbar').blur();
        $('#content').html('<div id="loading"><div class="cssload-container"><div class="cssload-item cssload-moon"></div></div></div>');
        $('#loading').css('display','inline-block');
        $(document).prop('title', 'streamhub - loading');
        //return; 
        $.get('/watch?title='+$('#searchbar').val().replace(' ','%20'),function(data){
            $('#loading').css('display','none');
            $(document).prop('title', 'streamhub - '+$('#searchbar').val());
            $('#content').html(data);
            $.getScript("/static/watch.js", function(data, textStatus, jqxhr) {
                console.log(data); //data returned
                console.log(textStatus); //success
                console.log(jqxhr.status); //200
                console.log('Load was performed.');
                });
            $('<link>')
            .appendTo('head')
            .attr({
                type: 'text/css', 
                rel: 'stylesheet',
                href: '/static/watcher.css'
            });
    
        });
      });
      $('#searchbar').keyup(function(e){
        if(e.keyCode == 13)
        {
           $(this).trigger("enterKey");
        }
      });
      

});