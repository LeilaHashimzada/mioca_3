let addBtns = document.getElementsByClassName('add-cart')

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

for (let i = 0; i < addBtns.length; i++){

    addBtns[i].addEventListener('click', function(event){
        event.preventDefault()
        let productId = this.dataset.product
        let action= this.dataset.action

        console.log("Item Added!", productId, action)

        let url = "update-item/"

        fetch(url, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify({
                "productId": productId,
                "action": action
            })
        }).then((response) => {
            return response.json()
        }).then((data) => {
            location.reload()
        })
    })

}
