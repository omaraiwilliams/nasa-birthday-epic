# <nasa-birthday-epic>

<1 to 2 sentences on what your program does with
NASA EPIC data>

## How it works
Function 1: get_epic_photos(api_key, date)
Description: Makes the API request for one date and returns the raw photo records exactly as NASA sends them. It only handles the request and error checking. It does not select, rename, or reformat any data.

Function 2: collect_birthdays(api_key, month_day, years)
Description: Builds one birthday date per year, fetches that year’s photos with get_epic_photos, and condenses each year’s raw records into a single summary. It counts the photos, takes the first photo’s timestamp and center coordinates, and builds the image URL from that photo’s date and image keys. Years with no photos or a failed request are left out.

Function 3: find_highlights(birthday_data)
Description: Loops through the birthday dictionary to find the year with the most photos and the year whose first photo had the northernmost center latitude

## How to run
1. Install requests: pip install requests
2. Run: python <your_file_name>.py
3. Uses "DEMO_KEY" by default. Swap in your own key
   from api.nasa.gov for higher rate limits.

## Built with
Python, requests and the NASA EPIC API
