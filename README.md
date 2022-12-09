
# Overview

reMinders uses Python to access the Notion API, sending HTTP requests to access data inside a defined database. From there, the website randomly generates any text found within that database of pages, with the intention of reminding the user of any tidbits of knowledge they may have forgotten. The user can access and display new pieces of knowledge by pressing on the "Generate" button, which through a Flask HTML implementation produces new information by sending requests to the Notion API.


# Setting Up

To use, first download all of the source code and navigate to the folder's filepath in your terminal. Make sure that Flask is installed and updated, and then run "flask run" in the root directory. From there, you can see the site and customize it to your liking. Right now, the software is only designed to work with the Notion integration I set up when developing (a sample "Knowledge" database with a variety of pages embedded within it). However, you can actually connect your own Notion account to then use this feature on a database of your own!

To do this, all you have to do is connect your own Notion account (done through a Notion "token" of sorts (API key for those more familiar) and the specific database ID of the database you are trying to use. First, you need to have a Notion account and create a workspace (or use your own existing workspace).

> *Note: You need to have Admin level access to the workspace you'd like to use with the reMinders application*.

From there, either create a database (you can input "/" followed with database in your desired Notion page, optionally opting for a full database rather than inline) or find a pre-existing one you'd like to use. While you're there, obtain its database ID by observing the 32 character string in the URL starting with "db" and ending right before the "?". You can find this string right after the name of your Notion workspace in the URL.

To have the API work with your account, you'll need to provide your own Notion key, done by setting up an integration over at https://www.notion.so/my-integrations. You'll have to set up an integration for your own account, and then link that integration with the database provided by navigating back to your database (once the integration is set up), clicking on the three dots in the right-hand corner, and adding the integration under the Connections menu.

Lastly, take the Integration key (starting with "secret_") and replace the predefined token variable in app.py with your key, and replace the predefined database ID in app.py with yours, and reMinders can now work with your database!

> Again, for the purposes of the reMinders application, you can just use the given set up to test whether or not the software works.


# Use

Whether you decided to use your own Notion database or my preset one, now you can try out the functionality of the application! Using it is very simple; once the Flask is up and running, you can then press the "Generate" button to procure a random tidbit to learn from! There really isn't anything else to it... reMinders is meant to have a very simple interface, although the backend is quite complicated with all of the API requesting it has to do.

If you opted to use your own Notion database, there are some important things to note. First, currently the supported data types that will be outputted are of the following: plain text, bullet point blocks, numbered blocks, toggle blocks, and to do  blocks. All other formats are currently unsupported, but this is by design as many times headings and other formats are more aimed at structuring a document rather than providing the content you'd like to be reminded of.

Another important thing to note is that the database retrieves the pages of the items within your database, not the items in the database itself. You can modify the code if you'd like to change that feature, simply removing the searchPage function and altering the readDatabase function with a JSON query to retrieve the entry title in the column you desruire (see the previously defined querty for reference, or visit the Notion API reference at https://developers.notion.com/reference/intro). So, if you have a database with the pages "Reflections," "Lecture Notes," and "Reminders," the application will crawl inside those pages and return the information inside of them, not the strings "Reflections," "Lecture Notes," and "Reminders," making it quite a powerful tool.

Lastly, the software currenly operates on the assumption that your database stores the pages linked in a column aptly named "Name." If you are using a database with a different column name, you can change the JSON query to reflect that.

# YouTube Video

Link: https://youtu.be/bu8bWoArPZs