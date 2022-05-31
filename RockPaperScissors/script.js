let results = ['rock', 'paper', 'scissors']
function computerPlay(res){
   let ran = Math.floor(Math.random()*3)
    return res[ran]
}
console.log(computerPlay(results))