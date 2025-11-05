import requests
from django.shortcuts import render

def dog_breeds(request):
    # Получаем список всех пород
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    breeds = list(response.json()['message'].keys())

    selected_breeds = []
    images = {}
    # Если пользователь отправил породы через форму
    if request.method == "POST":
        input_breeds = request.POST.get('breeds', '')
        selected_breeds = [b.strip().lower() for b in input_breeds.split(',')]
        for breed in selected_breeds:
            img_url = f"https://dog.ceo/api/breed/{breed}/images/random"
            img_res = requests.get(img_url)
            if img_res.status_code == 200 and img_res.json()["status"] == "success":
                images[breed] = img_res.json()["message"]
            else:
                images[breed] = None

    return render(
        request,
        "dogs/dog_breeds.html",
        {
            "breeds": breeds,
            "images": images,
            "selected_breeds": selected_breeds
        }
    )
