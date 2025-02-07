document.getElementById('resume-form').addEventListener('input', function() {
    const formData = new FormData(this);
    fetch('/update_preview', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(html => {
        document.getElementById('preview').innerHTML = html;
    });
});
