function update_records()
{
    $(".dev-team-list tbody tr.dev-team").each(function(x, y){
        $(y).attr('id', "dev-" + (x+1));
        $(y).find('th:first label.dev-counter').text(x+1);
        $(y).find('input[name*=name]').attr('name', 'form-' + x + '-name');
        $(y).find('input[name*=brief_introduction]').attr('name', 'form-' + x + '-brief_introduction');
    });
    $("#id_form-TOTAL_FORMS").val($(".dev-team-list tbody tr.dev-team").length);
}

function add_developer() {
    me = $(this);
    //last_record = $(".dev-team-list tbody tr.dev-team:last");
    current_record = me.parent().parent();
    //last_record.after(last_record.clone());
    current_record.after(current_record.clone());
    //$(".dev-team-list tbody tr.dev-team:last").find('input[type=text]').val('');
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

$(document).ready(function(){
    update_records();
    $(document).on("click",".add_developer", add_developer);
    $(document).on("click",".del_developer", del_developer);
    $(".picture").click(function(){
        $(this).next().trigger('click');
    });
    $('input[type=file]').change(function(){
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
});