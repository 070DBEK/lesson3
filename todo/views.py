from django.http import HttpResponse

def task_create(request):
    html = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <title>Yangi Vazifa Yaratish</title>
    <style>
        /* Ваши стили */
    </style>
</head>
<body>
    <h1>Yangi vazifa yaratish</h1>
    <form action="/create-task" method="POST">
        <label for="vazifa_nomi">Vazifa nomi:</label>
        <input type="text" id="vazifa_nomi" name="vazifa_nomi" required>
        <br>
        <br>
        <label for="tavsif">Tavsif:</label>
        <textarea id="tavsif" name="tavsif" required></textarea>
        <br>
        <br>
        <label for="muddat">Muddati:</label>
        <input type="datetime-local" id="muddat" name="muddat" required>
        <br>
        <br>
       <label for="muhimlik_darajasi">Muhimlik darajasi:</label>
        <select id="muhimlik_darajasi" name="muhimlik_darajasi">
            <option value="past">Past</option>
            <option value="orta">O'rta</option>
            <option value="yuqori">Yuqori</option>
        </select>
        <br>
        <br>
        <button type="submit">Vazifani saqlash</button>
    </form>
    <script>
        // Ваш JavaScript код для валидации и других функций
    </script>
</body>
</html>
"""
    return HttpResponse(html)
