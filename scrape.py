import csv
from google_play_scraper import Sort, reviews_all

# Daftar filter skor
filter_scores = [1, 2, 3, 4, 5]

result = []

# Loop untuk filter skor
for score in filter_scores:
    # Loop untuk tipe sort "MOST_RELEVANT" dan "NEWEST"
    for sort_type in [Sort.MOST_RELEVANT, Sort.NEWEST]:
        reviews = reviews_all(
            'id.ac.ub.gapura_mobile',
            sleep_milliseconds=0,
            lang='id',
            country='id',
            sort=sort_type,
            filter_score_with=score
        )
        result.extend(reviews)

csv_file = 'reviews_test2.csv'

# Ambil keys dari data pertama
fieldnames = result[0].keys()

# Write the reviews to the CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(result)

print('Reviews saved to CSV file:', csv_file)


