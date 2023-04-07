document.addEventListener("DOMContentLoaded", () => {
    const changingText = document.querySelector('.changing-text');
    const phrases = [
        'сайты для стартапов',
        'телеграмм боты для общения',
        'сайты для бизнесов',
        'сайты общего пользования'
    ];
    let currentPhraseIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    
    function updateText() {
        if (isDeleting) {
            if (charIndex > 0) {
                charIndex--;
            } else {
                isDeleting = false;
                currentPhraseIndex = (currentPhraseIndex + 1) % phrases.length;
            }
        } else {
            if (charIndex < phrases[currentPhraseIndex].length) {
                charIndex++;
            } else {
                isDeleting = true;
            }
        }
        changingText.textContent = phrases[currentPhraseIndex].substring(0, charIndex);
        setTimeout(updateText, isDeleting ? 100 : 200);
    }
    updateText();
});
