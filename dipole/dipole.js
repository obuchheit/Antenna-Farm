
let denom = 468;
let base = 1;
let frequency = 0;
let answer = 0;
let shownAnswer = '';
let currentNum = '';

document.querySelector('#hertzSelector').addEventListener('change',hertzUnit)
document.querySelector('#wavelengthSelector').addEventListener('change', lengthDenom)
document.querySelector('.lenUnit').addEventListener('click', unitConv);


//Adds and calculates freq with every keystroke.

document.addEventListener('keydown', (event) => {

  document.querySelector('.freqInput').innerText = currentNum

  if (event.key <= 9 && event.key >= 0) {
    let keyNum = event.key;
    let numStr = keyNum.toString();
    currentNum += numStr;
    currentNum = Number(currentNum)
    document.querySelector('.freqInput').innerText = currentNum;
  } else if (event.key == 'Backspace') {
    let number = document.querySelector('.freqInput').innerText;
    let text = number.toString();
    let newNum = text.slice(0, -1);
    currentNum = Number(newNum)
    document.querySelector('.freqInput').innerText = currentNum;
  }
  calculate(currentNum);
}) 



function calculate() {
  if (currentNum == 0){
    answer = 0;
    shownAnswer = 0;
  } else {
    frequency = base * currentNum;
    answer = denom/frequency;

    //Standard function
    if (document.querySelector('.lenUnit').innerText == 'Metric') {
      let feet = Math.floor(answer);
      let remainder = answer - Math.floor(answer);
      remainder = remainder * 12;
      let inches = Math.floor(remainder);
      remainder = remainder - Math.floor(remainder);
      let decimal = Math.round(32 * remainder);
      let decDenom = 32;
      
      if (decimal == 32) {
        decimal = 0
        inches += 1;
        if (inches == 12) {
          inches = 0;
          feet += 1;
        }
      } 
      else if (decimal > 0) {
        while (decimal % 2 == 0){
          decimal = decimal / 2;
          decDenom = decDenom / 2;
        }
      }

      if (decimal == 0) {
        shownAnswer = `${feet}' ${inches}"`;
      } else if (feet == 0) {
        shownAnswer = `${inches} ${decimal}/${decDenom}"`;
      } else {
        shownAnswer = `${feet}' ${inches}" ${decimal}/${decDenom}"`;;
      }

      //Metric Function
    } else {
      answer = answer * 0.3048
      if (answer < 1 && answer > 0.1) {
        let centi = 10 * answer;
        shownAnswer = `${centi}cm`;
      } else if (answer < 0.1) {
        let mili = 100 * answer;
        shownAnswer = `${mili}mm`;
      } else {
        shownAnswer = `${answer}Meters`;
      }
    }
  }
  
  document.querySelector('.antLength').innerText = shownAnswer;
  document.querySelector('.mes').innerText = answer/2;
  document.querySelector('.mes1').innerText = answer/2;
}

//Converts the hertz unit
//Bug: doesnt calc back, prob innerText
function hertzUnit() {
  if (this.value === 'kilo') {
    base = 0.01;
  } else if ( this.value === 'mega') {
    base = 1;
  } else {
    base = 1000;
  }
  calculate(currentNum);
}
//Adds the ability to change the wavelength of an antenna.
function lengthDenom() {
  if (this.value === 'quarter') {
    denom = 234
  }else if (this.value === 'half') {
    denom = 468
  } else {
    denom = 936
  }
  calculate(currentNum);
}
//Allows user to convert from metric to satandard.
function unitConv() {
  if (document.querySelector('.lenUnit').innerText == 'Metric') {
    document.querySelector('.lenUnit').innerText = 'Standard';
  } else {
    document.querySelector('.lenUnit').innerText = 'Metric';
  }
  calculate(currentNum)
}