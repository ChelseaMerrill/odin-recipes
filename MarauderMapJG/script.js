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
    var dom_img = document.getElementById("dom");
    var amanda_img = document.getElementById("amanda");
    var chelsea_img = document.getElementById("chelsea");
    var josh1_img = document.getElementById("josh1");
    var eliza_img = document.getElementById("eliza");
    var emily_img = document.getElementById("emily");
    ctx.drawImage(dom_img, 930, 450);
    ctx.drawImage(amanda_img, 10, 460);
    ctx.drawImage(chelsea_img, 50, 500);
    ctx.drawImage(josh1_img, 300, 720);
    ctx.drawImage(eliza_img, 1100, 220);
    ctx.drawImage(emily_img, 1060, 260);
};