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
