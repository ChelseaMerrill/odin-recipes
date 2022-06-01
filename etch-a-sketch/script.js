function menu(){
  document.getElementById('menu').innerHTML= 'To use this etch-a-sketch, click on each cell to fill it in'
}

function fillCell(element, color){
   element.style.backgroundColor = color;
}