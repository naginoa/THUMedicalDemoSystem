$(document).ready(function () {
    var flag;
    $("#img11").hide();
    $("#img12").hide();
    console.log("开始ajax请求");
//上传文件并返回上传内容
    $('#file10').change(function (e) {
        var formData = new FormData($('#uploadForm10')[0]);
        var name = e.currentTarget.files[0].name;
        console.log(name);
        var obj = document.getElementById("img11");
        obj.setAttribute("src", "http://101.6.64.182/images/backbone/" + name);
        $("#img11").show();
        var load = new Loading();
        load.init({
            target: "#div_js10"
        });
        load.start();
        $.ajax({
            url: "/get_backbone",
            type: "POST",
            data: formData,
            async: true,
            cashe: false,
            contentType: false,
            processData: false,
            success: function (bak_dict) {
                alert("检测完成");
                load.stop();
                var obj2 = document.getElementById("img12");
                obj2.setAttribute("src", bak_dict["desc"]);
                $("#img12").show();
            }
// 　　error: function (result) {
//       alert("上传失败！")
//       }
        });
    });
});
