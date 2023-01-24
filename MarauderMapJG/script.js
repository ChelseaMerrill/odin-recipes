

function myFunction() {
    console.log('this works')
    var x = document.getElementById("myDIV");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }

  window.onload = function() {
    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext("2d");
    var amanda_img = new Image();
    amanda_img.src = "amanda.png"
    var chelsea_img = new Image();
    chelsea_img.src = "chelsea.png";
    var josh1_img = new Image();
    josh1_img.src = "josh1.png"
    var eliza_img = new Image();
    eliza_img.src = "eliza.png";
    var emily_img = new Image();
    emily_img.src = "emily.png"
    var dom_img = new Image();
    dom_img.src = "dom.png" 
    ctx.drawImage(dom_img, 930, 450);
    ctx.drawImage(amanda_img, 10, 460);
    ctx.drawImage(chelsea_img, 50, 500);
    ctx.drawImage(josh1_img, 300, 720);
    ctx.drawImage(eliza_img, 1100, 220);
    ctx.drawImage(emily_img, 1060, 260);
    window.requestAnimationFrame(drawAshley)
    
};

function drawAshley(){
  var ctx = document.getElementsByTagName('canvas')[0].getContext('2d'),
  x = 0,
  y = 0;
function update() {
  x += 0.1;
  y += 0.1;
  if (x > 50) {
      killTheGame();return;
  }
  drawAshley();
}
function drawAshley() {
  var ashley_img = new Image();
  ashley_img.src = "ashley.png"
  ctx.clearRect(0, 0, 100, 100);
  ctx.fillStyle = 'red';
  ctx.drawImage(ashley_img, 800, 800)
  ctx.fillRect(x, y, 10, 10);
}
function killTheGame() {
  console.log('kill');
  webkitCancelRequestAnimationFrame(id);
}
var id = null;
(function tick () {
  console.log('tick');
  id = requestAnimationFrame(tick);
  update();
}());
  

}