document.querySelectorAll('.form-content').forEach(function(element) {
    element.style.display = 'none';
});

document.getElementById('typeselect').addEventListener('change', function() {
    console.log(this.value+"-form")
    // Get the value of the selected option
    let selectedOption = this.value;
    // Hide all content elements
    document.querySelectorAll('.form-content').forEach(function(element) {
        element.style.display = 'none';
    });
    // Show the content element that corresponds to the selected option
    document.getElementById(selectedOption + '-form').style.display = 'block';
});

function navbarCollapse(element) {
    console.log(element)
    if (!element.style.height || element.style.height == '0px') { 
        element.style.height = Array.prototype.reduce.call(element.childNodes, function(p, c) {return p + (c.offsetHeight || 0);}, 0) + 'px';
    } else {
        element.style.height = '0px';
    }
}