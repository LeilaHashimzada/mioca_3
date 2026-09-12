function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

async function updateCartItem(productId, action, url){

        const response = await fetch(url, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify({
                "productId": productId,
                "action": action
            })
        });

        const data = await response.json();
        location.reload();
        return data;
}


const cartButtons = document.querySelectorAll('.dec, .inc, .remove');

cartButtons.forEach(button => {
    button.addEventListener('click', function(event) {
        event.preventDefault();
        const btn = event.currentTarget;
        const productId = btn.dataset.product;
        const action = btn.dataset.action;
        const url = btn.dataset.url || "/update-item/";

        if (productId && action) {
            updateCartItem(productId, action, url);
        }
    });
});