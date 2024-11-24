from django.http import HttpResponse

def task_create(request):
    html = """
<!DOCTYPE html>
<html>
<head>
    <title>Создать новую задачу</title>
    <link rel="stylesheet" href="style.css"> </head>
<body>
    <h1>Yangi vazifa yaratish</h1>
    <form>
        <label for="taskName">Vazifa nomi:</label>
        <input type="text" id="taskName" name="taskName">

        <br>
        <br>

        <label for="description">Tavsif:</label>
        <textarea id="description" name="description"></textarea>
        
        <br>
        <br>
        
        <label for="deadline">Vazifa muddati:</label>
        <input type="date" id="deadline" name="deadline">
        
        <br>
        <br>

        <label for="model">Muhimlilik darajasi:</label>
        <select id="model" name="model">
            <option value="model1">Past</option>
            <option value="model2">O'rta</option>
            <option value="model2">Yuqori</option>
        </select>
    
        <br>
        <br>

        <button type="submit" >Yaratish</button>
    </form>
    <script src="script.js"></script> </body>
</html>
"""
    return HttpResponse(html)
