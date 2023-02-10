

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
  window.requestAnimationFrame(drawJory)
  window.requestAnimationFrame(drawAshley)
  window.requestAnimationFrame(drawZach)
};

function drawAshley() {
  var canvas = document.getElementById("canvas");
  ctx = canvas.getContext("2d");
  var myImg = new Image();
  var myImgPos = {
    x: 200,
    y: 550,
    width: 460,
    height: 200
  }
  function draw() {
    myImg.onload = function () {
      ctx.drawImage(myImg, myImgPos.x, myImgPos.y, myImgPos.width, myImgPos.height);
    }

    myImg.src = "ashley_again.png";
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
    x: 530,
    y: 630,
    width: 460,
    height: 200
  }
  function drawZach() {
    myImg.onload = function () {
      ctx.drawImage(myImg, myImgPos.x, myImgPos.y, myImgPos.width, myImgPos.height);
    }

    myImg.src = "zach_again.png";
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
    x: 790,
    y: 450,
    width: 420,
    height: 260
  }
  function drawJory() {
    myImg.onload = function () {
      ctx.drawImage(myImg, myImgPos.x, myImgPos.y, myImgPos.width, myImgPos.height);
    }

    myImg.src = "jory_again.png";
  }
  function moveJoryImg() {
    ctx.clearRect(myImgPos.x, myImgPos.y, myImgPos.x + myImgPos.width, myImgPos.y +
      myImgPos.height);
    myImgPos.y -= 6;
  }
  setInterval(drawJory, 500);
  setInterval(moveJoryImg, 500);
}


