from django.shortcuts import render
from datetime import datetime

def book_detail_list(request):
    # Пример данных (в реальном проекте - из базы данных)
    posts = [
        {
            'title': 'мой первый пост',
            'content': 'Это содержание моего первого поста в блоге. Здесь я рассказываю о том, как начал изучать Django.',
            'published_date': datetime(2024, 1, 15),
            'author': 'ADMIN'
        },
        {
            'title': 'второй пост о django',
            'content': 'Во втором посте я хочу поделиться впечатлениями о работе с шаблонами Django. Это очень удобно!',
            'published_date': datetime(2024, 1, 20),
            'author': 'AUTHOR'
        }
    ]
    # Рендерим шаблон и передаем данные в контексте
    return render(request, 'book_detail/book_detail_list.html', {'posts': posts})

def about(request):
    return render(request, 'book_detail/about.html')
