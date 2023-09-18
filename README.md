# streamlit-reddit-comment-search
 A self-hosted website to search and save Reddit user comment history using Python, Streamlit and the Reddit API.
 ___
<h3>Installation and Setup</h3>
<br>


* Tested with [Python 3.9](https://www.python.org/downloads/release/python-390/)
<br>
<details>
<summary>
 Generate a Reddit API 'client_id' and 'client_secret'
</summary>
 <br>

 1. Click on Create a new app in the Reddit app console: https://www.reddit.com/prefs/apps
 2. Name the app 'Reddit Comment Search'
 3. Select 'Script' from the list of radio buttons
 4. Add the description 'A python script to search through Reddit comment history."
 5. Use your public IP address as the 'About URL' and the 'Redirect URI'
 6. Confirm your status as a human
 7. The client_id will be the short-ish string of random characters underneath the name of the application
 8. The client_secret will be the "secret" listed under the application when you click on edit application
</details>

<br>


Once you have your Reddit API details, Update these values in the search.py file:
```
client_id="XXX"
client_secret="XXX"
```

Save the search.py file and then use the run.bat file to handle the required dependencies and run the script:
```
run.bat
```

The following page will automatically launch in your browser once the dependencies have been installed/checked:
```
http://localhost:1198/
```

You can search for a username, query the comments and filter the date range.

The resulting comments are then individually saved as text files in the 'comments' folder using the filename format:
```
timestamp - username - query.txt
```

___
<h3>Troubleshooting</h3>

Open TCP Network Port 1198 to allow communication with Streamlit.


___
<h3>Dependencies</h3>

* [Streamlit](https://pypi.org/project/Streamlit/)
* [PRAW](https://pypi.org/project/praw/)

___

[@GabrielNezovic](https://github.com/GabrielNezovic) 2023
