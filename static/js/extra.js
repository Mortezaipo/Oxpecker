function update_records()
{
    if ($(".dev-team-list").length > 0) {
        $(".dev-team-list tbody tr.dev-team").each(function(x, y){
            $(y).attr('id', "dev-" + (x+1));
            $(y).find('th:first label.dev-counter').text(x+1);
            $(y).find('input[name*=name]').attr('name', 'form-' + x + '-name');
            $(y).find('input[name*=brief_introduction]').attr('name', 'form-' + x + '-brief_introduction');
            $(y).find('input[name*=picture]').attr('name', 'form-' + x + '-picture');
        });
        $("#id_form-TOTAL_FORMS").val($(".dev-team-list tbody tr.dev-team").length);
    
    }else if ($(".screenshot-item").length > 0) {
        $(".screenshot-item").each(function(x, y){
            $(y).attr('id', "sc-" + (x+1));
            $(y).find('input[name*=title]').attr('name', 'form-' + x + '-title');
            $(y).find('input[name*=image]').attr('name', 'form-' + x + '-image');
        });
        $("#id_form-TOTAL_FORMS").val($(".screenshot-item").length);
    }
}

function add_developer() {
    me = $(this);
    current_record = me.parent().parent();
    current_record.after(current_record.clone());
    current_record.next().find('input[type=text]').val('');
    update_records();
}

function del_developer() {
    if ($(".dev-team-list tbody tr.dev-team").length == 1) {
        return false;
    }
    me = $(this);
    me.parent().parent().remove();
    update_records();
}

function add_screenshot() {
    me = $(this);
    current_record = me.parent().parent().parent().parent();
    current_record.after(current_record.clone());
    current_record.next().find('input[type=text]').val('');
    current_record.next().find('input[type=file]').val('');
    current_record.next().find('.screenshot').css({'background-image': ''});
    current_record.next().find('.screenshot').html('<div class="upload_screenshot picture text-center">Click Here To Upload</div>');
    update_records();
}

function del_screenshot() {
    if ($(".screenshot-item").length == 4) {
        return false;
    }
    me = $(this);
    me.parent().parent().parent().parent().remove();
    update_records();
}


$(document).ready(function(){
    update_records();
    $(document).on("click",".add_developer", add_developer);
    $(document).on("click",".del_developer", del_developer);
    $(document).on("click",".add-screenshot", add_screenshot);
    $(document).on("click",".del-screenshot", del_screenshot);

    $(document).on('click', '.picture', function(){
        $(this).next().trigger('click');
    });
    
    $(document).on('change','.profile_picture',function(){
         var me = this;
         if (me.files && me.files[0]) {
             var reader = new FileReader();
             reader.onload = function(e)
             {
                 $(me).prev().html('');
                 $(me).prev().addClass('div-picture');
                 $(me).prev().css({'background-image': 'url(' + e.target.result + ')'});
             }
             reader.readAsDataURL(me.files[0]);
         }else{
            $(me).prev().css({'background-image': ''});
            $(me).prev().removeClass('div-picture');
            $(me).prev().html('<i class="fa fa-camera"></i>');
         }
    });
    
    $(document).on('change','.screenshot-file',function(){
        var me = this;
        if (me.files && me.files[0]) {
             var reader = new FileReader();
             reader.onload = function(e)
             {
                 $(me).prev().html('');
                 $(me).prev().css({'background-image': 'url(' + e.target.result + ')'});
             }
             reader.readAsDataURL(me.files[0]);
         }else{
             $(me).prev().css({'background-image': ''});
             $(me).prev().html('<div class="upload_screenshot picture text-center">Click Here To Upload</div>');
         }
    });
});