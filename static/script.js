
  document.onreadystatechange = function() {
      if (document.readyState !== "complete") {
          document.querySelector(
            "body").style.visibility = "hidden";
          document.querySelector(
            "#loader").style.visibility = "visible";
      } else {
          document.querySelector(
            "#loader").style.display = "none";
          document.querySelector(
            "body").style.visibility = "visible";
      }
  };

function show(){
  
  
  var OpenWindow = window.open('','_blank','width=1024,height=768,resizable=1');
  var content = document.getElementById('forSBWindow');

  OpenWindow.document.write('<html><head><title>New window</title><link rel="stylesheet" type="text/css" href="'+url+'style.css"><link rel="stylesheet" type="text/css" href="'+url+'ref/ref.css"><script type="text/javascript" src="'+url+'main.js"></script><script type="text/javascript" src="'+url+'ref/ref.js"></script></head><body onmouserout="function()=>{alert("cycki")}" style="directories=no,titlebar=no,toolbar=no,location=no,status=no, menubar=no,scrollbars=no,resizable=no,width=400,height=350">');
  OpenWindow.document.write( content.outerHTML );
  OpenWindow.document.write('</body></html>');
 
  }

function close(){
  var x = document.getElementById('formContainer');
  var del = document.getElementById('container')
  x.remove(del)

  

}
let x;
function importData() {
  
  
    x = prompt("Wpisz adres url nowego obrazka: ",'');   
      

 
  
}
  function change(id) {
  importData();
  
   
   var c = JSON.parse('{"'+x+'":"'+id+'"}');
   $.ajax({
    type: 'POST',
    url: "/change",
    data: c,
    dataType: "json",
    success: function(data){
     
      var d= JSON.parse(data)
      alert(Object.keys(d))
      $("#calculate").attr("src", Object.keys(d));
             }
  });
  }
  
  
