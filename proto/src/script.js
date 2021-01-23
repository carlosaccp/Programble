
function paste(){
  navigator.clipboard.writeText(`import matplotlib.pyplot as plt



  x = [1, 2, 3, 4]
  y = [1, 4, 9, 16]
  
  
  
  plt.plot(x, y)
  plt.xlabel('X-axis label')
  plt.ylabel('Y-axis label')
  plt.show()`);
}

function hider() {
    var x = document.getElementById('fader');
    if (x.style.display === "none") {
        x.style.display = "block";
      } 
    else {
        x.style.display = "none";
      }
}