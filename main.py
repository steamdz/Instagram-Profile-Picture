import instaloader

Bot = instaloader.Instaloader()

User = 'steam_dz'

print(Bot.download_profile(User,profile_pic_only=True))