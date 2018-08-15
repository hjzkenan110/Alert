
function addtr(){
    var table = $("#alertrule");
    var t= $('<div class="form-inline" style="width: auto;">\
                <label style="width: auto;">警告方式:</label>\
                <select class="form-control" style="width: auto;" id="fuuu">\
                <option>邮箱</option> <option>短信</option>\
                </select><label>&nbsp;&nbsp;&nbsp;联系方式:</label>\
                <input class="form-control" style="width: 200px;" id="address">\
                <label>&nbsp;&nbsp;&nbsp;命中数:</label>\
                <input class="form-control" style="width: 200px;" id="numevents">\
                <div class="pull-right">\
                <button type="button" class="btn-xs btn-link" onclick="minus(this)">\
                <span class="glyphicon glyphicon glyphicon-minus"></span>\
                </button></div></div></br>');    
    table.append(t);
}


function minus(buttonobject){
    var td=$(buttonobject);
    td.parents(".pull-right").parents(".form-inline").next().remove();
    td.parents(".pull-right").parents(".form-inline").remove();
}

function sub(){
    var title = document.getElementById("title").value;
    var message = document.getElementById("message").value;
    var time_frame_type = document.getElementById("time_frame_type").value;
    var time_frame_num = document.getElementById("time_frame_num").value;
    var alert_type = document.getElementById("alert_type").value;
    var address = document.getElementById("address").value;
    var numevents = document.getElementById("numevents").value;
    var fuuu = document.getElementById("fuuu").value;
    alert(title, message, time_frame_type, time_frame_num, alert_type, address, numevents)
    data = {
        "title": title,
        "message": message,
        "time_frame_type": time_frame_type,
        "time_frame_num": time_frame_num
    }
    // $.ajax({
    //     type : "POST",
    //     url : js_path + "/api/alert",
    //     data : JSON.stringify(madd_data.editMaintain),
    //     contentType : "application/json",
    //     dataType : "json",
    // });
}