import re
log_entries = "[2023-04-15 10:30:45] INFO: User 'john_doe' logged in successfully with password 'secure123'; \
[2023-04-15 11:15:20] ERROR: Failed login attempt for user 'alice_smith' with password 'incorrect123'; \
[2023-04-15 12:05:55] INFO: User 'bob_jones' logged in successfully with password 'password123'; \
[2023-04-15 13:40:30] ERROR: Invalid credentials for user 'jane_davis' with password 'expired456'; \
[2023-04-15 14:02:10] INFO: User 'mike_lee' logged in successfully with password 'abc1234'; \
[2023-04-15 14:45:01] ERROR: Failed login attempt for user 'susan_wilson' with password 'wrongpass789'; \
[2023-04-15 15:00:00] INFO: User 'david_brown' logged in successfully with password 'mypassword987'; \
[2023-04-15 15:30:22] ERROR: Invalid credentials for user 'emily_taylor' with password 'oldpass123'; \
[2023-04-15 16:12:13] INFO: User 'natalie_white' logged in successfully with password 'qwerty1234'; \
[2023-04-15 16:45:10] ERROR: Failed login attempt for user 'robert_hall' with password 'password321'; \
[2023-04-15 17:00:33] INFO: User 'william_smith' logged in successfully with password 'letmein2024'; \
[2023-04-15 17:20:45] ERROR: Invalid credentials for user 'olivia_stewart' with password 'wrongpassword'; \
[2023-04-15 18:00:55] INFO: User 'patrick_moore' logged in successfully with password 'test12345'; \
[2023-04-15 18:30:10] ERROR: Failed login attempt for user 'grace_martin' with password 'forgottenpassword'; \
[2023-04-15 19:10:55] INFO: User 'lily_jackson' logged in successfully with password 'hello1234'; \
[2023-04-15 19:50:30] ERROR: Invalid credentials for user 'hannah_smith' with password 'dummy456'; \
[2023-04-15 20:20:00] INFO: User 'jacob_white' logged in successfully with password 'mypassword2024'; \
[2023-04-15 21:10:45] ERROR: Failed login attempt for user 'george_clark' with password '1234password'; \
[2023-04-15 21:50:10] INFO: User 'ava_harris' logged in successfully with password 'newpass123'; \
[2023-04-15 22:15:25] ERROR: Invalid credentials for user 'logan_scott' with password 'invalidpassword789'; \
[2023-04-15 23:00:15] INFO: User 'sophia_king' logged in successfully with password 'password2024'; \
[2023-04-15 23:40:00] ERROR: Failed login attempt for user 'mason_lee' with password 'incorrectpass123'; \
[2023-04-16 00:15:30] INFO: User 'lucas_garcia' logged in successfully with password 'welcome123'; \
[2023-04-16 01:00:05] ERROR: Invalid credentials for user 'chloe_robinson' with password 'secret1234'; \
[2023-04-16 01:30:10] INFO: User 'jackson_brown' logged in successfully with password 'strongpass987'; \
[2023-04-16 02:00:50] ERROR: Failed login attempt for user 'zoe_james' with password 'incorrect321'; \
[2023-04-16 03:00:20] INFO: User 'benjamin_lee' logged in successfully with password 'qwerty098'; \
[2023-04-16 03:40:45] ERROR: Invalid credentials for user 'mia_martinez' with password 'wrongpass2024'; \
[2023-04-16 04:10:30] INFO: User 'isabella_johnson' logged in successfully with password 'newpassword123'; \
[2023-04-16 04:40:50] ERROR: Failed login attempt for user 'elijah_white' with password 'password111'; \
[2023-04-16 05:10:30] INFO: User 'madison_davis' logged in successfully with password 'passwordtest123'; \
[2023-04-16 06:00:15] ERROR: Invalid credentials for user 'evan_martin' with password 'expiredpass'; \
[2023-04-16 06:45:40] INFO: User 'olivia_harris' logged in successfully with password 'letmein1234'; \
[2023-04-16 07:20:55] ERROR: Failed login attempt for user 'charlotte_wilson' with password 'qwertyuiop'; \
[2023-04-16 08:00:05] INFO: User 'jackson_smith' logged in successfully with password 'supersecret123'; \
[2023-04-16 08:40:10] ERROR: Invalid credentials for user 'michael_taylor' with password 'randompass123'; \
[2023-04-16 09:10:30] INFO: User 'emily_brown' logged in successfully with password 'testingpass123'; \
[2023-04-16 09:50:45] ERROR: Failed login attempt for user 'grayson_jackson' with password 'abcd1234'; \
[2023-04-16 10:30:15] INFO: User 'ava_scott' logged in successfully with password '123abc456'; \
[2023-04-16 11:00:40] ERROR: Invalid credentials for user 'liam_moore' with password 'oldpassword123'; \
[2023-04-16 11:45:05] INFO: User 'emma_king' logged in successfully with password 'passwordnew123'; \
[2023-04-16 12:30:25] ERROR: Failed login attempt for user 'oliver_clark' with password 'wrongword567'; \
[2023-04-16 13:10:50] INFO: User 'noah_taylor' logged in successfully with password 'testpassword456';"



def extract_attempted_users(log):
    #   we only want the data that is inside the regex we use ?:
    #   ?: means everything enclosed in the matching
    regex_pattern = r'(?:User|user)\s{1}\'([a-zA-Z]+_[a-zA-Z]+)'
    users = re.findall(regex_pattern, log)

    return users


print(extract_attempted_users(log_entries))