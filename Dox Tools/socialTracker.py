import os
import requests
import time
try:
    from colorama import Fore
except:
    print('[!] Please install the "colorama" module.')
    print('[!] pip install colorama')
    c = input('[?] Would you like to install it now? (y/n): ')
    if c.lower().startswith('y'):
        os.system('pip install colorama')
        print('[+] Successfully installed "colorama" module.')
        print('[+] Please restart the program.')
        time.sleep(3)
    sys.exit()

username = input(f'[{Fore.BLUE}?{Fore.RESET}] Enter username: ')
  
instagram = f'https://www.instagram.com/{username}'
facebook = f'https://www.facebook.com/{username}'
twitter = f'https://www.twitter.com/{username}'
youtube = f'https://www.youtube.com/{username}'
blogger = f'https://{username}.blogspot.com'
google_plus = f'https://plus.google.com/s/{username}/top'
reddit = f'https://www.reddit.com/user/{username}'
wordpress = f'https://{username}.wordpress.com'
pinterest = f'https://www.pinterest.com/{username}'
github = f'https://www.github.com/{username}'
tumblr = f'https://{username}.tumblr.com'
flickr = f'https://www.flickr.com/people/{username}'
steam = f'https://steamcommunity.com/id/{username}'
vimeo = f'https://vimeo.com/{username}'
soundcloud = f'https://soundcloud.com/{username}'
disqus = f'https://disqus.com/by/{username}'
medium = f'https://medium.com/@{username}'
deviantart = f'https://{username}.deviantart.com'
vk = f'https://vk.com/{username}'
aboutme = f'https://about.me/{username}'
imgur = f'https://imgur.com/user/{username}'
flipboard = f'https://flipboard.com/@{username}'
slideshare = f'https://slideshare.net/{username}'
fotolog = f'https://fotolog.com/{username}'
spotify = f'https://open.spotify.com/user/{username}'
mixcloud = f'https://www.mixcloud.com/{username}'
scribd = f'https://www.scribd.com/{username}'
badoo = f'https://www.badoo.com/en/{username}'
patreon = f'https://www.patreon.com/{username}'
bitbucket = f'https://bitbucket.org/{username}'
dailymotion = f'https://www.dailymotion.com/{username}'
etsy = f'https://www.etsy.com/shop/{username}'
cashme = f'https://cash.me/{username}'
behance = f'https://www.behance.net/{username}'
goodreads = f'https://www.goodreads.com/{username}'
instructables = f'https://www.instructables.com/member/{username}'
keybase = f'https://keybase.io/{username}'
kongregate = f'https://kongregate.com/accounts/{username}'
livejournal = f'https://{username}.livejournal.com'
angellist = f'https://angel.co/{username}'
last_fm = f'https://last.fm/user/{username}'
dribbble = f'https://dribbble.com/{username}'
codecademy = f'https://www.codecademy.com/{username}'
gravatar = f'https://en.gravatar.com/{username}'
pastebin = f'https://pastebin.com/u/{username}'
foursquare = f'https://foursquare.com/{username}'
roblox = f'https://www.roblox.com/user.aspx?username={username}'
gumroad = f'https://www.gumroad.com/{username}'
newsground = f'https://{username}.newgrounds.com'
wattpad = f'https://www.wattpad.com/user/{username}'
canva = f'https://www.canva.com/{username}'
creative_market = f'https://creativemarket.com/{username}'
trakt = f'https://www.trakt.tv/users/{username}'
five_hundred_px = f'https://500px.com/{username}'
buzzfeed = f'https://buzzfeed.com/{username}'
tripadvisor = f'https://tripadvisor.com/members/{username}'
hubpages = f'https://{username}.hubpages.com'
contently = f'https://{username}.contently.com'
houzz = f'https://houzz.com/user/{username}'
blipfm = f'https://blip.fm/{username}'
wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'
hackernews = f'https://news.ycombinator.com/user?id={username}'
codementor = f'https://www.codementor.io/{username}'
reverb_nation = f'https://www.reverbnation.com/{username}'
designspiration = f'https://www.designspiration.net/{username}'
bandcamp = f'https://www.bandcamp.com/{username}'
colourlovers = f'https://www.colourlovers.com/love/{username}'
ifttt = f'https://www.ifttt.com/p/{username}'
ebay = f'https://www.ebay.com/usr/{username}'
slack = f'https://{username}.slack.com'
okcupid = f'https://www.okcupid.com/profile/{username}'
trip = f'https://www.trip.skyscanner.com/user/{username}'
ello = f'https://ello.co/{username}'
tracky = f'https://tracky.com/user/~{username}'
basecamp = f'https://{username}.basecamphq.com/login'
tradingview = f'https://www.tradingview.com/u/{username}'
truelancer = f'https://www.truelancer.com/freelancer/{username}'
repl_it = f'https://repl.it/@{username}'
bit_ly = f'https://bitly.com/u/{username}'
codepen = f'https://codepen.io/{username}'
codesandbox = f'https://codesandbox.io/u/{username}'
codechef = f'https://www.codechef.com/users/{username}'
codeforces = f'https://codeforces.com/profile/{username}'
codesignal = f'https://app.codesignal.com/profile/{username}'
coderbyte = f'https://coderbyte.com/profile/{username}'
hackerrank = f'https://www.hackerrank.com/{username}'
hackerearth = f'https://www.hackerearth.com/@{username}'
auth0 = f'https://{username}.auth0.com'
codewars = f'https://www.codewars.com/users/{username}'
codeschool = f'https://www.codeschool.com/users/{username}'
codesnap = f'https://codesnap.io/users/{username}'
codescalers = f'https://www.codescalers.com/profile/{username}'
codeeval = f'https://www.codeeval.com/profile/{username}'
codeproject = f'https://www.codeproject.com/Members/{username}'
codeshare = f'https://codeshare.io/user/{username}'
codegym = f'https://codegym.cc/users/{username}'
codecademy = f'https://www.codecademy.com/{username}'
codechef = f'https://www.codechef.com/users/{username}'
codecombat = f'https://codecombat.com/play/ladder/{username}'
codeconquest = f'https://www.codeconquest.com/profile/{username}'
codecool = f'https://www.codecool.com/profile/{username}'
codehs = f'https://codehs.com/users/{username}'
codeigniter = f'https://codeigniter.com/user_guide/{username}'
codeinstitute = f'https://codeinstitute.net/profiles/{username}'

