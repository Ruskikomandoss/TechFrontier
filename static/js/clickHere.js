const clickhere = document.querySelector("#terms a")


document.addEventListener('DOMContentLoaded', function(){
    if (sessionStorage.getItem('clickedTooMuch') === 'true'){
        clickhere.style.display = 'none'
    } else {

    let clickCount = 0;
    clickhere.addEventListener('mouseover', function(){
        clickhere.style.backgroundColor = 'pink';
    });

    clickhere.addEventListener('mouseout', function(){
        clickhere.style.backgroundColor = '#444'
    });

    clickhere.addEventListener('click', function(event){
        event.preventDefault();
        clickCount++;

        if (clickCount === 1){
            clickhere.textContent = "Congrats, you have clicked!"
        } else if (clickCount === 2){
            clickhere.textContent = "Nice, twice clicked"
        } else if (clickCount === 3){
            confirm('Ok, I get it, it was fun for a moment. But stop clicking. If you click again, consequences shall be severe.')
            clickhere.textContent = "Don't click me again 😠"
        } else if (clickCount === 4){
            alert("That's it. No more cool clicking button for you.")
            clickhere.remove()
            sessionStorage.getItem('ClickedTooMuch', 'true')
        }

})}})
