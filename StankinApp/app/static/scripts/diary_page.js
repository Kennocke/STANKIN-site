var button;
var element;
$(document).ready(function(){
  element = document.getElementsByName("note");
  create_btn = document.getElementById("create_btn");

  element.forEach(item => {
    item.addEventListener('click', function() {
      create_btn.disabled = true;
      create_btn.style.backgroundColor = "grey";
      element.forEach(item => {item.style.backgroundColor = "white"});
      item.style.backgroundColor = "orange";
      $.ajax({
        url: '/diary_page/',
        method: 'POST',
        data: {
          name: 'test',
          id: item.id,
          click: true
        },
        success: function (json) {
          $("input[name=created_date]").val(json.created_date);
          $("input[name=title]").val(json.title);
          $("textarea[name=main_text]").val(json.main_text);
        },
        error: function (xhr, errmsg, err) {
          console.log(xhr.status + ": " + xhr.responseText);
        }
      });
    });
  });

});
