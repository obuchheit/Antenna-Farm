
let denom = 468;
let base = 1;
let frequency = 0;
let answer = 0;
let shownAnswer = '';
let halfShownAnswer = '';
let currentNum = '';

document.querySelector('#hertzSelector').addEventListener('change',hertzUnit)
document.querySelector('#wavelengthSelector').addEventListener('change', lengthDenom)
document.querySelector('.lenUnit').addEventListener('click', unitConv);
document.querySelector('#quickBands').addEventListener('change', bandsCalc);


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

      let halfFeet = feet/2;
      let halfInches = inches/2;
      let halfFrac = decimal/2;
      let halfDecDenom = 32;
      
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

      //Half Measurement function

      if (halfFrac == 32) {
        halfFrac = 0
        halfInches += 1;
        if (halfInches == 12) {
          halfInches = 0;
          halfFeet += 1;
        }
      } 
      else if (halfFrac > 0) {
        while (halfFrac % 2 == 0){
          halfFrac = halfFrac / 2;
          halfDecDenom = halfDecDenom / 2;
        }
      }

      if (halfFrac == 0) {
        halfShownAnswer = `${halfFeet}' ${halfInches}"`;
      } else if (halfFeet == 0) {
        halfShownAnswer = `${halfInches} ${halfFrac}/${halfDecDenom}"`;
      } else {
        halfShownAnswer = `${halfFeet}' ${halfInches}" ${halfFrac}/${halfDecDenom}"`;
      }

      //Metric Function
    } else {
      answer = answer * 0.3048
      if (answer < 1 && answer > 0.1) {
        let centi = 10 * answer;
        shownAnswer = `${(centi).toFixed(2)}cm`;
        halfShownAnswer = `${(centi/2).toFixed(2)}cm`;
      } else if (answer < 0.1) {
        let mili = 100 * answer;
        shownAnswer = `${(mili).toFixed(1)}mm`;
        halfShownAnswer = `${(mili/2).toFixed(1)}mm`;
      } else {
        shownAnswer = `${(answer).toFixed(3)}Meters`;
        halfShownAnswer = `${(answer/2).toFixed(3)}Meters`
      }
    }
  }
  
  document.querySelector('.antLength').innerText = shownAnswer;
  document.querySelector('.mes').innerText = halfShownAnswer;
  document.querySelector('.mes1').innerText = halfShownAnswer;
}

//Converts the hertz unit
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
  if (this.innerText === 'Metric') {
    this.innerText = 'Standard';
  } else {
    this.innerText = 'Metric';
  }
  calculate(currentNum)
}

//Calculates Pre-Configured Bands
function bandsCalc() {
  currentNum = this.value;
  document.querySelector('.freqInput').innerText = currentNum;
  calculate(currentNum);
}