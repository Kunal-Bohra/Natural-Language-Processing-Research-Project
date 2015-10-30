# ---------------------------Import Section Begins----------------------------#

import requests
import json

# ----------------------------Import Section Ends-----------------------------#


# ----------------------------Constants Section Begins------------------------#

api_public_key1 = "G51myncNVoPZP0HRGLmE2wBsRJ6xMBRfYMem5w5v6Izppyb2OUnCFB9RgOO4v67U"
api_public_key2 = "CDwONliYQgHWG94ViguTQqdaxrV3IxCwwIPnKxIEGfo6lZEPve5KhSL0aNN3j6jj"
api_public_key3 = "5XMJzi1BGTeiy9H77cPcUxutPosqHMj47r6xB9xDD3aQoSqoo4mWKynIHBb10f8t"
api_public_key4 = "GoQ4ZrIvjvK6UIzbqwx5MV6O4LGN16i562R7IqBPOJXY4afAgZAyCWIcxLVIHgQ1"
api_public_key5 = "91pA9x8XJPyyRpNIiuqOST8srBHU7GYW8ONFX4nrhuXhwMJQjwbP00sdzRgWkgqV"
api_public_key6 = "xgeUt96SQzgGIFjT1L36s3JD0n177B4iz8uPPrZifeGWlniNpXzIeOPtoBp6rJt0"
api_public_key7 = "xgeUt96SQzgGIFjT1L36s3JD0n177B4iz8uPPrZifeGWlniNpXzIeOPtoBp6rJt0"
api_public_key8 = "sPaISRnOUxCCjZNEImCOG59dIzfNqX8MMDIw1q1bDZadLP6zd0MaiLkr90xrN0tp"

