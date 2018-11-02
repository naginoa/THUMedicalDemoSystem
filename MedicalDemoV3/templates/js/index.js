$(document).ready(function () {
    var flag;
    $("#desc_table").hide();
    console.log("开始ajax请求");
//上传文件并返回上传内容
    $('#file').change(function () {
        var formData = new FormData($('#uploadForm')[0]);
        $("#desc_text").html("");
        $.ajax({
            url: "/get_desc",
            type: "GET",
            data: formData,
            async: true,
            cashe: false,
            contentType: false,
            processData: false,
            success: function (result) {
                alert("上传成功");
                $("#desc_text").html(result["desc"]);
                // $("#desc_table").hide();
                //insert_table();
                flag = result["flag"]
            },
// 　　error: function (result) {
//       alert("上传失败！")
//       }
        });
    });

//判断是否已上传文件
    $.ajax({
        url: "/get_flag",
        type: "GET",
        success: function (result) {
            flag = result["flag"];
            console.log(flag);
            if (flag == 1) {
                get_desc2();
            }
        },
// 　　error: function (result) {
//       alert("上传失败！")
//       }
    });

//返回上传内容
    function get_desc2() {
        $("#desc_text").html("");
        $.ajax({
            url: "/get_desc2",
            type: "GET",
            success: function (result) {
                $("#desc_text").html(result["desc"]);
                //$("#desc_table").hide();
                //insert_table();
            },
            error: function (result) {
            }
        });

    }

//插入表格
    function insert_table() {
        color_list = ["success", "warning", "info"];
        $.ajax({
            url: "/get_table",
            type: 'GET',
            success: function (result) {
                $("#table_body").html("");
                console.log("请求成功");
                var table_list = result["table_list"];
                console.log(table_list);
                i = 0;
                j = 0;
                $.each(table_list, function (i, field1) {
                    // console.log(field1);
                    console.log(i);
                    id = "tr_" + i;
                    if (i % 2 == 0) {
                        $("#table_body").append("<tr class='active'  id=" + id + " >");
                    }
                    else {
                        $("#table_body").append("<tr class=" + color_list[j % 3] + " id=" + id + " >");
                        j++;
                    }
                    i++;

                    // $.each(field1, function (j, field2) {
                    //     $("#table_body").append("<td>"+field2+"</td");
                    $("#" + id).append("<td >" + field1["tooth_map_str"] + "</td");
                    $("#" + id).append("<td>" + field1["text"] + "</td");
                    $("#" + id).append("<td>" + field1["property"] + "</td");
                    $("#" + id).append("<td>" + field1["property_chn"] + "</td");
                    $("#" + id).append("<td>" + field1["value"] + "</td");
                    $("#" + id).append("<td>" + field1["description"] + "</td");


                    // });
                    $("#table_body").append("</tr>");
                });
            }
        });

    }

    $('#button').click(function () {
        console.log($("#desc_text"));
        $("#desc_table").hide();
        insert_table();
    });

});

