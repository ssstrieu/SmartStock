var addCount=0;
$( ".addStock" ).click(function() {
    $('.btnContainer').before("<div class='col-md-2'><lable for='symbol"+(addCount+3)+"' class='labels'>Ticker Symbol</lable><input type='text' class='form-control' name='symbol"+(addCount+3)+"' placeholder='NEW'></div>")
    addCount++;
    console.log(addCount);
    if (addCount>2){
    	$('.addStock').addClass('hide')

    }
})

