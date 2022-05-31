let results = ['rock', 'paper', 'scissors']
winners =[];

function game(){
    for (let i = 1; i <= 5; i++) {
        playRound(i);
      }
      document.querySelector("button").textContent = "Play new game";
}

function playRound(round) {
    const playerSelection = playerChoice();
    const computerSelection = computerPlay();
    const winner = checkWinner(playerSelection, computerSelection);
    winners.push(winner);
    logRound(playerSelection, computerSelection, winner, round);
}

function playerChoice() {
    let input = prompt("Type Rock, Paper, or Scissors");
    while (input == null) {
      input = prompt("Type Rock, Paper, or Scissors");
    }
    input = input.toLowerCase();
    let check = validateInput(input);
    while (check == false) {
      input = prompt(
        "Type Rock, Paper, or Scissors. Spelling needs to be exact, but capitilization doesnt matter"
      );
      while (input == null) {
        input = prompt("Type Rock, Paper, or Scissors");
      }
      input = input.toLowerCase();
      check = validateInput(input);
    }
    return input;
  }

function computerPlay(){
    return results[Math.floor(Math.random()*3)]
    
}

function validateInput(res){
    return results.includes(res);
}

function checkWinner(playerSelection, computerSelection){
    if (playerSelection === computerSelection){
        return 'draw'
    } else if ((playerSelection== 'rock' && computerSelection == 'scissors') || (playerSelection == 'paper' && computerSelection == 'rock') || ( playerSelection=='scissors' && computerSelection == 'paper')){
        return 'You win ' + playerSelection + ' beats ' + computerSelection + '!'
    } else{
        return 'You Lost ' + computerSelection + ' beats ' + playerSelection + '!'
    }
}

  function logRound(playerChoice, computerPlay, winner, round) {
    console.log("Round:", round);
    console.log("Player Chose:", playerChoice);
    console.log("Computer Chose:", computerPlay);
    console.log(winner);
  }