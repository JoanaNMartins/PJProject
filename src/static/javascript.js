
document.getElementById("temp_F")
.addEventListener("keyup", function (evt) {
  // conversão da temperatura
  // let converted_val = (5/9) * (this.value - 32);

  // return/display converted value with 1 decimals
  document.getElementById("temp_C").value = parseFloat(((5/9) * (this.value - 32)).toFixed(1));
}, false);

document.getElementById("temp_C")
.addEventListener("keyup", function (evt) {
  // conversão da temperatura
  // let converted_val = (5/9) * (this.value - 32);

  // return/display converted value with 2 decimals
  document.getElementById("temp_F").value = parseFloat(((9/5) * (this.value) + 32).toFixed(1));
}, false);
