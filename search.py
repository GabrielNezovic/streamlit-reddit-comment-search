import praw
import datetime
import os
import streamlit as st

# HOW TO: Generate a Reddit API 'client_id' and 'client_secret' #
# 1. Click on Create a new app in the Reddit app console: https://www.reddit.com/prefs/apps
# 2. Name the app 'Reddit Comment Search'
# 3. Select 'Script' from the list of radio buttons
# 4. Add the description 'A python script to search through Reddit comment history."
# 5. Use your public IP address as the 'About URL' and the 'Redirect URI'
# 6. Confirm your status as a human
# 7. The client_id will be the short-ish string of random characters underneath the name of the application
# 8. The client_secret will be the "secret" listed under the application when you click on edit application

# Set up the Reddit API credentials
reddit = praw.Reddit(
    client_id='XXX',
    client_secret='XXX',
    user_agent='Reddit API Script'
)

# Convert unix timestamp to yyyymmddhhmmss
def unix_timestamp_to_formatted(timestamp):
    # Convert Unix timestamp to a datetime object
    dt_object = datetime.datetime.utcfromtimestamp(timestamp)

    # Format the datetime object as "yyyymmddhhmmss"
    formatted_timestamp = dt_object.strftime("%Y%m%d%H%M%S")

    return formatted_timestamp
    
# Search the Reddit comments
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
                # Convert Unix timestamp to formatted timestamp (yyyymmddhhmmss)
                formatted_timestamp = unix_timestamp_to_formatted(comment.created_utc)
                # Generate the filename based on username and timestamp
                filename = f"{formatted_timestamp} - {username} - {query}.txt"
                # Save the comment content to a text file in the "comments" folder
                with open(os.path.join("comments", filename), "w", encoding="utf-8") as file:
                    file.write(comment.body)
                    st.success(filename)
# Streamlit UI
def main():
    st.title("Reddit Comment Search")
    # Create the search input boxes
    with st.form("Search"):
        col1, col2, col3, col4  = st.columns(4)
        with col1:
            username = st.text_input("Username", placeholder="Username", label_visibility="collapsed")
        with col2:
            query = st.text_input("Search Query", placeholder="Search Query", label_visibility="collapsed")
        with col3:
            date_range = st.text_input("Date Filter", value="365", placeholder="Days to Filter", help="Filter the comment history by X days from today's date, e.g., use '365' to search for the last 1 year of comments.", label_visibility="collapsed")
        search_results = st.empty()
        search_results_message = st.empty()
        with col4:
            #Initialise the success session state
            if "success" not in st.session_state:
                st.session_state["success"] = False
            
            success = st.session_state["success"]
            
            # Set up the Submit Button
            submit_button = st.form_submit_button("Search", type="secondary", use_container_width=True)
        
            # Retrieve and save matching comments
            if submit_button:
                # Clear the prevous status message
                search_results_message.empty()
                
                #Display the search results
                with search_results.status("Search Results", expanded=True):
                    search_comments_by_user(username, query, date_range)
                #Display a success message
                search_results_message.success("Matching comments saved to the 'comments' folder.")
                
                # Set the Success sessions tate
                success = True
                st.session_state["success"] = success
                
        # Clear the list of previous search results
        success = st.session_state["success"]
        if success:
            search_results.empty()
            
# Run the Streamlit app
if __name__ == "__main__":
    main()