const words = ['javascript', 'html', 'github', 'intellij', 'compsci', 'css', 'python', 'binary', 'hexadecimal', 'sassybootsrap', 'codecodecode', 'pbl'];
const finalMessage = document.getElementById('final-message');
const notification = document.getElementById('notification-container');
const popup = document.getElementById('popup-container');
const figureParts= document.querySelectorAll(".figure-part");
const playAgainBtn = document.getElementById('play-button');
const wordE1 = document.getElementById('word');
const wrongLettersE1 = document.getElementById('wrong-letters');
let selectedWord = words[Math.floor(Math.random() * words.length)];
const wrongLetters = [];
const correctLetters = [];

function displayWord(){
    wordE1.innerHTML = `
    ${selectedWord
        .split('')
        .map(
            letter =>`
        <span class="letter">
        ${correctLetters.includes(letter) ? letter : ''}
        </span>
        `
        )
        .join('')}
    `;

    const innerWord = wordE1.innerText.replace(/\n/g, '');

    if(innerWord === selectedWord){
        finalMessage.innerText = 'You won! 🗿🔥💪😳';
        popup.style.display= 'flex';
    }
}

function updateWrongLetterE1(){

    wrongLettersE1.innerHTML = `
    ${wrongLetters.length > 0 ? '<p>Incorrect Answers</p>' : ''}
    ${wrongLetters.map(letter => `<span>${letter}</span>`)}
    `;


    figureParts.forEach((part,index) => {
        const errors = wrongLetters.length;

        if(index < errors) {
            part.style.display = 'block'
        }
        else{
            part.style.display = 'none';
        }
    });

    if(wrongLetters.length === figureParts.length){
        finalMessage.innerText = 'You lost... 🇱 + ratio. The correct word is displayed below.';
        wordE1.innerText = selectedWord;
        popup.style.display = 'flex';


    }
}

function showNotification(){
    notification.classList.add('show');

    setTimeout(() => {
        notification.classList.remove('show');
    }, 2000);
}


window.addEventListener('keydown', e =>{
    if(e.keyCode >= 65 && e.keyCode <=90){
        const letter = e.key;

        if(selectedWord.includes(letter)){
            if(!correctLetters.includes(letter)){
                correctLetters.push(letter);

                displayWord();
            } else{
                showNotification();
            }
        } else{
            if(!wrongLetters.includes(letter)){
                wrongLetters.push(letter);

                updateWrongLetterE1();
            } else{
                showNotification();
            }
        }
    }
});

playAgainBtn.addEventListener('click', () => {

    correctLetters.splice(0);
    wrongLetters.splice(0);

    selectedWord = words[Math.floor(Math.random() * words.length)];

    displayWord();

    updateWrongLetterE1();

    popup.style.display = 'none';
});

displayWord();

