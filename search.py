import praw
import datetime
import os
import streamlit as st

# HOW TO: Generate a Reddit API 'client_id' and 'client_secret' #

# 1. Click on Create a new app in the reddit app console: https://www.reddit.com/prefs/apps
# 2. Name the app 'Reddit Comment Search'
# 3. Select 'Script' from the list of radio buttons
# 4. Add the description 'A python script to search through reddit comment history."
# 5. Use your public IP address as the about url and the redirect uri
# 6. Confirm your status as a human
# 7. The client_id will be the short-ish string of random characters underneath the name of the application
# 8. The client_secret will be the "secret" listed under the application when you click on edit application

# Set up the Reddit API credentials
reddit = praw.Reddit(
    client_id='XXX',
    client_secret='XXX',
    user_agent='Reddit API Script'
)

def search_comments_by_user(username, query, date_range):
    # Get the Reddit user
    user = reddit.redditor(username)

    # Convert date_range to an integer
    date_range = int(date_range)

    # Calculate the start and end dates based on the current date and days in the past
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=date_range)

    # Convert the dates to Unix timestamps
    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())

    # Get the comments by the user within the date range
    comments = user.comments.new(limit=None)

    # Create a folder named "comments" if it doesn't exist
    if not os.path.exists("comments"):
        os.makedirs("comments")

    # Search for matching comments
    for comment in comments:
        if comment.created_utc >= start_timestamp and comment.created_utc <= end_timestamp:
            if query.lower() in comment.body.lower():
                # Generate the filename based on username and timestamp
                filename = f" {int(comment.created_utc)} - {username} - {query}.txt"
                # Save the comment content to a text file in the "comments" folder
                with open(os.path.join("comments", filename), "w", encoding="utf-8") as file:
                    file.write(comment.body)
                    st.success(filename)
def main():
    st.title("Reddit Comment Search")
    # Create the search input boxes
    with st.form("Search"):
        col1,col2,col3 = st.columns(3)
        with col1:
            username = st.text_input("Username", placeholder="Snoo")
        with col2:
            query = st.text_input("Search Query", placeholder="Alien")
        with col3:
            date_range = st.text_input("Date Filter", placeholder="365", help="Filter the comment history by X days from todays date, eg use '365' to search for the last 1 year of comments.''")
        # Retrieve and save matching comments
        if st.form_submit_button("Search Comments", type="secondary", use_container_width=True):
            with st.status("Search Results"):
                search_comments_by_user(username, query, date_range)
        
            st.success("Matching comments saved to the 'comments' folder.")
            
if __name__ == "__main__":
    main()