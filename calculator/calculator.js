let total = 0;
let currentNum = ''; 
let multi = false;
let div = false;



document.querySelector('#button-one').addEventListener('click', numbers)
document.querySelector('#button-two').addEventListener('click', numbers)
document.querySelector('#button-three').addEventListener('click', numbers)
document.querySelector('#button-four').addEventListener('click', numbers)
document.querySelector('#button-five').addEventListener('click', numbers)
document.querySelector('#button-six').addEventListener('click', numbers)
document.querySelector('#button-seven').addEventListener('click', numbers)
document.querySelector('#button-eight').addEventListener('click', numbers)
document.querySelector('#button-nine').addEventListener('click', numbers)
document.querySelector('#button-zero').addEventListener('click', numbers)
document.querySelector('#add-button').addEventListener('click', add);
document.querySelector('#subtract-button').addEventListener('click', add)
document.querySelector('#clear').addEventListener('click', clear)
document.querySelector('#equals-button').addEventListener('click', equals)
document.querySelector('#multi-button').addEventListener('click', multiply)

function numbers() {
  currentNum += this.innerText;
  document.querySelector('.screen').innerText = Number(currentNum);
}

function add() {
  if (this.innerText == '-' && total !== 0) {
    total += Number(currentNum);
    console.log(total)
    currentNum = '-';
    document.querySelector('.screen').innerText = 0;
  } else if (this.innerText == '-' && total == 0) {
    total += Number(currentNum);
    console.log(total)
    currentNum = '-';
    document.querySelector('.screen').innerText = 0;
  } else {
    total += Number(currentNum);
    console.log(total)
    currentNum = 0;
    document.querySelector('.screen').innerText = Number(currentNum);
  }
}
function multiply() {
  if (total == 0) {
    total += Number(currentNum);
    console.log(total);
    multi = true;
    document.querySelector('.screen').innerText = 0;
    currentNum = 0;
  } else {
    total = total * Number(currentNum);
  }
}

function divide() {
}

function equals() {
  if (multi == true) {
    total = Number(currentNum) * total;
    document.querySelector('.screen').innerText = total;
    currentNum = 0;
    console.log(total);
    multi = false;
  } else {
    total += Number(currentNum)
    document.querySelector('.screen').innerText = total;
    currentNum = 0;
    console.log(total)
  }
  
}

function clear() {
  location.reload();
}
