__author__ = 'Kunal'

'''
This script generates a file with all user/commentor's statistics and some updated features from old metadata file.
'''

# -------------------------- Constants Section Begin -------------------------------------#

# Input user comments file
user_comments_file = open('C:\Users\Owner\Desktop\Data\\article_comments.txt', 'r')

# Map to store updated metadata
user_comments_map = {}

# Input user metadata file
old_user_metadata_file = open('C:\Users\Owner\Desktop\Data\user_metadata_wired.txt', 'r')

# Map to store updated metadata
old_user_metadata_map = {}

# New output user metadata file with more features
new_user_metadata_file = open('C:\Users\Owner\Desktop\Data\updated_user_metadata_wired.txt', 'w')

# Map to store updated metadata
new_user_metadata_map = {}

# -------------------------- Constants Section End ---------------------------------------#


# -------------------------- Functions Section Begin -------------------------------------#

'''
Input:
Output:
'''


def populate_old_user_metadata_map():
    for line in old_user_metadata_file:
        line = line.strip()
        line = line.split('\t')
        user_id = line[0]
        num_of_comments = str(line[1])
        num_of_followers = str(line[2])
        num_of_following = str(line[3])
        num_of_likes_received = str(line[4])
        reputation = str(line[5])
        old_features = [num_of_comments, num_of_followers, num_of_following, num_of_likes_received, reputation]
        old_user_metadata_map[user_id] = old_features
    return


'''
Input: None
Output: Populated user comments map
'''


def populate_user_map():
    for line in user_comments_file:
        line = line.strip()
        line = line.split('\t')
        if len(line) == 3:  # Make sure there are 3 columns
            article_id = line[0]
            user_id = line[1]
            comment = line[2]
            comment_length = str(len(comment.split(' ')))
            article_comment_tuple = (article_id, comment, comment_length)
            if user_id not in user_comments_map:
                # Init the value as empty list. Then add all comments as tuples entries in the list.
                user_comments_map[user_id] = []
                user_comments_map[user_id].append(article_comment_tuple)
            else:
                # Entry already exists so simply add it to the map
                user_comments_map[user_id].append(article_comment_tuple)

    # Debug message
    print len(user_comments_map)

    # Compute two new features
    for key in user_comments_map:
        comment_features_list = user_comments_map[key]  # Get the list of tuples
        num_of_comments = len(comment_features_list)
        total_comment_length = 0.0
        for current_feature_tuple in comment_features_list:
            total_comment_length += int(current_feature_tuple[2])
        avg_comment_length = total_comment_length / num_of_comments

        # Add values to new map
        if key in old_user_metadata_map:
            new_user_metadata_map[key] = old_user_metadata_map[key]  # Add old feature
            new_user_metadata_map[key].append(num_of_comments)  # Add new features
            new_user_metadata_map[key].append(avg_comment_length)  # Add new features

    # Now write the map to a new file in tab delimited format as
    # user_id \t avg_comment_length \t num_of_comments_in_train_data

    for key in new_user_metadata_map:
        line = new_user_metadata_map[key]
        num_of_comments = str(line[0])
        num_of_followers = str(line[1])
        num_of_following = str(line[2])
        num_of_likes_received = str(line[3])
        reputation = str(line[4])
        num_of_commt = str(line[5])
        avg_cmt_len = str(line[6])

        new_user_metadata_file.write(key + '\t' + num_of_comments + '\t' + num_of_followers + '\t' +
                                     num_of_following + '\t' + num_of_likes_received + '\t' + reputation + '\t' +
                                     num_of_commt + '\t' + avg_cmt_len + '\n')

    print len(new_user_metadata_map)
    return


def main():
    populate_old_user_metadata_map()
    populate_user_map()
    # Close the file handlers
    old_user_metadata_file.close()
    user_comments_file.close()
    new_user_metadata_file.close()
    return


# -------------------------- Functions Section End ---------------------------------------#


if __name__ == "__main__":
    main()
