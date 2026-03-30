const celsius = 25.0;
const fahrenheit = (celsius * 9/5) + 32;
const kelvin = celsius + 273.15;

console.log(`${celsius} deg C = ${fahrenheit.toFixed(2)} deg F = ${kelvin.toFixed(2)}K`);
function celsiusToFahrenheit(c: number): number {
  return (c * 9) / 5 + 32;
}

console.log(celsiusToFahrenheit(0));
