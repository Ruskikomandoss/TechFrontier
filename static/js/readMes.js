const readMes = document.getElementsByTagName('a');

document.addEventListener('DOMContentLoaded', function(){
for (let item of readMes){
    if (item.innerHTML.trim() === 'Read More'){
        item.addEventListener('click', function(event){
            event.preventDefault();
            alert('Nothing to read for now. Sorry!')
        })
    }
}})


