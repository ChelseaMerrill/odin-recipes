

function myFunction() {
  console.log('this works')
  var x = document.getElementById("myDIV");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

window.onload = function () {
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

function drawAshley() {
  var canvas = document.getElementById("canvas");
  ctx = canvas.getContext("2d");

  var myImg = new Image();
  var myImgPos = {
    x: 500,
    y: 600,
    width: 120,
    height: 50
  }

  function draw() {
    myImg.onload = function () {
      ctx.drawImage(myImg, myImgPos.x, myImgPos.y, myImgPos.width, myImgPos.height);
    }

    myImg.src = "ashley.png";
  }

  function moveMyImg() {
    ctx.clearRect(myImgPos.x, myImgPos.y, myImgPos.x + myImgPos.width, myImgPos.y +
      myImgPos.height);
    myImgPos.x += 5;
  }

  setInterval(draw, 300);
  setInterval(moveMyImg, 300);


}