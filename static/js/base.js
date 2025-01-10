document.addEventListener('DOMContentLoaded', function () {
    var toastElements = [].slice.call(document.querySelectorAll('.toast'));
    toastElements.forEach(function (toastElement) {
        var toast = new bootstrap.Toast(toastElement);
        toast.show();
    });
});
    document.addEventListener('DOMContentLoaded', function () {
        const arrowUp = document.getElementById('arrowUp');

        // Show/hide the button when scrolling
        window.addEventListener('scroll', function () {
            if (window.scrollY > 200) {
                arrowUp.style.display = 'block'; // Show button when scrolled down
            } else {
                arrowUp.style.display = 'none'; // Hide button when at the top
            }
        });

        // Scroll to the top when the button is clicked
        arrowUp.addEventListener('click', function () {
            window.scrollTo({
                top: 0,
                behavior: 'smooth' // Smooth scroll to the top
            });
        });
    });
