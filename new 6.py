import os
import re
import praw
import credentials

# create the objects from the imported modules

# reddit api login
reddit = praw.Reddit(credentials)

subreddit = reddit.subreddit('new') #,'hiphopheads','news','Music','BlackPeopleTwitter'])


# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))



# Get the values from our subreddit and reply to post
subreddit = reddit.subreddit('music')
for submission in subreddit.hot():
    print(submission.title)

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("chris brown", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("A verbal argument ensued and Chris Brown pulled the vehicle over on an unknown street, reached over Robyn F. with his right hand, opened the car door and attempted to force her out. Brown was unable to force Robyn F. out of the vehicle because she was wearing a seat belt. When he could not force her to exit, he took his right hand and shoved her head against he passenger window of the vehicle, causing an approximate one-inch raised circular contusion. Robyn F. turned to face Brown and he punched her in the left eye with his right hand. He then drove away in the vehicle and continued to punch her in the face with his right hand while steering the vehicle with his left hand. The assault caused Robyn F.s mouth to fill with blood and blood to splatter all over her clothing and the interior of the vehicle. Brown looked at Robyn F. and stated, Im going to beat the shit out of you when we get home! You wait and see! The detective said Robyn F. then used her cell phone to call her personal assistant Jennifer Rosales, who did not answer. Robyn F. pretended to talk to her and stated, Im on my way home. Make sure the police are there when I get there. After Robyn F. faked the call, Brown looked at her and stated, You just did the stupidest thing ever! Now Im really going to kill you! Brown resumed punching Robyn F. and she interlocked her fingers behind her head and brought her elbows forward to protect her face. She then bent over at the waist, placing her elbows and face near her lap in [an] attempt to protect her face and head from the barrage of punches being levied upon her by Brown. Brown continued to punch Robyn F. on her left arm and hand, causing her to suffer a contusion on her left triceps (sic) that was approximately two inches in diameter and numerous contusions on her left hand. Robyn F. then attempted to send a text message to her other personal assistant, Melissa Ford. Brown snatched the cellular telephone out of her hand and threw it out of the window onto an unknown street. Brown continued driving and Robyn F. observed his cellular telephone sitting in his lap. She picked up the cellular telephone with her left hand and before she could make a call he placed her in a head lock with his right hand and continued to drive the vehicle with his left hand. Brown pulled Robyn F. close to him and bit her on her left ear. She was able to feel the vehicle swerving from right to left as Brown sped away. He stopped the vehicle in front of 333 North June Street and Robyn F. turned off the car, removed the key from the ignition and sat on it. Brown did not know what she did with the key and began punching her in the face and arms. He then placed her in a head lock positioning the front of her throat between his bicep and forearm. Brown began applying pressure to Robyn F.s left and right carotid arteries, causing her to be unable to breathe and she began to lose consciousness. She reached up with her left hand and began attempting to gouge his eyes in an attempt to free herself. Brown bit her left ring and middle fingers and then released her. While Brown continued to punch her, she turned around and placed her back against the passenger door. She brought her knees to her chest, placed her feet against Browns body and began pushing him away. Brown continued to punch her on the legs and feet, causing several contusions. Robyn F. began screaming for help and Brown exited the vehicle and walked away. A resident in the neighborhood heard Robyn F.s plea for help and called 911, causing a police response. An investigation was conducted and Robyn F. was issued a Domestic Violence Emergency Protective Order.")
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)
        else:
            print('Keywords Not Found' + submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")


# Get the values from the comments in our subreddit and reply
if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []

for comments in subreddit.stream.comments():
    #print(subreddit.comment)

    # If we haven't replied to this post before
    if comments not in comments_replied_to:

        # Do a case insensitive search
        if re.search("chris brown", submission.title, re.IGNORECASE):
            # Reply to the post
            comments.reply("A verbal argument ensued and Chris Brown pulled the vehicle over on an unknown street, reached over Robyn F. with his right hand, opened the car door and attempted to force her out. Brown was unable to force Robyn F. out of the vehicle because she was wearing a seat belt. When he could not force her to exit, he took his right hand and shoved her head against he passenger window of the vehicle, causing an approximate one-inch raised circular contusion. Robyn F. turned to face Brown and he punched her in the left eye with his right hand. He then drove away in the vehicle and continued to punch her in the face with his right hand while steering the vehicle with his left hand. The assault caused Robyn F.s mouth to fill with blood and blood to splatter all over her clothing and the interior of the vehicle. Brown looked at Robyn F. and stated, Im going to beat the shit out of you when we get home! You wait and see! The detective said Robyn F. then used her cell phone to call her personal assistant Jennifer Rosales, who did not answer. Robyn F. pretended to talk to her and stated, Im on my way home. Make sure the police are there when I get there. After Robyn F. faked the call, Brown looked at her and stated, You just did the stupidest thing ever! Now Im really going to kill you! Brown resumed punching Robyn F. and she interlocked her fingers behind her head and brought her elbows forward to protect her face. She then bent over at the waist, placing her elbows and face near her lap in [an] attempt to protect her face and head from the barrage of punches being levied upon her by Brown. Brown continued to punch Robyn F. on her left arm and hand, causing her to suffer a contusion on her left triceps (sic) that was approximately two inches in diameter and numerous contusions on her left hand. Robyn F. then attempted to send a text message to her other personal assistant, Melissa Ford. Brown snatched the cellular telephone out of her hand and threw it out of the window onto an unknown street. Brown continued driving and Robyn F. observed his cellular telephone sitting in his lap. She picked up the cellular telephone with her left hand and before she could make a call he placed her in a head lock with his right hand and continued to drive the vehicle with his left hand. Brown pulled Robyn F. close to him and bit her on her left ear. She was able to feel the vehicle swerving from right to left as Brown sped away. He stopped the vehicle in front of 333 North June Street and Robyn F. turned off the car, removed the key from the ignition and sat on it. Brown did not know what she did with the key and began punching her in the face and arms. He then placed her in a head lock positioning the front of her throat between his bicep and forearm. Brown began applying pressure to Robyn F.s left and right carotid arteries, causing her to be unable to breathe and she began to lose consciousness. She reached up with her left hand and began attempting to gouge his eyes in an attempt to free herself. Brown bit her left ring and middle fingers and then released her. While Brown continued to punch her, she turned around and placed her back against the passenger door. She brought her knees to her chest, placed her feet against Browns body and began pushing him away. Brown continued to punch her on the legs and feet, causing several contusions. Robyn F. began screaming for help and Brown exited the vehicle and walked away. A resident in the neighborhood heard Robyn F.s plea for help and called 911, causing a police response. An investigation was conducted and Robyn F. was issued a Domestic Violence Emergency Protective Order.")
            print("Bot replying to : ", comments)

        else:
            print('Keywords Not Found')

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for comments in comments_replied_to:
        f.write(post_id + "\n");