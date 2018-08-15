
function addtr(){
    var table = $("#alertrule");
    var t= $('<div class="form-inline" style="width: auto;">\
                <label style="width: auto;">警告方式:</label>\
                <select class="form-control" style="width: auto;">\
                <option>邮箱</option> <option>短信</option>\
                </select><label>&nbsp;&nbsp;&nbsp;联系方式:</label>\
                <input class="form-control" style="width: 100px;">\
                <label>&nbsp;&nbsp;&nbsp;命中数:</label>\
                <input class="form-control" style="width: 100px;">\
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