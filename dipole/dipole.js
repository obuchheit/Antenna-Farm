
let denom = 468;
let base = 1;
let frequency = 0;
let answer = 0;

document.querySelector('#hertzSelector').addEventListener('change',hertzUnit)
document.querySelector('#wavelengthSelector').addEventListener('change', lengthDenom)
document.querySelector('#calcButton').addEventListener('click', calculate);

document.querySelector('.lenUnit').addEventListener('click', calculate);


//unitButton change to select attr 


function calculate() {
  intInput = document.getElementById('freqInput')
  int = intInput.value;
  frequency = base * int;
  answer = denom/frequency;

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