user_detail_url1 = "https://disqus.com/api/3.0/users/details.json?api_key=" + api_public_key1 + "&user:username="
user_detail_url2 = "https://disqus.com/api/3.0/users/details.json?api_key=" + api_public_key2 + "&user:username="
user_detail_url3 = "https://disqus.com/api/3.0/users/details.json?api_key=" + api_public_key3 + "&user:username="
user_detail_url4 = "https://disqus.com/api/3.0/users/details.json?api_key=" + api_public_key4 + "&user:username="
user_detail_url5 = "https://disqus.com/api/3.0/users/details.json?api_key=" + api_public_key5 + "&user:username="
user_detail_url6 = "https://disqus.com/api/3.0/users/details.json?api_key=" + api_public_key6 + "&user:username="
user_detail_url7 = "https://disqus.com/api/3.0/users/details.json?api_key=" + api_public_key7 + "&user:username="
user_detail_url8 = "https://disqus.com/api/3.0/users/details.json?api_key=" + api_public_key8 + "&user:username="

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
Input: List of user ids
Output: Map consisting of user's metadata.
'''


def generate_commenters_data(commenter_id_list):

    usermap = {}  # Init the map to store users and their metadata as key, value respectively

    commenter_id_list1 = commenter_id_list[:998]
    commenter_id_list2 = commenter_id_list[1000:1998]
    commenter_id_list3 = commenter_id_list[1999:2997]
    commenter_id_list4 = commenter_id_list[2998:3995]
    commenter_id_list5 = commenter_id_list[3996:4994]
    commenter_id_list6 = commenter_id_list[4995:5992]
    #commenter_id_list7 = commenter_id_list[5993:6990]
    #commenter_id_list8 = commenter_id_list[6991:]

    for j in range(len(commenter_id_list1)):
        print("List 1")
        current_user_id = commenter_id_list1[j]
        updated_user_detail_url = user_detail_url1 + str(current_user_id)
        api_response = call_url(updated_user_detail_url)
        parsed_response = api_response[
            'response']  # Get the value list of dicts corresponding to key "response"
        num_of_followers = str(parsed_response['numFollowers'])
        num_of_following = str(parsed_response['numFollowing'])
        num_of_comments = str(parsed_response['numPosts'])
        num_of_likes_received = str(parsed_response['numLikesReceived'])
        reputation = str(parsed_response['reputation'])
        current_user_metadata = (current_user_id, num_of_comments, num_of_followers, num_of_following,
                                     num_of_likes_received, reputation)
        usermap[current_user_id] = current_user_metadata

    for j in range(len(commenter_id_list2)):
        print("List 2")
        current_user_id = commenter_id_list2[j]
        updated_user_detail_url = user_detail_url2 + str(current_user_id)
        api_response = call_url(updated_user_detail_url)
        parsed_response = api_response[
            'response']  # Get the value list of dicts corresponding to key "response"
        num_of_followers = str(parsed_response['numFollowers'])
        num_of_following = str(parsed_response['numFollowing'])
        num_of_comments = str(parsed_response['numPosts'])
        num_of_likes_received = str(parsed_response['numLikesReceived'])
        reputation = str(parsed_response['reputation'])
        current_user_metadata = (current_user_id, num_of_comments, num_of_followers, num_of_following,
                                     num_of_likes_received, reputation)
        usermap[current_user_id] = current_user_metadata


    for j in range(len(commenter_id_list3)):
        print("List 3")
        current_user_id = commenter_id_list3[j]
        updated_user_detail_url = user_detail_url3 + str(current_user_id)
        api_response = call_url(updated_user_detail_url)
        parsed_response = api_response[
            'response']  # Get the value list of dicts corresponding to key "response"
        num_of_followers = str(parsed_response['numFollowers'])
        num_of_following = str(parsed_response['numFollowing'])
        num_of_comments = str(parsed_response['numPosts'])
        num_of_likes_received = str(parsed_response['numLikesReceived'])
        reputation = str(parsed_response['reputation'])
        current_user_metadata = (current_user_id, num_of_comments, num_of_followers, num_of_following,
                                     num_of_likes_received, reputation)
        usermap[current_user_id] = current_user_metadata


    for j in range(len(commenter_id_list4)):
        print("List 4")
        current_user_id = commenter_id_list4[j]
        updated_user_detail_url = user_detail_url4 + str(current_user_id)
        api_response = call_url(updated_user_detail_url)
        parsed_response = api_response[
            'response']  # Get the value list of dicts corresponding to key "response"
        num_of_followers = str(parsed_response['numFollowers'])
        num_of_following = str(parsed_response['numFollowing'])
        num_of_comments = str(parsed_response['numPosts'])
        num_of_likes_received = str(parsed_response['numLikesReceived'])
        reputation = str(parsed_response['reputation'])
        current_user_metadata = (current_user_id, num_of_comments, num_of_followers, num_of_following,
                                     num_of_likes_received, reputation)
        usermap[current_user_id] = current_user_metadata

    for j in range(len(commenter_id_list5)):
        print("List 5")
        current_user_id = commenter_id_list5[j]
        updated_user_detail_url = user_detail_url5 + str(current_user_id)
        api_response = call_url(updated_user_detail_url)
        parsed_response = api_response[
            'response']  # Get the value list of dicts corresponding to key "response"
        num_of_followers = str(parsed_response['numFollowers'])
        num_of_following = str(parsed_response['numFollowing'])
        num_of_comments = str(parsed_response['numPosts'])
        num_of_likes_received = str(parsed_response['numLikesReceived'])
        reputation = str(parsed_response['reputation'])
        current_user_metadata = (current_user_id, num_of_comments, num_of_followers, num_of_following,
                                     num_of_likes_received, reputation)
        usermap[current_user_id] = current_user_metadata

    for j in range(len(commenter_id_list6)):
        print("List 6")
        current_user_id = commenter_id_list6[j]
        updated_user_detail_url = user_detail_url6 + str(current_user_id)
        api_response = call_url(updated_user_detail_url)
        parsed_response = api_response[
            'response']  # Get the value list of dicts corresponding to key "response"
        num_of_followers = str(parsed_response['numFollowers'])
        num_of_following = str(parsed_response['numFollowing'])
        num_of_comments = str(parsed_response['numPosts'])
        num_of_likes_received = str(parsed_response['numLikesReceived'])
        reputation = str(parsed_response['reputation'])
        current_user_metadata = (current_user_id, num_of_comments, num_of_followers, num_of_following,
                                     num_of_likes_received, reputation)
        usermap[current_user_id] = current_user_metadata


    # for j in range(len(commenter_id_list7)):
    #     current_user_id = commenter_id_list7[j]
    #     updated_user_detail_url = user_detail_url7 + str(current_user_id)
    #     api_response = call_url(updated_user_detail_url)
    #     parsed_response = api_response[
    #         'response']  # Get the value list of dicts corresponding to key "response"
    #     num_of_followers = str(parsed_response['numFollowers'])
    #     num_of_following = str(parsed_response['numFollowing'])
    #     num_of_comments = str(parsed_response['numPosts'])
    #     num_of_likes_received = str(parsed_response['numLikesReceived'])
    #     reputation = str(parsed_response['reputation'])
    #     current_user_metadata = (current_user_id, num_of_comments, num_of_followers, num_of_following,
    #                                  num_of_likes_received, reputation)
    #     usermap[current_user_id] = current_user_metadata
    #
    #
    # for j in range(len(commenter_id_list8)):
    #     current_user_id = commenter_id_list8[j]
    #     updated_user_detail_url = user_detail_url4 + str(current_user_id)
    #     api_response = call_url(updated_user_detail_url)
    #     parsed_response = api_response[
    #         'response']  # Get the value list of dicts corresponding to key "response"
    #     num_of_followers = str(parsed_response['numFollowers'])
    #     num_of_following = str(parsed_response['numFollowing'])
    #     num_of_comments = str(parsed_response['numPosts'])
    #     num_of_likes_received = str(parsed_response['numLikesReceived'])
    #     reputation = str(parsed_response['reputation'])
    #     current_user_metadata = (current_user_id, num_of_comments, num_of_followers, num_of_following,
    #                                  num_of_likes_received, reputation)
    #     usermap[current_user_id] = current_user_metadata

    return usermap


'''
Main function
'''


def main():

    comment_author_ids = []  # Init the list to store ids of all users who made comments

    # Init the files
    comment_file = open("C:\Users\Owner\Desktop\Data\\article_comments.txt", 'r')
    user_metadata_file = open("C:\Users\Owner\Desktop\Data\\user_metadata_wired.txt", 'w')
    user_metadata_file.write('user_id' + '\t' + 'num_of_comments' + '\t' + 'num_of_followers' + '\t' +
                             'num_of_following' + '\t' + 'num_of_likes_received' + '\t' + 'reputation' + '\n')

    # Read the comment file and create a list of all commentor's ids.
    for line in comment_file:
        line = line.strip()
        commentor_metadata = line.split('\t')
        if len(commentor_metadata) == 3:
            current_commentor = commentor_metadata[1]
            comment_author_ids.append(current_commentor)

    print len(comment_author_ids)
    comment_author_ids = list(set(comment_author_ids))  # Remove duplicates
    print len(comment_author_ids)
    print comment_author_ids

    # Generate user details data dump
    user_map = generate_commenters_data(comment_author_ids)
    print len(user_map)
    for user_id in user_map:
        current_user_metadata = user_map[user_id]
        num_of_comments = str(current_user_metadata[1])
        num_of_followers = str(current_user_metadata[2])
        num_of_following = str(current_user_metadata[3])
        num_of_likes_received = str(current_user_metadata[4])
        reputation = str(current_user_metadata[5])

        user_metadata_file.write(user_id + '\t' + num_of_comments + '\t' + num_of_followers + '\t' +
                                 num_of_following + '\t' + num_of_likes_received + '\t' + reputation + '\n')


    comment_file.close()

# ----------------------------Functions Section Ends--------------------------#

if __name__ == "__main__":
    main()
