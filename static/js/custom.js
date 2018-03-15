
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function load_modal(response,url)
{
    if (!$("#modal").hasClass("show"))
    {
        $("#modal").modal();
    }
    $("#modal_content").html(response["content"]);
    $("#modal_title").html(response["title"]);
    $("#modal_form").attr("action",url);
    $("select:not([multiple])").addClass("custom-select");
    $("select[multiple=multiple]").prop("size",10);
}

$(function() {
  
  
  $.ajaxSetup({
              beforeSend: function(xhr, settings) {
              if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
              }
              }
              });
  
  //gestion des menu (requete AJAX)
  $("select[multiple=multiple]").prop("size",20);
  
  $("body").on("click", ".link_detail", function (event) {
               url=$(this).attr("href");
               $("#modal_add_button").addClass("hidden");
               $("#modal_button").addClass("hidden");
               $.ajax({type: "GET",url: url,success : function(response){load_modal(response,url);}});
               event.preventDefault();
               });
  
  $("body").on("click", ".link_create_update", function (event) {
               url=$(this).attr("href");
               $("#modal_add_button").addClass("hidden");
               $("#modal_button").attr("class","btn btn-primary");
               $("#modal_button").html("Sauvegarder");
               $.ajax({type: "GET",url: url,success : function(response){load_modal(response,url);}});
               event.preventDefault();
               });
  
  $("body").on("click", ".link_import_or_create", function (event) {
               url=$(this).attr("href");
               $("#modal_add_button").removeClass("hidden");
               $("#modal_add_button").attr("href",url.replace("import","create"));
               $("#modal_button").attr("class","btn btn-primary");
               $("#modal_button").html("Importer");
               $.ajax({type: "GET",url: url,success : function(response){load_modal(response,url);}});
               event.preventDefault();
               });
  
  $("body").on("click", ".link_delete", function (event) {
               url=$(this).attr("href");
               $("#modal_add_button").addClass("hidden");
               $("#modal_button").attr("class","btn btn-danger");
               $("#modal_button").html("Supprimer");
               $.ajax({type: "GET",url: url,success : function(response){load_modal(response,url);}});
               event.preventDefault();
               });
  
  
  $("#modal_form").ajaxForm({
            beforeSubmit: function (arr, $form, options) {
            $("#modal_button").text("Patientez").addClass("active");
            return true;
            },
            success:function(response, status, xhr){
            location.reload(true);
            },
            error: function(response, status, xhr) {
            $("#modal_button").text("Sauvegarder").removeClass("active");
            $("#modal_content").html(response.responseJSON["content"]);
            $("select:not([multiple])").addClass("custom-select");
            $("select[multiple=multiple]").prop("size",10);
            },
            });
  
  $("#select_groupe").on('change', function() {
                         groupe=this.value;
                         if (groupe=="Tous")
                         {
                         $(".groupe").each(function(){
                                           $(this).closest("tr").removeClass("hidden");
                                           });
                         }
                         else
                         {
                         $(".groupe").each(function(){
                                           
                                           groupe_string=$(this).html();
                                           if (groupe_string.indexOf(groupe) !== -1)
                                           {
                                           $(this).closest("tr").removeClass("hidden");
                                           }
                                           else
                                           {
                                           $(this).closest("tr").addClass("hidden");
                                           }
                                           });
                         }
                         });
  
  $("#select_type").on('change', function() {
                       type=this.value;
                       if (type=="Tous")
                       {
                       $(".type").each(function(){
                                       $(this).closest("tr").removeClass("hidden");
                                       });
                       }
                       else
                       {
                       $(".type").each(function(){
                                       type_string=$(this).html();
                                       if (type_string.indexOf(type) !== -1)
                                       {
                                       $(this).closest("tr").removeClass("hidden");
                                       }
                                       else
                                       {
                                       $(this).closest("tr").addClass("hidden");
                                       }
                                       });
                       }
                       });
  
  $("#map_button").click(function(event){
     $( "#map_display" ).toggleClass("hidden show");
     $( "#list_display" ).toggleClass("hidden show");
     $( "#type_display" ).toggleClass("fa-map-marker fa-list");
     if ($("#map_display").hasClass("show"))
     {
     google.maps.event.trigger(initialize());
     }
     });

  
  
  $("body").on("click", ".button_show", function (event) {
               
               if ($(this).closest(".information").find(".row").hasClass("show"))
               {
               $(this).closest(".information").find(".row").removeClass("show");
               $(this).text("(show all)");
               }
               else
               {
               $(this).closest(".information").find(".row").addClass("show");
               $(this).text("(hide inactive)");
               }
               event.preventDefault();
               });
  });
