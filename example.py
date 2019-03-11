"""
    instabot example

    Workflow:
    Repost best photos from users to your account
    By default bot checks username_database.txt
    The file should contain one username per line!
"""

import argparse
import os
import sys
import json
import time

from tqdm import tqdm

import instagram_scraper as insta

insta_profiles = [
'billgates',
'joerogan'
]

userdb = '\n'.join(insta_profiles)+'\n'

file = open("userdb.txt","w")
file.write(userdb)
file.close()

file = open("username_database.txt","w")
file.write("maskofshiva")
file.close()


number_last_photos = 3
x = 0

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot, utils


USERNAME_DATABASE = 'username_database.txt'
POSTED_MEDIAS = 'posted_medias.txt'


def repost_best_photos(bot, users, amount=1):
    medias = get_not_used_medias_from_users(bot, users)
    medias = sort_best_medias(bot, medias, amount)
    for media in tqdm(medias, desc='Reposting photos'):
        repost_photo(bot, media)


def sort_best_medias(bot, media_ids, amount=1):
    best_medias = [bot.get_media_info(media)[0] for media in tqdm(media_ids, desc='Getting media info')]
    best_medias = sorted(best_medias, key=lambda x: (x['like_count'], x['comment_count']), reverse=True)
    return [best_media['pk'] for best_media in best_medias[:amount]]


def get_not_used_medias_from_users(bot, users=None, users_path=USERNAME_DATABASE):
    if not users:
        users = utils.file(users_path).list
    users = map(str, users)
    total_medias = []
    for user in users:
        medias = bot.get_user_medias(user, filtration=False)
        medias = [media for media in medias if not exists_in_posted_medias(media)]
        total_medias.extend(medias)
    return total_medias


def exists_in_posted_medias(new_media_id, path=POSTED_MEDIAS):
    medias = utils.file(path).list
    return str(new_media_id) in medias


def update_posted_medias(new_media_id, path=POSTED_MEDIAS):
    medias = utils.file(path)
    medias.append(str(new_media_id))
    return True


def repost_photo(bot, new_media_id, path=POSTED_MEDIAS):
    if bot.upload_photo(instapath, "#model #models #Modeling #modelo #modellife #modelling #modelagency #Modelos #modelphotography #modelsearch #ModelStatus #modelingagency #modelfitness #ModelsWanted #modelshoot #modella #modelmanagement #modelscout #modeltest #modelindonesia #modele #modelife #modelmayhem #modelgirl #modell #modelslife #modelkids #modelcall #modelpose #ModelBehavior"):
        update_posted_medias(new_media_id, path)
        bot.logger.info('Media_id {0} is saved in {1}'.format(new_media_id, path))


parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
parser.add_argument('-file', type=str, help="users filename")
parser.add_argument('-amount', type=int, help="amount", default=1)
parser.add_argument('users', type=str, nargs='*', help='users')
args = parser.parse_args()

bot = Bot()
bot.login()

users = None
if args.users:
    users = args.users
elif args.file:
    users = utils.file(args.file).list

while x < len(insta_profiles):
    imgScraper = insta.InstagramScraper(usernames=[insta_profiles[x]], maximum=number_last_photos, media_metadata=True, latest=True,media_types=['image'])
    imgScraper.scrape()
    print("image scraping is running or not")

    try:
        with open(insta_profiles[x] + '/' + insta_profiles[x] + '.json', 'r') as j:
            json_data = json.load(j)
            newstr = (json_data[0]["display_url"])
            imgUrl = newstr.split('?')[0].split('/')[-1]
            instapath = insta_profiles[x] + '/' + imgUrl
            print(instapath)
        repost_best_photos(bot, users, args.amount)
        time.sleep(600)
    except:
        print("User is set to Private scraping next user")
    x += 1
