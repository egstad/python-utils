"""Module that let's us add/edit json"""
import json
import csv


# Edit vars below to edit location
DIR_OLD = "data-old/"
DIR_NEW = "data-new/"

# Edit vars below to define input (old) and output (new) file names
FILE_OLD = "all-cards-20230721092742.json"
# FILE_OLD = "unique-artwork-sample.json"
FILE_NEW = "database.csv"


# Pipe old (input) database into var called 'data_old'
# Then create temp array for new (output) json called 'data_new'
with open(DIR_OLD + FILE_OLD, "r", encoding="utf-8") as database:
    data_old = json.load(database)
    data_new = []


def shape_and_write_csv():
    """Transfer only what we need from data_old to data_new"""
    index_count = 0

    with open(DIR_NEW + FILE_NEW, "a", encoding="utf-8") as csvfile:
        fieldnames = ["index", "title", "content", "description"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    # then write the rows
    for obj in data_old:
        if (
            obj.get("image_uris")
            and obj.get("image_uris").get("border_crop")
            and obj.get("lang") == "en"
            and obj.get("highres_image")
        ):
            content = obj["image_uris"]["border_crop"]
            title = obj["name"] if obj.get("name") else ""
            description = obj["type_line"] if obj.get("type_line") else ""

            with open(DIR_NEW + FILE_NEW, "a", encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(
                    {
                        "index": index_count,
                        "title": title.encode("unicode_escape").decode("utf-8"),
                        "content": content,
                        "description": description.encode("unicode_escape").decode(
                            "utf-8"
                        ),
                    }
                )

            print("✅ " + title + " added!")
            index_count += 1
        else:
            print("🛑 " + str(index_count) + " skipped!")


def init():
    """initialize file: shape data and write it so json file'"""
    print("shaping data!")
    shape_and_write_csv()


init()
