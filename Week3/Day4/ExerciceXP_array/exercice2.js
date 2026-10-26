const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th", "st", "nd", "rd"];

colors.forEach((color, index) => {
    const number = index + 1;

    const suffix =
        (number % 10 <= 3 && number % 10 !== 0 && number < 20)
            ? ordinal[number]
            : (number % 10 >= 1 && number % 10 <= 3)
                ? ordinal[number % 10]
                : ordinal[0];

    console.log(`${number}${suffix} choice is ${color}.`);
});
