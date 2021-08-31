
function show() {
  var p = document.getElementById('pwd');
  p.setAttribute('type', 'text');
}

function hide() {
  var p = document.getElementById('pwd');
  p.setAttribute('type', 'password');
}

var pwShown = 0;

document.getElementById("eye").addEventListener("click", function () {
  if (pwShown == 0) {
      pwShown = 1;
      show();
  } else {
      pwShown = 0;
      hide();
  }
}, false);


function save_checkbox(name)
{
    localStorage[name] = document.getElementById(name).checked ? 1 : 0
}
function load_checkbox()
{
    var table = document.getElementById('resources')
    var input = table.getElementsByTagName('input')
 
    for(var i = 0; i < input.length; i++)
    {
        var checkbox = input[i]
        checkbox.checked = parseInt(localStorage[checkbox.id], 10)
    }
}