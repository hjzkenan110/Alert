window.onload=function(){ 
    get_info();
} 

function get_info() {
    $.ajax({
        url: '/api/alert', //请求的url
        type: 'get', //请求的方式
        cache : false,	//禁用缓存
        dataType: "json",
        error:function () {
            alert('请求失败');
        },
        success:function (data) {
            var str1 = "";
            //清空table中的html
            $("#tab").html("");
            for(var i = 0;i<data.length;i++){
                str1 = '<tr class="grid-item"><td class="action-checkbox"><input type="checkbox" name="_selected_action" value="'+ data[i]['info_id']+ '" class="action-select"></td>\
                <td>' + data[i]['info_id'] + '</td>\
                <td>' + data[i]['title'] + '</td>\
                <td>' + data[i]['message'] + '</td>\
                <td>' + data[i]['time_frame_type'] + '</td>\
                <td>' + data[i]['time_frame_num'] + '</td>\
                <td>' + data[i]['update_time'] + '</td>\
                <td>' + data[i]['create_time'] + '</td>\
                <td>修改/删除</td>'
                $("#tab").append(str1);
            }
            //$("#fuck").append("</tbody></th>")
        }
    });
} 

function checkOrCancelAll(){
    var check=document.getElementById("action-toggle");
    //2.获取选中状态
    var checkedElt=check.checked;
    //3.若checked=true,将所有的复选框选中,checked=false,将所有的复选框取消
    var allCheck=document.getElementsByName("_selected_action");
    //4.循环遍历取出每一个复选框中的元素
    if(checkedElt){
        //全选
        for(var i=0;i<allCheck.length;i++){
            //设置复选框的选中状态
            allCheck[i].checked=true;
        }
    }else{
        //取消全选
        for(var i=0;i<allCheck.length;i++){
            allCheck[i].checked=false;
        }
    }
}
    