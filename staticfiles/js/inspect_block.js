document.addEventListener('DOMContentLoaded', (event) => {

    // Disable right-click context menu
    document.body.addEventListener('contextmenu', function(e) {
        e.preventDefault();
    });

    // Disable F12, Ctrl+Shift+I, Ctrl+Shift+J, Ctrl+Shift+C, Ctrl+U
    document.addEventListener('keydown', function(e) {
        if (e.keyCode == 123) { // F12
            e.preventDefault();
        }
        if (e.ctrlKey && e.shiftKey && e.keyCode == 'I'.charCodeAt(0)) { // Ctrl+Shift+I
            e.preventDefault();
        }
        if (e.ctrlKey && e.shiftKey && e.keyCode == 'J'.charCodeAt(0)) { // Ctrl+Shift+J
            e.preventDefault();
        }
        if (e.ctrlKey && e.shiftKey && e.keyCode == 'C'.charCodeAt(0)) { // Ctrl+Shift+C
            e.preventDefault();
        }
        if (e.ctrlKey && e.keyCode == 'U'.charCodeAt(0)) { // Ctrl+U
            e.preventDefault();
        }
    });
});
