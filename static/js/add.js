var alert_count = 1;
var alert_count_list = Array();
alert_count_list.push(alert_count);

function addtr(){
    alert_count++;
    alert_count_list.push(alert_count);

    var table = $("#alertrule");
    str = parseInt(alert_count);
    var h = '<div class="form-inline" style="width: auto;">\
                <label style="width: auto;">警告方式:</label>\
                <select class="form-control" style="width: auto;" id="alert_type_'+ str + '">\
                <option>------</option>\
                <option value="email">邮箱</option> <option value="phone">短信</option>\
                </select><label>&nbsp;&nbsp;&nbsp;联系方式:</label>\
                <input class="form-control" style="width: 200px;" id="address_'+ str + '">\
                <label>&nbsp;&nbsp;&nbsp;命中数:</label>\
                <input class="form-control" style="width: 200px;" id="numevent_'+ str + '">\
                <div class="pull-right">\
                <button type="button" class="btn-xs btn-link" onclick="minus(this)">\
                <span class="glyphicon glyphicon glyphicon-minus"></span>\
                </button></div></div></br>'
    var t= $(h);    
    table.append(t);
}


function minus(buttonobject){
    var td=$(buttonobject);
    alert_num = td.parents(".pull-right").prev(".form-control").attr('id');
    alert_num = alert_num.slice(9);
    alert_num = parseInt(alert_num);
    for(var i = 1;i <= alert_count_list.length; i++){
        if (alert_num == alert_count_list[i]){
            alert_count_list.splice(i, 1);
            break;
        }
    }

    td.parents(".pull-right").parents(".form-inline").next().remove();
    td.parents(".pull-right").parents(".form-inline").remove();
}

function sub(){
    var title = document.getElementById("title").value;
    var message = document.getElementById("message").value;
    var v = $("#time_frame_type option:selected").val();
    if(v == '分钟'){
        v = 'minutes';
    }

    var time_frame_type = v;
    //var time_frame_type = options.;
    var time_frame_num = document.getElementById("time_frame_num").value;
    var alert_list = Array()
    for(var i = 0; i < alert_count_list.length; i++){
        str = alert_count_list[i] + "";

        alert_list.push({"alert_type": $("#alert_type_"+ str +" option:selected").val(), "address": document.getElementById("address_"+ str).value, "numevents": document.getElementById("numevent_"+ str).value});
    }
    data = {
        'title': title,
        'message': message,
        'time_frame_type': time_frame_type,
        'time_frame_num': time_frame_num,
        'alert': alert_list
    }
    $.ajax({
        type : "POST",
        url : "/api/alert/",
        data : JSON.stringify(data),
        headers:{},
        contentType : "application/json",
        dataType : "json",
        success: function(result){
            alert("请记住您的id: "+ result["id"])
            window.location.href="../list/"
        }
    });
}

$("#checkall").click(function(){
    
});