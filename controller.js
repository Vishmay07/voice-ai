$(document).ready(function () {
    

    eel.expose(DisplayMessage)
    function DisplayMessage (message) {

        $(".siri-message li:first").text(message);
        $(".siri-message ").textillate("start");
      }

      eel.expose(showHood)
      function showHood(){
        $("#oval").attr("hidden",false);
        $("#siriwave").attr("hidden",true);
      }


});