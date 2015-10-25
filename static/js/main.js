var addCount=0;
$( ".addStock" ).click(function() {
    $('.btnContainer').before("<div class='col-md-2'><lable for='symbol' class='labels'>Ticker Symbol</lable><input type='text' class='form-control' name='symbol' placeholder='NEW'></div>")
    addCount++;
    console.log(addCount);
    if (addCount>2){
    	$('.addStock').addClass('hide')

    }
})

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

$(function () {
  $('[data-toggle="popover"]').popover()
})
