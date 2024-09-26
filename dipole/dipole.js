document.querySelector('#hertzSelector').addEventListener('change',hertzUnit)
document.querySelector('#calcButton').addEventListener('click', calculate);
document.querySelector('#wavelengthSelector').addEventListener('change', lengthDenom)


let denom = 468;
let base = 1000000;
let frequency = 0;



function calculate() {
  int = document.querySelector('#freqInput').innerText
  frequency = base * int;
  let answer = denom/freq;
  document.querySelector('.output').innerText = answer;
  document.querySelector('.mes').innerText = answer/2;
}

function hertzUnit() {
  if (this.innerText === 'KHz') {
    base = 1000;
  } else if ( this.innerText === 'MHz') {
    base = 1000000;
  } else {
    base = 1000000000
  }
}

function lengthDenom() {
  if (this.innerText == '1/4') {
    denom = 234
  }else if (this.innerText == '1/2') {
    denom = 468
  } else {
    denom = 936
  }
}