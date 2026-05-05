// Alerts
$(document).ready(function () {
    setTimeout(function () {
        $(".custom-alert").fadeOut('slow', function () {
            $(this).remove();
        });
    }, 3000);
});

// Delete
$(document).ready(function () {
    $('.delete-btn').on('click', function () {
        var recordId = $(this).data('slug');
        var recordName = $(this).data('name');

        $('#recordName').text(recordName);

        $('#deleteForm').attr('action', '/delete/' + recordId + '/');
    });
});

function toggleDarkMode() {
    // ضيف أو شيل الـ class من الـ body
    document.body.classList.toggle('dark-mode');

    // حفظ الاختيار في المتصفح عشان ميروحش مع الـ Refresh
    const isDark = document.body.classList.contains('dark-mode');
    localStorage.setItem('dark-mode', isDark);
}

// أول ما الصفحة تفتح، شوف المستخدم كان مختار إيه
if (localStorage.getItem('dark-mode') === 'true') {
    document.body.classList.add('dark-mode');
}