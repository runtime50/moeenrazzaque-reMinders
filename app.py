import json, requests, random

from flask import Flask, render_template, request

app = Flask(__name__)

# Information needed for Notion API to work (token obtained by going to https://www.notion.so/my-integrations, database_id depends on use case)
token = 'secret_VehP61kZI5lUS7Lpj5qOTmyXtwjuHh0ZQYP5b5aYxFv'
database_id = 'db328d289b3e47d1a0ab058d01bc88dd'
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def readDatabase(database_id, headers):
    # Requests the Notion API to view the content of the datasbase specified with database_id
    readUrl = f"https://api.notion.com/v1/databases/{database_id}/query"
    res = requests.request("POST", readUrl, headers=headers)

    # Logic to ensure the API requeset went through
    if res.status_code != 200:
        print(f"Error:  {res.status_code}")

    # Storing the request (JSON format) into the data variable
    data = res.json()

    # Calculates number of database entries to correcrtly look through JSON data and obtain the id of a random entry in database
    index_range = len(data['results']) - 1
    list_index = random.randint(0, index_range)
    entry_page_id = data['results'][list_index]['id']
    return entry_page_id

def searchPage(page_id, headers):
    # Requests the Notion API to search within the randomly chosen page, accessing the "blocks" of data inside
    readUrl = f"https://api.notion.com/v1/blocks/{page_id}/children"
    res = requests.request("GET", readUrl, headers=headers)

    # Logic to ensure the API request went through
    if res.status_code != 200:
        print(f"Error:  {res.status_code}")

    # Storing the request (JSON format) into the data variable, and making sure that the entry has some children element inside of it
    data = res.json()
    if data['results'] == []:
        return "This is an entry with no associated page."

    # Generating a random index to find a random entry within the Notion page to output
    index_range = len(data['results']) - 1
    list_index = random.randint(0, index_range)

    # Logic to try a variety of format options, ensuring that all desired text is outputted
    try:
        text = data['results'][list_index]['paragraph']['rich_text'][0]['plain_text']
    except KeyError:
        try:
            text = data['results'][list_index]['bulleted_list_item']['rich_text'][0]['plain_text']
        except KeyError:
            try:
                text = data['results'][list_index]['numbered_list_item']['rich_text'][0]['plain_text']
            except KeyError:
                try:
                    text = data['results'][list_index]['toggle']['rich_text'][0]['plain_text']
                except KeyError:
                    try:
                        text = data['results'][list_index]['to_do']['rich_text'][0]['plain_text']
                    except:
                        # Catch-all case if using an unsupported Notion block
                        text = "UNSUPPORTED NOTION FORMAT"
    return text

@app.route("/", methods=["GET"])
def index():
    # Only using "GET" as never taking any data from user
    if request.method == "GET":
        # Running previously defined functions to generate a random tidbit of knowledge from my database of notes, then rendering to page
        entry_id = readDatabase(database_id, headers)
        output = searchPage(entry_id, headers)
        return render_template("index.html", output=output)