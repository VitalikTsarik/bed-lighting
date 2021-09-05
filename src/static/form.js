const BASE_URL = 'http://192.168.100.43';
const LED_URL = `${BASE_URL}/led`;

const form = document.getElementById('colors');

function addColorListener(inputId, outputId) {
    const output = document.getElementById(outputId);
    const input = document.getElementById(inputId);

    output.value = parseInt(input.value);
    form.addEventListener('input', () => {
        output.value = parseInt(input.value);
    });
}

function getColorValue(id) {
    const output = document.getElementById(`${id}Output`);
    return Number(output.value);
}

addColorListener('red', 'redOutput');
addColorListener('green', 'greenOutput');
addColorListener('blue', 'blueOutput');

const submit = document.getElementsByTagName('button')[0];
submit.addEventListener('click', async (e) => {
    e.preventDefault();

    const effect = document.getElementById(`effect`).value;

    const rawResponse = await fetch(LED_URL, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            color: {
                red: getColorValue('red'),
                green: getColorValue('green'),
                blue: getColorValue('blue'),
            },
            effect: effect,
        })
    });
    const content = await rawResponse.json();
    console.log(content);
});
