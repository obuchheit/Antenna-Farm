document.querySelector('#hertzSelector').addEventListener('change',hertzUnit)
document.querySelector('#wavelengthSelector').addEventListener('change', lengthDenom)
document.querySelector('#calcButton').addEventListener('click', calculate);


let denom = 468;
let base = 1;
let frequency = 0;



function calculate() {
  intInput = document.getElementById('freqInput')
  int = intInput.value;
  console.log(int)
  frequency = base * int;
  console.log(frequency)
  let answer = denom/frequency;
  console.log(answer)
  document.querySelector('.antLength').innerText = answer;
  document.querySelector('.mes').innerText = answer/2;
  document.querySelector('.mes1').innerText = answer/2;
}

function hertzUnit() {
  if (this.innerText === 'KHz') {
    base = 1000;
  } else if ( this.innerText === 'MHz') {
    base = 1;
  } else {
    base = .001;
  }
  console.log(base)
}

function lengthDenom() {
  if (this.innerText == '1/4') {
    denom = 234
  }else if (this.innerText == '1/2') {
    denom = 468
  } else {
    denom = 936
  }
  console.log(denom)
}