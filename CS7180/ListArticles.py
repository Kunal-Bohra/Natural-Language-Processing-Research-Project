# ---------------------------Import Section Begins----------------------------#

import requests
import json

# ----------------------------Import Section Ends-----------------------------#


# ----------------------------Constants Section Begins------------------------#

api_public_key = "bchEgB1DO3EApFlZDcYtkvxqUa9xhdJlzj03K9bvgUH0vr1zfNpBA14AaXpt7YIB"

api_secret_key = "Bb8XyOKTBGfH4thoEj1hBISsuqI7gKURlbbXtHk45NW5w0l4fMFuBAE85oQT5965"

api_public_key2 = "zmLeN58T8R3tC0xcZBQLI6ijRpDGlOiAzouKFjyGDgKmIMdsUI5Q0BOUfoF6DSQ5"

api_secret_key2 = "OPWiFNzaffNiiSlwDL41yga9QnhmoLL5Aif5SKlxm6UU2xf0joXn8CVJQH3dvIgP"

forum = "wired"

popular_thread_url = "https://disqus.com/api/3.0/threads/listPopular.json?api_key=" + api_public_key + "&forum=" + forum + "&limit=100" + "&interval=90d"
popular_thread_task = "popular_thread"

list_thread_url = "https://disqus.com/api/3.0/threads/list.json?api_key=" + api_public_key + "&forum=" + forum + "&limit=100"
list_thread_task = "list_thread"

list_post_url = "https://disqus.com/api/3.0/threads/listPosts.json?api_key=" + api_public_key2 + "&limit=100" + "&thread="
list_post_task = "list_post"

user_detail_url = "https://disqus.com/api/3.0/users/details.json?api_key=" + api_public_key + "&user:username="

response_string = "response"
# ----------------------------Constants Section Ends--------------------------#


# ----------------------------Functions Section Begins------------------------#
'''
Input: Any URL adhering to DISQUS API documentation.
Output: JSON response returned by DISQUS API.
'''


def call_url(url):
    response = requests.get(url)
    api_response = json.loads(response.content)  # Load as JSON
    # print json.dumps(parsed, indent=4, sort_keys=True)
    return api_response  # Return a dictionary type object


'''
Input: Dictionary returned by call_url(url) method and a string which indicates the required value from an item of list
       and type/task of processing.
Output: A data structure containing values from JSON response' items.
'''


def generate_article_metadata(task):
    article_metadata = {}  # Initialize the metadata map to be returned
    output_value = []  # Initialize a list of value to be returned
    next_page_cursor = ""

    if task == popular_thread_task:
        api_response = call_url(popular_thread_url)
        parsed_response = api_response[
            response_string]  # Get the value list of dicts corresponding to key "response"
        for i in range(len(parsed_response)):  # Loop over the list and get the item needed
            current_link_value = parsed_response[i]['link']  # Get the required value from the current item in list
            output_value.append(str(current_link_value))  # Add link string to the list
        return output_value  # Return the list of values

    else:
        for i in range(150):  # Loop n times and each time fetch 100 articles
            if i == 0:
                print i
                new_url = list_thread_url  # Same lnk to begin with
                api_response = call_url(new_url)  # Call the API
                parsed_response = api_response[
                    response_string]  # Get the value list of dicts corresponding to key "response"
                cursor = api_response["cursor"]
                next_page_cursor = cursor["next"]
            else:
                print i
                new_url = list_thread_url + "&cursor=" + next_page_cursor  # Add cursor to get next page and so on
                api_response = call_url(new_url)  # Call the API
                parsed_response = api_response[
                    response_string]  # Get the value list of dicts corresponding to key "response"
                new_cursor = api_response["cursor"]
                next_page_cursor = new_cursor["next"]

            for j in range(len(parsed_response)):  # Loop over the list and get the item needed.
                current_post_value = parsed_response[j][
                    'posts']  # Get the required value from the current item in list
                if int(current_post_value) > 50:
                    article_id = parsed_response[j]['id']
                    article_author = str(parsed_response[j]['author'])
                    article_category = str(parsed_response[j]['category'])
                    article_created = str(parsed_response[j]['createdAt'])
                    article_title = parsed_response[j]['clean_title'].encode('ascii', 'ignore')
                    article_posts = str(parsed_response[j]['posts'])
                    article_link = str(parsed_response[j]['link'])
                    article_metadata[article_id] = (article_title, article_author, article_category, article_created,
                                                    article_posts, article_link)
    return article_metadata


'''
Input: List of thread id of of articles
Output: Map where key is thread_id and value if a list of tuples where each tuple if of form
(a,b,c) where a is thread_id of the comment, b is author username and c is comment text.
'''


def generate_posts_data(thread_id_list):
    comments_map = {}  # Init the map.
    for j in range(len(thread_id_list)):
        current_thread_id = thread_id_list[j]  # Get the thread id from list
        comments_map[current_thread_id] = []  # Init the entry in map. We will add tuples (a,b,c) to this list below

        updated_url = list_post_url + str(current_thread_id)
        api_response = call_url(updated_url)
        parsed_response = api_response[
            response_string]  # Get the value list of dicts corresponding to key "response"

        for i in range(len(parsed_response)):  # Loop over the response and get the item needed after parsing
            is_top_level_comment = parsed_response[i]["parent"]  # Yes, if null.
            if is_top_level_comment is None and 'username' in parsed_response[i][
                'author']:  # Fetch only those posts which are top level comments
                # print str(parsed_response[i]['author'])
                post_author_name = str(parsed_response[i]['author']['username'])
                # print post_author_name
                post_text = parsed_response[i]['raw_message'].encode('ascii', 'ignore')  # Get the post text value
                author_post_tuple = (current_thread_id, post_author_name, post_text)  # Create the tuple (a,b, c)
                comments_map[current_thread_id].append(author_post_tuple)  # Insert the tuple in list.
    return comments_map  # Return the map.


