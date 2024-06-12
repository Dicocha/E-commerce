function searchProduct() {
    var searchText = document.getElementById('searchBar').value;

    var url = `{% url 'products:search' text=%s %}`.replace('%s', searchText);
    window.location.href = url;
}