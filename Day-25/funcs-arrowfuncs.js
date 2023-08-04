"use strict"

function subtract (num1, num2) {
    return num1 - num2;
}

console.log(subtract(10,5));

const welcome = function(name, age, gender) {
    return `My name is ${name}, I am ${age} years old of gender ${gender}`;
}

console.log(welcome('Tom', 27, 'Male'));

const powerUp = (n1, n2) => Math.pow(n1, n2);
console.log(powerUp(3, 3));