'''
Input: List of user ids
Output: Map consisting of user's metadata.
'''


def generate_commenters_data(commenter_id_list):

    usermap = {}  # Init the map to store users and their metadata as key, value respectively
    print commenter_id_list
    for j in range(len(commenter_id_list)):
        current_user_id = commenter_id_list[j]
        updated_user_detail_url = user_detail_url + str(current_user_id)
        api_response = call_url(updated_user_detail_url)
        parsed_response = api_response[
            response_string]  # Get the value list of dicts corresponding to key "response"
        num_of_followers = str(parsed_response['numFollowers'])
        num_of_following = str(parsed_response['numFollowing'])
        num_of_comments = str(parsed_response['numPosts'])
        num_of_likes_received = str(parsed_response['numLikesReceived'])
        reputation = str(parsed_response['reputation'])
        current_user_metadata = (current_user_id, num_of_comments, num_of_followers, num_of_following,
                                     num_of_likes_received, reputation)
        usermap[current_user_id] = current_user_metadata

    return usermap


'''
Main function
'''


def main():
    # popular_thread_response = call_url(popular_thread_url)  # Call the API
    # popular_thread_links = generate_article_metadata("link", "popular_thread")
    # print len(popular_thread_links)

    # Init the files
    links_file = open("C:\Users\Owner\Desktop\Data\links.txt", 'w')

    article_metadata_file = open("C:\Users\Owner\Desktop\Data\\article_metadata_wired.txt", 'w')
    article_metadata_file.write('current_article_id' + '\t' + 'article_title' + '\t' + 'article_author' + '\t' +
                                'article_category' + '\t' + 'article_created' + '\t' + 'article_posts' + '\t' +
                                'article_link' + '\n')

    comment_file = open("C:\Users\Owner\Desktop\Data\\article_comments.txt", 'w')
    comment_file.write('current_comment_thread_id' + '\t' + 'current_comment_author' + '\t' + 'current_comment_text' +
                       '\n')

    user_metadata_file = open("C:\Users\Owner\Desktop\Data\\user_metadata_wired.txt", 'w')
    user_metadata_file.write('user_id' + '\t' + 'num_of_comments' + '\t' + 'num_of_followers' + '\t' +
                             'num_of_following' + '\t' + 'num_of_likes_received' + '\t' + 'reputation' + '\n')

    article_ids = []  # Init a list to store the links and then write them to a file for scrapping.
    comment_author_ids = []  # Init the list to store ids of all users who made comments

    articles = generate_article_metadata("list_thread")
    for article in articles:
        current_article_metadata = articles[article]

        # Write the link to a file and store to a list for other function to use.
        current_article_link = str(current_article_metadata[-1])
        current_article_id = str(article)
        article_ids.append(current_article_id)
        links_file.write(current_article_link + "\n")

        # Write article's metadata to a file
        article_title = current_article_metadata[0].encode('ascii', 'ignore')
        article_author = str(current_article_metadata[1])
        article_category = str(current_article_metadata[2])
        article_created = str(current_article_metadata[3])
        article_posts = str(current_article_metadata[4])
        article_link = str(current_article_metadata[5])

        article_metadata_file.write(current_article_id + '\t' + article_title + '\t' + article_author + '\t' +
                                    article_category + '\t' + article_created + '\t' + article_posts + '\t' +
                                    article_link + '\n')

    print len(article_ids)


    # Generate comments data dump
    comments_map = generate_posts_data(article_ids)
    for key in comments_map:
        current_comment_list = comments_map[key]

        for comment in current_comment_list:
            current_comment_thread_id = str(comment[0])
            current_comment_author = str(comment[1])
            current_comment_text = comment[2].encode('ascii', 'ignore')

            # Write to the output file.
            comment_file.write(current_comment_thread_id + '\t' + current_comment_author + '\t' + current_comment_text +
                               '\n')
            # Add comment author id to list for further processing.
            comment_author_ids.append(current_comment_author)

    print len(comment_author_ids)

    # # Generate user details data dump
    # user_map = generate_commenters_data(comment_author_ids)
    # for user_id in user_map:
    #     current_user_metadata = user_map[user_id]
    #
    #     num_of_comments = str(current_user_metadata[1])
    #     num_of_followers = str(current_user_metadata[2])
    #     num_of_following = str(current_user_metadata[3])
    #     num_of_likes_received = str(current_user_metadata[4])
    #     reputation = str(current_user_metadata[5])
    #
    #     user_metadata_file.write(user_id + '\t' + num_of_comments + '\t' + num_of_followers + '\t' +
    #                              num_of_following + '\t' + num_of_likes_received + '\t' + reputation + '\n')
    #
    # # Debug statements
    # print("Num of Articles:")
    # print len(articles)
    # print("Num of Article Ids:")
    # print len(article_ids)
    # print("Num of Comments:")
    # print len(comments_map)
    # print("Num of Commenter:")
    # print len(comment_author_ids)
    # print len(user_map)
    # # Close file handlers
    # links_file.close()
    # article_metadata_file.close()
    # comment_file.close()
    #
    #
# ----------------------------Functions Section Ends--------------------------#

if __name__ == "__main__":
    main()
