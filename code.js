// A small JavaScript sample

function greetUser(name) {
    const cleanName = name.trim();
    return cleanName === '' ? 'Please enter your name.' : `Hello, ${cleanName}!`;
}

const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = numbers.map((number) => number * 2);
const evenNumbers = numbers.filter((number) => number % 2 === 0);
const total = numbers.reduce((sum, number) => sum + number, 0);

console.log(greetUser('Developer'));
console.log('Doubled numbers:', doubledNumbers);
console.log('Even numbers:', evenNumbers);
console.log('Total:', total);
