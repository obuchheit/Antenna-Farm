document.querySelector('#hertzSelector').addEventListener('change',hertzUnit)


document.querySelector('#calcButton').addEventListener('click', calculate);


let denom = 468;
let base = 1000000;
let frequency = 0;



function calculate() {
  let answer = denom/freq
  document.querySelector('.output').innerText = answer
}

function hertzUnit() {
  if (this.innerText)
}