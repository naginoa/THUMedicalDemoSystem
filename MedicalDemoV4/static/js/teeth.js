$(document).ready(function () {
    var flag;
    $("#img1").hide();
    $("#img2").hide();
    console.log("开始ajax请求");
//上传文件并返回上传内容
    $('#file5').change(function (e) {
        var formData = new FormData($('#uploadForm5')[0]);
        var name = e.currentTarget.files[0].name;
        console.log(name);
        var obj = document.getElementById("img1");
        obj.setAttribute("src", "http://101.6.64.182/images/teeth_detection/" + name);
        $("#img1").show();
        var load = new Loading();
        load.init({
            target: "#div_js"
        });
        load.start();
        $.ajax({
            url: "/get_teeth",
            type: "POST",
            data: formData,
            async: true,
            cashe: false,
            contentType: false,
            processData: false,
            success: function (img_dict) {
                alert("检测完成");
                load.stop();
                var obj2 = document.getElementById("img2");
                obj2.setAttribute("src", img_dict["desc"]);
                $("#img2").show();
            }
// 　　error: function (result) {
//       alert("上传失败！")
//       }
        });
    });
});
