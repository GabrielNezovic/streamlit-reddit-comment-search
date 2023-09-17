# streamlit-reddit-comment-search
 A self-hosted website to search and save Reddit user comment history using Python, Streamlit and the Reddit API.
<br>
<br>

<details>
<summary>HOW TO: Generate a Reddit API 'CLIENT_ID' and 'CLIENT_SECRET'</summary>
 

 1. Click on Create a new app in the reddit app console: https://www.reddit.com/prefs/apps
 2. Name the app 'Reddit Comment Search'
 3. Select 'Script' from the list of radio buttons
 4. Add ther description 'A python script to search through reddit comment history."
 5. Use your public IP address as the about url and the redirect uri
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

It should automatically load the website in your browser on launch:
```
http://localhost:1198
```

You can search for username, query and a date range.

The search results are individually saved as text files in the 'comments' folder with the filename format:
```
timestamp - username - query.txt
```
