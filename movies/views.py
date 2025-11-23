from django.shortcuts import render

def index(request):
    movies = [
        {
            'title': 'THe Bad Guys',
            'description': 'Мультфильм «Плохие парни» рассказывает о банде антропоморфных животных-преступников, которые ради спасения от тюрьмы решают притвориться хорошими, но в итоге обнаруживают, что им нравится быть добрыми, и предотвращают злодейский план',
            'poster': 'the.jpg',
            'trailer': 'https://youtu.be/d8XnK14-x_A?si=ubiwVMYp3Z1JRgl1',
        },
        {
            'title': 'МегаМозг',
            'description': 'В мультфильме «Мегамозг» суперзлодей побеждает супергероя, но, потеряв смысл жизни, создает нового противника, который сам становится угрозой для города, вынуждая Мегамозга стать настоящим героем.',
            'poster': 'mozg.jpg',
            'trailer': 'https://youtu.be/AFwrmkAHEk4?si=uVdTgMNnkqcX8Hyh',
        },
        {
            'title': 'Гарри Потер и философский камень',
            'description': 'Гарри Поттер узнает, что он волшебник, и в школе Хогвартс предотвращает похищение философского камня злодеем.',
            'poster': 'mrpoter.jpg',
            'trailer': 'https://youtu.be/AFwrmkAHEk4?si=uVdTgMNnkqcX8Hyh',
        }
    ]
    return render(request, 'movies/index.html', {'movies': movies})