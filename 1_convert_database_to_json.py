"""Module that let's us add/edit json"""
import json


# Edit vars below to edit location
DIR_OLD = "data-old/"
DIR_NEW = "data-new/"

# Edit vars below to define input (old) and output (new) file names
FILE_OLD = "all-cards-20230721092742.json"
# FILE_OLD = "unique-artwork-sample.json"
FILE_NEW = "database.json"


# Pipe old (input) database into var called 'data_old'
# Then create temp array for new (output) json called 'data_new'
with open(DIR_OLD + FILE_OLD, "r", encoding="utf-8") as database:
    data_old = json.load(database)
    data_new = []


def shape_json_data():
    """Transfer only what we need from data_old to data_new"""
    index_count = 0

    for obj in data_old:
        if (
            obj.get("image_uris")
            and obj.get("image_uris").get("border_crop")
            and obj.get("lang") == "en"
            and obj.get("highres_image")
        ):
            content = obj["image_uris"]["border_crop"]
            title = obj["name"] if obj.get("name") else ""
            description = obj["oracle_text"] if obj.get("oracle_text") else ""

            data_new.append(
                {
                    "index": index_count,
                    "content": content,
                    "title": title,
                    "description": description,
                }
            )
            index_count += 1

            print("✅ " + title + " added!")
        else:
            print("🛑 " + str(index_count) + " skipped!")


def write_to_json_file():
    """Create a new json file and pipe in 'data_new'"""
    with open(DIR_NEW + FILE_NEW, "r+", encoding="utf-8") as outfile:
        json.dump(data_new, outfile, indent=2)


def init():
    """initialize file: shape data and write it so json file'"""
    print("shaping data!")
    shape_json_data()
    print("writing to new file!")
    write_to_json_file()


init()