def banner():
    print(f"""
{Fore.RED}
███████╗██╗  ██╗██╗██████╗ ██████╗ ██╗   ██╗██╗  ██╗██╗████████╗
██╔════╝██║ ██╔╝██║██╔══██╗██╔══██╗╚██╗ ██╔╝██║ ██╔╝██║╚══██╔══╝
███████╗█████╔╝ ██║██║  ██║██║  ██║ ╚████╔╝ █████╔╝ ██║   ██║   
╚════██║██╔═██╗ ██║██║  ██║██║  ██║  ╚██╔╝  ██╔═██╗ ██║   ██║   
███████║██║  ██╗██║██████╔╝██████╔╝   ██║   ██║  ██╗██║   ██║   
╚══════╝╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝   ╚═╝   
{Fore.RESET}
by focat // focat@eyeware.systems

[REPO] https://github.com/Code1Tech/SkiddyKit
[GITHUB] https://github.com/Code1Tech
""")


web = [
instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus, 
medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, basecamp,
repl_it, bit_ly, codepen, codesandbox, codechef, codeforces, codesignal, coderbyte,
hackerrank, hackerearth, auth0, codewars, codeschool, codeshare, codegym, codecademy, codesnap,
codeinstitute, codehs, codeigniter, codeconquest, codecool, codecombat, codeproject, codeeval,  
codescalers,]

def search():
    print(f'[{Fore.BLUE}+{Fore.RESET}] Searching for accounts with the name "{username}"...')
    time.sleep(2.5)
    print(f'[{Fore.GREEN}~{Fore.RESET}] ~ Results ~')

    accurateLinks = []
    allLinks = []
    for url in web:
        r = requests.get(url)

        if r.status_code == 200:
            print(f'[{Fore.BLUE}+{Fore.RESET}] Found a match!')
            print(f'[{Fore.RED}-{Fore.RESET}] Link: {url}\n[{Fore.RED}-{Fore.RESET}] Webpage status code: {r.status_code}')
            if username in r.text:
                print(f'[{Fore.BLUE}+{Fore.RESET}] Username: {username} - text has been detected in url. This might be accurate.\n')
                accurateLinks.append(url)
                allLinks.append(url)
            else:
                print(f'[{Fore.RED}!{Fore.RESET}] Username: {username} - text has not been detected in url, could be a false positive.\n')
                allLinks.append(url)

    total = len(web)
    print(f'[{Fore.GREEN}~{Fore.RESET}] {len(allLinks)} out of {total} matches were found.')
    print(f'[{Fore.GREEN}~{Fore.RESET}] {len(accurateLinks)} of these matches were accurate.')
    c = input(f"[{Fore.BLUE}?{Fore.RESET}] Would you like to save the results to a file? (y/n): ")
    if c.lower().startswith('y'):
        print(f'[{Fore.BLUE}+{Fore.RESET}] Saving results to file...')
        with open('results.txt', 'w') as f:
            f.write(f'[+] ~ Results ~')
            f.write(f'[~] {len(allLinks)} matches were found.')
            f.write(f'[~] {len(accurateLinks)} of these matches were accurate.')
            f.write(f'[~] ~ Accurate Links ~')
            for link in accurateLinks:
                f.write(f'[+] {link}')
            f.write('--------------------------------------------')
            f.write(f'[~] ~ All Links ~')
            for link in allLinks:
                f.write(f'[{Fore.BLUE}+{Fore.RESET}] {link}')
        print(f'[{Fore.GREEN}~{Fore.RESET}] Results have been saved to "results.txt"')
    print(f'[{Fore.GREEN}~{Fore.RESET}] Exiting...')
    time.sleep(1)
    sys.exit()

if __name__=='__main__':
    banner()
    search()