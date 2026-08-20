// A small JavaScript sample

function greetUser(name) {
    const cleanName = name.trim();
    return cleanName === '' ? 'Please enter your name.' : `Hello, ${cleanName}!`;
}

const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = numbers.map((number) => number * 2);

console.log(greetUser('Developer'));
console.log('Doubled numbers:', doubledNumbers);
