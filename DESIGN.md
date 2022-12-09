
# Overview

reMinders uses Python to access the Notion API, sending HTTP requests to access data inside a defined database. From there, the website randomly generates any text found within that database of pages, with the intention of reminding the user of any tidbits of knowledge they may have forgotten. The user can access and display new pieces of knowledge by pressing on the "Generate" button, which through a Flask HTML implementation produces new information by sending requests to the Notion API.


# Implementation: Backend

reMinders was created by using Python to send HTTP requests to the Notion API (accessed through https://api.notion.com), and then manipulating the JSON data received to perform the expected functionality. To do this, let's walk through app.py where the specific implementation of the backend of reMinders lies.

Of course, like any Python script, we begin by importing a variety of libraries that will be used throughout the program. The most important, besides Flask which is used to connect the frontend and backend, are json (used for data manipulation), requests (used to send HTTPS requests to the Notion API), and random (used to help with choosing random pieces of information to generate).

From there, to actually use the Notion API, the API token, database ID, and necessary headers are defined. This is all so that we can access the right version of the API and have the right level of access to retrieve information from our own Notion account. You can read more about the specific header implementation over at https://developers.notion.com/reference/authentication, where the Notion team outlines what exact values they look for when authenticating the HTTP request.

> *Note: Not described below are the variety of checks I perform throughout app.py to make sure the data received is valid. It's there, but not significant and the code (with it's comments) should explain itself thoroughly*

The first function of interest is readDatabases, which takes in the database ID and headers as its two parameters. It sends a HTTP POST request querying the database, and then stores the received data in a variable that can be further manipulated. It does some math to find the right range of values available to index, and then generates a random index value to plug into a JSON search, retrieving the specific page ID of the database entry.

From there, the next function, searchPage, takes in the a page ID (likely generated from readDatabases) and the previously defined headers, and then sends another HTTP request, this time to access the content of a specific page. It stores the information, calculates the available index range, and then performs a number of search requests to find one that returns a text value to output.

> *Note: While the nested try statements looks messy, it was the simplest and most effective solution I found. I tried using a for loop with a list but it did not work as expected with the try statement.*


# Implementation: Frontend

With the frontend, I used a simple approach of using Flask to connect my HTML with a Python-based backend. You may have noticed that I included my CSS inline within my HTML, and that is because I did not have much of it. Also, there was a bug where my style.css file did not link to my HTML, and to avoid that from happening, I simply embedded all of my styling within the webpage itself. This apporach has the added benefit of the webpage content always loading accurately styled, in the case of any packet loss.

At the bottom of app.py, I call the two previously defined function and plug in their output into a return template request that updates the "output" value in my HTML with what the function returns. Heading over to index.html, you can see the only thing changing is the paragraph element with the name="output." This is because I am only ever getting information from my backend, never sending any. From there, I use a style HTML button element, embedded within the form with the "GET" method, to indicate to the backend that I'd like to push a new request to my Python script.

The rest of index.html contains a simply webpage structure, with a logo, a couple of text elements, and some visual elements to make it all look nice. I also have supplemented every element with custom CSS styling to make the webpage look interesting and visually dynamic.