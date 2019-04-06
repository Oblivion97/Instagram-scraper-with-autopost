![image](https://raw.githubusercontent.com/reliefs/Instagram-scraper-with-autopost/master/img/banner.png)

Instagram scraper which scrapes peoples images use machine learning to recognise a face, if face
is detected it will repost that photo.

## Face detection at work on a live webcam 

![image](https://res.cloudinary.com/practicaldev/image/fetch/s--qdvR8Vl8--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://cloud.githubusercontent.com/assets/896692/24430398/36f0e3f0-13cb-11e7-8258-4d0c9ce1e419.gif)

Script now saves user session and and have CLI session. 
I also integrated it with instabot api.
90% of it are junk code I will fix it later.

This script scrapes images from users and then repost them under your Instagram accounts with your own tags.

Demo:
https://www.instagram.com/siliconeheaven/

## To install script:

```
Ubuntu:
sudo apt install cmake

Arch Linux:
sudo pacman -S cmake

git clone https://github.com/reliefs/Instagram-scraper-with-autopost.git

cd Instagram-scraper-with-autopost

sudo pip install -r requirements.txt

change instaprofiles.txt to the instagram profiles you wanna scrape

Run: python example.py
```

## Troubleshoot
If you are getting Illegal Instruction with face_recognition follow this guide:
https://github.com/ageitgey/face_recognition/issues/11#issuecomment-475482716

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE TERMS AND CONDITIONS FOR COPYING, DISTRIBIUTION AND MODIFICATION.

0. You just do WHAT THE FUCK YOU WANT TO.
