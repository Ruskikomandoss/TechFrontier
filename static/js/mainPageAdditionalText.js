document.addEventListener('DOMContentLoaded', () => {
const revealLink = document.querySelector('#content-revealing-button button');
const hiddenContent = document.querySelector('#hidden-main-page-content');

function reveal(){
    hiddenContent.classList.toggle('is-visible');
    if (revealLink.textContent === 'Click to read more!'){
        revealLink.textContent = 'Click to hide'
    }   
    else{
        revealLink.textContent === 'Click to read more!'
    }
}

revealLink.addEventListener('click', reveal)})

/* 
This still doesn't quite work as intended, upon initial initiation the button stays
in it's 'Click to hide state'.

To be resolved later.
*/