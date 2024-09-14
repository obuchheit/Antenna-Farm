let total = 0;
let currentNum = ''; 


document.querySelector('#button-one').addEventListener('click', one)
document.querySelector('#button-two').addEventListener('click', two)
document.querySelector('#button-three').addEventListener('click', three)
document.querySelector('#button-four').addEventListener('click', four)
document.querySelector('#button-five').addEventListener('click', five)
document.querySelector('#button-six').addEventListener('click', six)
document.querySelector('#button-seven').addEventListener('click', seven)
document.querySelector('#button-eight').addEventListener('click', eight)
document.querySelector('#button-nine').addEventListener('click', nine)
document.querySelector('#button-zero').addEventListener('click', zero)
document.querySelector('#add-button').addEventListener('click', add);
document.querySelector('#subtract-button').addEventListener('click', add)
document.querySelector('#clear').addEventListener('click', clear)
document.querySelector('#equals-button').addEventListener('click', equals)


function one() {
  currentNum += '1';
  console.log(currentNum);
  document.querySelector('.screen').innerText = Number(currentNum);
}

function two() {
  currentNum += '2';
  document.querySelector('.screen').innerText = Number(currentNum);
}

function three() {
  currentNum += '3';
  document.querySelector('.screen').innerText = Number(currentNum);
}

function four() {
  currentNum += '4';
  document.querySelector('.screen').innerText = Number(currentNum);
}

function five() {
  currentNum += '5';
  document.querySelector('.screen').innerText = Number(currentNum);
}

function six() {
  currentNum += '6';
  document.querySelector('.screen').innerText = Number(currentNum);
}

function seven() {
  currentNum += '7';
  document.querySelector('.screen').innerText = Number(currentNum);
}

function eight() {
  currentNum += '8';
  document.querySelector('.screen').innerText = Number(currentNum);
}

function nine() {
  currentNum += '9';
  document.querySelector('.screen').innerText = Number(currentNum);
}
function zero() {
  currentNum += '0';
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
}
function divide() {
}

function equals() {
  total += Number(currentNum)
  document.querySelector('.screen').innerText = total;
  console.log(total)
}

function clear() {
  location.reload();
}
