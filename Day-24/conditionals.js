let strictA = true;
let strictB = 1;
console.log(strictA == strictB); // true
console.log(strictA === strictB); // false

console.log(strictA != strictB); //false
console.log(strictA !== strictB); //true

let age = 10

if (age > 18 && age < 65) {
    console.log('Adult');
}
else if (age < 18) {
    console.log('Underage');
}
else {
    console.log('OAP');
}

console.log((age > 50)? 'over 50' : 'under 50');