window.onload = function(){
    const button = document.getElementById('openWindowButton')

    button.addEventListener('click', event => {
        button.textContent = `Click count: ${event.detail}`
    });
}
