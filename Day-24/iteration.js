"use strict"

let a = 100

// while (a < 200) {
//     console.log('A');
//     a ++;
// }

while (a <= 200) {
    if (a %2 == 0) {
        console.log('-');
    }
    else {
        console.log('*');
    }
    a++;
}

for (let i = 0; i < 10; i++) {
    for (let j = 1; j <= 10; j++) {
        console.log(j);
    }
}

let day = 'saturday'

switch (day) {
    case 'monday':
        console.log('Monday');
    case 'tuesday':
        console.log('Tuesday');
    case 'wednesday':
        console.log('Wednesday');
    case 'thursday':
        console.log('Thursday');
    case 'friday':
        console.log('Friday');
        break;
    case 'saturday':
        console.log('Saturday');
        break;
    case 'sunday':
        console.log('Sunday');
        break;
    default:
        console.log('Not a day of the week');
}