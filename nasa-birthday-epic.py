import requests

BASE_URL = "https://api.nasa.gov/EPIC"


def get_epic_photos(api_key, date):
    url = f"{BASE_URL}/api/natural/date/{date}"
    try:
        response = requests.get(url, params={"api_key": api_key})
    except requests.exceptions.RequestException:
        return None

    if response.status_code != 200:
        return None
    return response.json()


def collect_birthdays(api_key, month_day, years):
    birthday_data = {}

    for year in years:
        photos = get_epic_photos(api_key, f"{year}-{month_day}")
        if not photos:  # None or empty list
            continue

        first = photos[0]
        date_path = first["date"][:10].replace("-", "/")  # "2020/08/13"
        birthday_data[year] = {
            "count": len(photos),
            "time": first["date"],
            "lat": first["centroid_coordinates"]["lat"],
            "lon": first["centroid_coordinates"]["lon"],
            "url": f"{BASE_URL}/archive/natural/{date_path}/png/{first['image']}.png?api_key={api_key}",
        }

    return birthday_data


def find_highlights(birthday_data):
    if not birthday_data:
        return None

    most_photos = None
    northernmost = None
    for year in birthday_data:
        if most_photos is None or birthday_data[year]["count"] > birthday_data[most_photos]["count"]:
            most_photos = year
        if northernmost is None or birthday_data[year]["lat"] > birthday_data[northernmost]["lat"]:
            northernmost = year

    return {"most_photos": most_photos, "northernmost": northernmost}


def main():
    api_key = "DEMO_KEY"
    birthday_data = collect_birthdays(api_key, "08-13", range(2016, 2026))

    for year, info in birthday_data.items():
        print(year, info["count"], "photos | first at", info["time"],
              "| center", info["lat"], info["lon"])
        print("  ", info["url"])

    print(find_highlights(birthday_data))


main()
