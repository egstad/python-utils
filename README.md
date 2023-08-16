# Python utils

## 1. Reshape large datasets

These modules take large datasets and convert them into smaller, nicely formatted shapes. Sometimes I like to export them as `csv`'s so I can play with them within Google Sheets. Other times I convert them into `json`. Neat.

- [1_convert_database_to_csv.py](1_convert_database_to_csv.py)
- [1_convert_database_to_json.py](1_convert_database_to_json.py)

## 2. Scrape images from webpages

There's been a few times now where I need to scrape data (specifically images) from MANY webpages. I created this module for that.

- [2_download_images_from_json.py](2_download_images_from_json.py)

## 3. Convert CSV to JSON

Earlier I mentioned that I sometimes like to play with data in Google Sheets. That's because I'm sorta boo-boo at python. Unfortunately GS doesn't offer a json export. But they do offer a CSV export!!!! Thank god. Once doing so, run that file through this module and you'll have a nice little json file.

- [3_convert_csv_to_json.py](3_convert_csv_to_json.py)
