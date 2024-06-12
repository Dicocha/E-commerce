function addToCart(productId) {
    var quantityValue = document.getElementById('input' + productId).value;

    // Check if the quantity is greater than 0 before redirecting
    if (quantityValue > 0) {
        var url = '/products/add_to_cart/%s/%s'.replace('%s', productId).replace('%s', quantityValue);
        window.location.href = url;
    } else {
        alert("Please select a valid quantity.");
    }
}