

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
  emily_img.src = "emily.png";
  var dom_img = new Image();
  dom_img.src = "dom.png";
  var ant_img = new Image();
  ant_img.src = "ant.png";
  var darrin_img = new Image();
  darrin_img.src = "darrin.png";
  var grayce_img = new Image();
  grayce_img.src = "grayce.png";
  var isaiah_img = new Image();
  isaiah_img.src = "isaiah.png";
  var jessie_img = new Image();
  jessie_img.src = "jessie.png";
  var jet_img = new Image();
  jet_img.src = "jet.png";
  var michael_img = new Image();
  michael_img.src = "michael.png";
  ctx.drawImage(dom_img, 930, 450);
  ctx.drawImage(amanda_img, 10, 460);
  ctx.drawImage(chelsea_img, 50, 500);
  ctx.drawImage(josh1_img, 300, 720);
  ctx.drawImage(eliza_img, 1100, 220);
  ctx.drawImage(emily_img, 1060, 260);
  ctx.drawImage(ant_img, 410, 640);
  ctx.drawImage(michael_img, 480, 650);
  ctx.drawImage(isaiah_img, 255, 458);
  ctx.drawImage(jessie_img, 345, 570);
  ctx.drawImage(jet_img, 700, 150);
  ctx.drawImage(grayce_img, 670, 180);
  ctx.drawImage(darrin_img, 1100, 740);

  // window.requestAnimationFrame(drawZach)
  // window.requestAnimationFrame(drawAshley)
  // window.requestAnimationFrame(drawJory)

};

function drawAshley() {
  var canvas = document.getElementById("canvas");
  ctx = canvas.getContext("2d");
  var myImg = new Image();
  var myImgPos = {
    x: 590,
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
  setInterval(draw, 500);
  setInterval(moveMyImg, 500);
}

function drawZach() {
  var canvas = document.getElementById("canvas");
  ctx = canvas.getContext("2d");
  var myImg = new Image();
  var myImgPos = {
    x: 650,
    y: 680,
    width: 120,
    height: 50
  }
  function drawZach() {
    myImg.onload = function () {
      ctx.drawImage(myImg, myImgPos.x, myImgPos.y, myImgPos.width, myImgPos.height);
    }

    myImg.src = "zach.png";
  }
  function moveZachImg() {
    ctx.clearRect(myImgPos.x, myImgPos.y, myImgPos.x + myImgPos.width, myImgPos.y +
      myImgPos.height);
    myImgPos.x += 5;
  }
  setInterval(drawZach, 500);
  setInterval(moveZachImg, 500);
}

function drawJory() {
  var canvas = document.getElementById("canvas");
  ctx = canvas.getContext("2d");
  var myImg = new Image();
  var myImgPos = {
    x: 980,
    y: 570,
    width: 120,
    height: 50
  }
  function drawJory() {
    myImg.onload = function () {
      ctx.drawImage(myImg, myImgPos.x, myImgPos.y, myImgPos.width, myImgPos.height);
    }

    myImg.src = "jory.png";
  }
  function moveJoryImg() {
    ctx.clearRect(myImgPos.x, myImgPos.y, myImgPos.x + myImgPos.width, myImgPos.y +
      myImgPos.height);
    myImgPos.y -= 5;
  }
  setInterval(drawJory, 500);
  setInterval(moveJoryImg, 500);
}