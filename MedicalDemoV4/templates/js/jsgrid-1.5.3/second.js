$(document).ready(function () {
    var flag;//全局变量，判断是否已上传文件
$.ajax({
    url:"/get_flag",
    type: "POST",
    success:function (result) {
        flag=result["flag"];
        console.log(flag);
        if(flag==1){
            main();
        }
　　},
　　error: function (result) {
      alert("还未上传文件！")
      }
　　　　});



function main() {
    console.log("开始ajax请求");
    //返回上传文本内容
$("#desc_text").html("");
$.ajax({
    url:"/get_desc2",
    type: "POST",
    success:function (result) {
        $("#desc_text").html(result["desc"]);
　　},
　　error: function (result) {
  }
　　　　});

//返回plan
$.ajax({
    url:"/get_plan",
    type: "POST",
    success:function (result) {
        $("#plan").html(result["plan"]);
　　},
　　error: function (result) {
    alert("get_plan error!")
  }
　　　});

//返回图片
 $.ajax({
        type:'post',
         url:"/get_picture",
         success: function(result) {
           picture_list=result["picture"];
              $("#desc_picture").html(" ");
              k=1;
            $.each(picture_list, function (i, field1) {
                //将图片的Base64编码设置给src
             $("#desc_picture").append(" <div class='col-md-4'>" +
                 "                     <img  class='img-thumbnail'  src="+field1+" >" +
                 "                </div>")
             });
            if (k%3==0){
                $("#desc_picture").append("<br/>")
            }
            k++;
             },
         error:function(data){
             alert('响应失败！');
         }
      });

}

});